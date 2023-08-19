## Base 128 Varint Encoder/Decoder

This repository contains an exercise that will serve as a guide in implementing the Base 128 Varint encoding as used in Protocol Buffers. The purpose of this exercise is to provide a practical exploration of an interesting encoding and to introduce fundamental concepts associated with binary data such as understanding hexadecimal, byte ordering, and bitwise operations.

### Getting Started

Before you dive into coding, it's important to have a clear understanding of the problem and the technology involved. Start by reading the [Protocol Buffers Encoding Documents](https://protobuf.dev/programming-guides/encoding/#varints). This guide will give you an in-depth understanding of varints and their encoding, which is the primary concept involved in this exercise.

### What to Implement

The main task is to develop an encode and decode function.

- The `Encode Function` should accept an unsigned 64-bit integer as input and return a sequence of bytes in the varint encoding that Protocol Buffers uses.

* The `Decode Function` should perform the inverse of the encode function, i.e. accept the byte sequence produced by the encode function and convert it back into the unsigned 64-bit integer.
