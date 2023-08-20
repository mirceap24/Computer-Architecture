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
        part = n & 0x7f # n % 128
        n >>= 7 
        if n > 0:
            # part += 0b10000000
            part |= 0x80 
        out.append(part)
    return bytes(out)

def decode(varn):
    """
    1. Initialize a counter for the number of bytes processed
    2. Initialize the result to 0
    3. For each byte in the varint:
       - Extract the lower 7 bits
       - Shift them to their appropriate position and add to the result
       - If the MSB is not set, stop processing
    """
    result = 0 
    shift = 0 
    for byte in varn:
        # get the lower 7 bits and shift them to their appropriate position
        result |= (byte & 0x7F) << shift
        # if MSB is not set this is the last byte 
        if not (byte & 0x80):
            break 
        shift += 7
    return result

def decode_multiple(data):
    """
    Decode a byte string containing multiple varints.

    1. Initialize an empty list to store the decoded integers.
    2. Process each byte in the input data:
        a. Start decoding a new number.
        b. While the MSB (most significant bit) of the current byte is set,
           this indicates that the current varint continues to the next byte.
        c. Extract the lower 7 bits of the byte, and shift them to the 
           correct position based on the number of bytes processed for the 
           current varint.
        d. When a byte is encountered with the MSB not set, this indicates 
           the end of the current varint.
        e. Add the decoded number to the list.
    3. Return the list of decoded integers.
    """
    decoded_values = []
    i = 0 
    while i < len(data):
        current_value = 0 
        shift = 0 
        while data[i] & 0x80:
            current_value |= (data[i] & 0x7F) << shift
            shift += 7 
            i += 1 
        # decode the last byte for the current varint 
        current_value |= (data[i] & 0x7F) << shift 
        i += 1 
        decoded_values.append(current_value)
    return decoded_values

def zigzag_encode_32(n):
    """
    ZigZag encoding for 32-bit signed integers.

    The main purpose of ZigZag encoding is to transform signed integers
    into unsigned integers, where numbers with small absolute value (both
    positive and negative) have small varint encoded byte size.

    Steps:
    1. Left shift the number by 1. This operation essentially makes space
       for the least significant bit to be used as the sign bit.
    2. If the number is negative, we XOR the shifted number with 1. 
       This is equivalent to subtracting 1. Otherwise, we XOR with 0. 
       This operation essentially interweaves positive and negative numbers.
       The positive numbers are represented by even numbers and the negative
       numbers by odd numbers.
    """
    return (n << 1) ^ (n >> 31)

def zigzag_encode_64(n):
    return (n << 1) ^ (n >> 63)

def zigzag_decode(encoded):
    return (encoded >> 1) ^ -(encoded & 1)



if __name__ == '__main__':
    cases = (
        ('1.uint64', b'\x01'),
        ('150.uint64', b'\x96\x01'),
        ('maxint.uint64', b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\01'),
    )
    for fname, expectation in cases:
        with open("varint/" + fname, 'rb') as f:
            n = struct.unpack('>Q', f.read())[0]
            assert encode(n) == expectation
    
    for fname, encoded in cases:
        assert decode(encode(n)) == n
    
    multi_cases = [
        (b'\x01', [1]),
        (b'\x01\x96\x01', [1, 150]),
        (b'\x01\x96\x01\xac\x02', [1, 150, 300]),
        (b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\01\x01', [2**64 - 1, 1]),  # Max UINT64 followed by 1
    ]
    for encoded, expectation in multi_cases:
        assert decode_multiple(encoded) == expectation
        
    print('Ok!')
