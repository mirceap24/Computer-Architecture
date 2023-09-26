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

def decode_one(varn):
    """
    Decodes a single varint from the given byte sequence starting at the given index.
    Returns the decoded integer and the index where the next varint begins.
    """
    n = 0  # Initialize the accumulator to 0.
    i = 0  # Set the current index to 0

    for b in varn[i:]:  # Start iterating from the given start index.
        n <<= 7  # Shift the accumulator left by 7 bits to make room for the next 7 bits.
        n |= (b & 0x7f)  # Discard the MSB of the current byte, and accumulate the remaining 7 bits into the accumulator.
        i += 1  # Increment the index.
        if not (b & 0x80):  # If the MSB is not set, this is the last byte in this varint.
            break

    return n  # Return the decoded integer and the next index.



for n in range(10):
    assert decode_one(encode(n)) == n

print("ok!")
