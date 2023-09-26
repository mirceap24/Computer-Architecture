import struct


def encode(n):
    """
    This function encodes the given integer 'n' into a varint
    following the varint encoding scheme. In this scheme:
    1. The integer is processed 7 bits at a time.
    2. The most significant bit (MSB) of each byte is used as a continuation flag.
    3. The continuation flag is set to 1 for all bytes except the last byte, which has a flag of 0.
    4. The function returns the encoded bytes.
    """
    out = [] # Initialize an empty list to hold the parts of the varint encoding.
    while n > 0:
        part = n & 0x7F # extract the 7 least significant bits
        n >>= 7 # right shift 'n' by 7 bits, effectively discarding the 7 bits we just processed
        if n > 0: # If there are more bits to process, set the MSB of 'part' to 1.
            part |= 0x80 # This sets the MSB by using the bitwise OR operation with 0b10000000.
        out.append(part)
    return bytes(out)

def decode(varn):
    """
    This function decodes a varint encoded byte sequence 'varn' back into an integer.
    1. It iterates through the bytes in 'varn' in reverse order.
    2. It shifts the accumulator left by 7 bits to make room for the next 7 bits from the current byte.
    3. It discards the most significant bit (MSB) of the current byte, which is the continuation flag in varint encoding.
    4. It accumulates the 7 bits from the current byte into the accumulator.
    5. Finally, it returns the decoded integer.
    """
    n = 0  # Initialize the accumulator to 0.

    for b in reversed(varn):  # Iterate through the bytes in 'varn' in reverse order.
        n <<= 7  # Shift the accumulator left by 7 bits to make room for the next 7 bits.
        n |= (b & 0x7f)  # Discard the MSB of the current byte, and accumulate the remaining 7 bits into the accumulator.

    return n  # Return the decoded integer.


for n in range(10):
    assert decode(encode(n)) == n

print("ok!")
