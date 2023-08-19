# take the unsigned 64-bit integer and think of it as a sequence of 7 bit integers
import struct 

def encode(n):
    """
    1. initialize an empty list to store the encoded bytes 
    2. process until n > 0 
    3. extract the least significant 7 bits of the number 
    4. shift the number to the right by 7 bits <=> divide by 128
    5. if there are still more bits left to encode after this byte, 
        set the MSB of the current byte to indicate continuation
    """
    out = []
    while n > 0:
        part = n % 128
        n >>= 7 
        if n > 0:
            # part += 0b10000000
            part |= 0x80 
        out.append(part)
    return bytes(out)

with open('varint/150.uint64', 'rb') as f:
    n = struct.unpack('>Q', f.read())[0]
    print(encode(n))
