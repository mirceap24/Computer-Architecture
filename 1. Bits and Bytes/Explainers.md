### Virtual Memory:

- Memory is viewed by machine-level programs as a vast array of bytes termed `virtual memory`.
- Each byte in memory has a unique number called its `address`. The complete set of addresses is the `virtual address space`.
- The representation of this vast array is conceptual, with the actual implementation using a mix of DRAM, flash memory, disk storage, hardware, and OS software.

* The `C compiler` and `runtime system` partition this memory for storing program data, instructions, and control data. Management of this memory occurs within the virtual address space.
* A `pointer` in C has the virtual address of the first byte of storage. The C compiler uses this, coupled with type information, to generate machine-level code.

### Binary, Decimal, and Hexadecimal:

- A byte consists of 8 bits.
- In binary, its value varies from 00000000 to 11111111.
- When viewed as a decimal, its value ranges from `0` to `255`.
- For convenience, bit patterns are often represented in `hexadecima`. Hex uses digits `0-9` and `A-F` for 16 possible values. So, a byte in hexadecimal ranges from `00` to `FF``.
- In C, numbers starting with 0x or 0X are considered hexadecimal.

### Conversions Between Number Systems:

- Converting between binary and hexadecimal can be done one hex digit at a time.
- For example:
  - Hexadecimal value `0x173A4C` is equivalent to binary `000101110011101001001100`
  * Binary value `1111001010110110110011` translates to hexadecimal `3CADB3`
- For values that are powers of 2 (like `x = 2^n`), their hexadecimal representation can be quickly found. For instance, `2,048 (2^11)` in hexadecimal is `0x800`.

### Word Size and Virtual Address Space:

- The `word size` of a computer signifies the standard size of pointer data and is crucial in determining the maximum virtual address space.
- A machine with a w-bit word size can access virtual addresses ranging from 0 to 2^w-1, translating 2^w bytes.

### Transition from 32-bit to 64-bit:

- There's been a shift from 32-bit word size machines to 64-bit machines.
- `32-bit word size`: Limits the virtual address space to 4GB (about 4 × 10^9 bytes).
- `64-bit word size`: Offers a virtual address space of 16 exabytes (roughly 1.84 × 10^19 bytes).
  Many 64-bit computers maintain backward compatibility, capable of running 32-bit programs.

### Data Formats in Computers and C:

- Machines support varied data formats and lengths for encoding, such as bytes, integers (of 2-, 4-, and 8-byte lengths), and floating-point numbers (4- and 8-byte lengths).
- C Language Data Types:

  - C supports multiple formats for both integer and floating-point data. The byte allocations for various C data types might differ based on the 32-bit or 64-bit compilation.
  - Integer Data Types: can be signed (representing negative and positive values) or unsigned (only nonnegative values).
    - `char`: represents a byte. It might store integer values or characters.
    - `short`, `int`, and `long`: Offer a range of sizes. On 64-bit systems, `int` usually remains 4 bytes while `long` often shifts from 4 bytes (32-bit) to 8 bytes (64-bit).
  - Fixed-size integer types: ISO C99 introduced fixed-size types like `int32_t` (4 bytes) and `int64_t` (8 bytes) to provide consistency across machines and compilers.

  * Floating-point types: Include float (single precision, 4 bytes) and double (double precision, 8 bytes).
  * Pointers: A pointer (like `char *`) uses the full word size, be it 32-bit or 64-bit.

## Portability and Word Size Assumptions:

- Portability ensures a program runs correctly across different systems. While C standards set minimum ranges for data types, the exact sizes can vary, making some programs dependent on word size.

* Many programs written during the 32-bit era (around 1980-2010) made word size assumptions that can cause issues when migrated to 64-bit systems. An example of such an assumption is using `int` type for storing pointers, which is problematic for 64-bit programs.

## Addressing and Byte Ordering

- Multi-byte Objects in Memory: Multi-byte objects (like integers spanning 4 bytes) are stored in contiguous memory locations, with the address of the object being the smallest address of the sequence. For instance, if an integer variable is stored at address 0x100 and spans 4 bytes, it will occupy memory locations 0x100 through 0x103.
- Byte Ordering:
  - Little Endian: The least significant byte is stored first. Using the example integer 0x01234567, in little-endian format, 0x67 (the least significant byte) would be at the lowest address, 0x100.
  * Big Endian: The most significant byte is stored first. In the case of our example integer, 0x01 (the most significant byte) would be at the lowest address, 0x100.
- Intel-compatible machines mainly use little-endian, while machines from IBM and Oracle (due to their acquisition of Sun Microsystems) primarily use big-endian. However, some modern processors can operate in either mode (bi-endian). For instance, ARM microprocessors, popular in smartphones, can work in both modes but the dominant OSs for these processors, Android and iOS, operate only in little-endian.
- The choice between little and big endian is, in essence, arbitrary and has been a point of contention in computing history. The terms are derived from Jonathan Swift's "Gulliver's Travels" where there was a disagreement on which end of an egg should be cracked open. Generally, for application developers, the byte ordering of their machine remains inconspicuous.
- Problems arise mainly in networking, where data from a machine with one byte ordering is sent to another machine with a different ordering. This results in reversed bytes, which can lead to communication problems. Data sent over networks needs to adhere to established conventions to prevent such discrepancies. Another case where byte ordering is visible is when inspecting machine-level programs or when programming techniques bypass the usual type system, as can be done in C with casts and unions.

## Representing Strings and Code

- Strings in C are represented as arrays of characters, ending with a null (value 0) character. Commonly, characters are encoded using the ASCII standard. For instance, the string "12345" translates to the byte sequence `31 32 33 34 35 00` in ASCII. This representation remains consistens across different systems using the ASCII encoding, making text data more universally compatible than binary data.
- When examining a sample C function, the machine code generated varies based on the system and its specifications. This highlights that different machines or even the same machines with different operating systems can produce different binary representations for the same function. As a result, binary code is often not portable across varied machine and OS combinations.
- At the core of computer systems, a program is perceived as a sequence of bytes. The machine lacks knowledge about the program's source, operating mainly on byte sequences, with some additional auxiliary data potentially aiding debugging.

## Bit-Level Operations in C

- C supports bitwise Boolean operations, using symbols such as | for "or," & for "and," ~ for "not," and ^ for "exclusive-or." These operations can be applied to any integral data type. To best understand their effects, it's recommended to convert hexadecimal arguments to binary, perform the operation, and then revert to hexadecimal.
- A notable feature in C is the ability to perform bit-level operations without requiring a third location for temporary storage. This doesn't necessarily offer a performance advantage but serves as an intellectual exercise
- itwise operations in C can be confused with logical operations. The logical operations treat any nonzero value as true and 0 as false, returning 1 or 0 accordingly. Bitwise operations will match their logical counterparts only when arguments are 0 or 1. Logical operators, such as '&&' and '||', are distinct from their bit-level counterparts in their evaluation approach. For instance, logical operators may not evaluate their second argument if the result can be determined from the first.
- C also offers shift operations, which move bit patterns to the left or right. Left shift operations (<<) move bits to the left, dropping the most significant bits and filling the right with zeros. Right shift operations (>>) have two types: logical and arithmetic. Logical fills the left with zeros, while arithmetic fills with repetitions of the most significant bit, useful for signed integer data.
- However, the C standards aren't clear on which type of right shift should be used for signed numbers, leading to potential portability issues. Most systems use arithmetic right shifts for signed data. For unsigned data, logical shifts are mandatory. Java, in contrast, clearly defines its right shift behavior. The expression x >> k does an arithmetic shift, while x >>> k performs a logical shift.
- Regarding shifts beyond the size of a data type, C standards are ambiguous. On many machines, the shift amount is determined by the lowest log2 w bits of the amount, resulting in a modular approach (k mod w). Java, however, mandates the modular approach for shift operations.

## Understanding w-bit Binary Representation in C

- Consider a `w-bit` integer, represented as a bit vector. This bit vector can be denoted in two ways:
  - As `x``, which represents the entire vector.
  - As `[xw−1, xw−2, ... , x0]`, where each xi indicates an individual bit in the vector.
- Each bit, xi, in this vector can either be 0 or 1. If xi is 1, it implies the value 2^i should be included as part of the number's total value. This representation can be described by the function B2Uw (Binary to Unsigned of length w):

```
B2Uw(x) = Σ xi * 2^i  (from i=0 to w-1)

```

For example:

B2U4([0001]) = 1
B2U4([0101]) = 5
B2U4([1011]) = 11
B2U4([1111]) = 15
