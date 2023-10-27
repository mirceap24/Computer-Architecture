import struct

with open('synflood.pcap', 'rb') as f:
    magic_number, major, minor, _, _, _, llh_type = struct.unpack('<IHHIIII', f.read(24))
    assert magic_number == 0xa1b2c3d4 # confirm that file is LE 
    print(f'Pcap protocol version {major}.{minor}')
    assert llh_type == 0 # loopback 

    count = 0
    initiated = 0 
    acked = 0
    while True:
        per_packet_header = f.read(16)
        if len(per_packet_header) == 0:
            break 
        count += 1
        _, _, length, untrunc_length = struct.unpack('<IIII', per_packet_header)
        assert length == untrunc_length # nothing truncated
        packet = f.read(length)
        assert struct.unpack('<I', packet[:4])[0] == 2 # ipv4
        ihl = (packet[4] & 0x0f) << 2 
        assert ihl == 20
        src, dst, _, _, flags = struct.unpack('!HHIIH', packet[24:38])
        syn = (flags & 0x0002) > 0
        ack = (flags & 0x0010) > 0
        if dst == 80 and syn:
            initiated += 1
        if src == 80 and ack: 
            acked += 1 
        print(f'{src} -> {dst}{syn and " SYN" or ""}{ack and " ACK" or ""}')
    print(f'{count} packets parsed {initiated} connections, {acked} '
          f'({acked / float(initiated):0.2f} %) acked')
