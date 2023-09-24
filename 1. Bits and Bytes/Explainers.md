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

- In computers, we often use binary numbers to represent data. An unsigned binary number is a representation where all the bits are positive weights.
- Imagine a bar graph where every bit position ` i`` in the number adds a height of  `2^i` to the bar.

## Two's-Complement Encoding (B2T)

- Two's complement is a method to represent both positive and negative numbers in binary.
- The most significant bit determines the sign of the number.
- Range:
  - Smallest: `-2^(w-1)`
  - Largest: `2^(w-1) - 1`
  - For a 4-bit number, it will be -8 and 7
- Alternative Representations:
  - One's Complement (B20): flipping all the bits gets the negative representation. This has two representations for zero.
  - Sign Magnitude (B2S): leftmost bit indicates sign, rest of bits represent magnitude. Also has two zeros: positive and negative.
- Programming Considerations:
  - Portability: Different computers might represent numbers differently.
  - Java Standards: Java uses two's complement with specified bit widths.
  - C Standards: C provides varying sizes for data types like int and long. For guaranteed sizes, C99 introduced types like int32_t.

## Conversion Between Signed and Unsigned

- In the C programming language, one can cast between various numeric data types. An important aspect to note is the casting between signed(`int`) and unsigned(`unsigned int`) integers. From a purely mathematical standpoint, there are several conventions you might think of for such conversions. For instance, should converting a negative to `unsigned` give zero? However, C's approach is mainly from a bit-level perspective rather than a numeric one.

* Consider the example:

```C
short int v = -12345;
unsigned short uv = (unsigned short) v;
printf("v = %d, uv = %u\n", v, uv);
```

On a two's-complement machine, this code outputs:

```
v = -12345, uv = 53191

```

- The key takeaway is that the bit patterns of the values remain identical, but their interpretation changes. The 16-bit two's complement representation of -12345 matches the 16-bit unsigned representation of 53191.

* In another scenario:

```C
unsigned u = 4294967295u; /* UMax */
int tu = (int) u;

```

The output is:

```
u = 4294967295, tu = -1

```

- For a 32-bit word size, the bit patterns representing `4.294.967.295` (unsigned) and `-1` (two's complement) are identical.

* To delve deeper into the conversion process, we can define a set of mathematical functions:
  - `U2Bw`: maps numbers to their bit representations in unsigned form
  - `T2Bw`: maps numbers to their bit representations in two's complement form.

- We can also define:

  - `T2Uw(x)`: Given a two's-complement number x, yields an unsigned number with the same bit pattern
  - `U2Tw(x)`: Given an unsigned number x, yields a two's-complement number with the same bit pattern

  ```
  T2Uw(x) =
  - x + 2^w if x < 0
  - x if x ≥ 0

  ```

  - For instance, T2U16(-12345) = 53.191
  - To sum it up, conversions between signed and unsigned integers in C is based on a bit-level perspective. Within a certain range, the numeric values have the same representation in both formats. Outside this range, conversions either add or subtract 2^w.

  ## Signed versus Unsigned in C

  - C supports both signed and unsigned arithmetic for its integer data types.
  - Most machines use two's complement for signed numbers, although the C standard doesn't mandate it.
  - By default, most numbers in C are considered signed. Appending `U` or `u` makes a constant unsigned.
  - C allows conversion between unsigned and signed. On most systems, the underlying bit pattern doesn't change during these conversions. For example, converting -1 (signed) to unsigned won't alter its bit representation but will change its interpretation.
  - Explicit casting can be done using syntax like `(int) ux`, which converts the unsigned variable `ux` to signed. However, conversions can also occur implicitly. For instance, if you assign an unsigned value to a signed variable without casting, the value is implicitly cast to signed
  - `printf` doesn't use type information. It simply interprets the bits of a value based on the format specifier (%d, %u, %x, etc.). Thus, you can print a signed integer using %u or an unsigned integer using %d. This might produce unexpected results if you're not careful.

  For example:

  ```
  int x = -1;
  unsigned u = 2147483648; /* 2 to the 31st */
  printf("x = %u = %d\n", x, x);
  printf("u = %u = %d\n", u, u);

  ```

- This code produces:

```
x = 4294967295 = -1
u = 2147483648 = -2147483648

```

- This result occurs because `%u` interprets the bit pattern as an unsigned integer and `%d` interprets it as a signed integer. In two's complement, `-1 is represented by all 1s, which is `4294967295`when interpreted as an unsigned integer. Similarly,`2147483648`(2^31) is the smallest possible signed 32-bit integer when interpreted in two's complement, hence`2147483648`
- C has a rule where if one operand of an operation is signed and the other is unsigned, the signed operand is implicitly cast to unsigned. This can result in unexpected behavior, especially with relational operators.

```C
int signed_var = -1;
unsigned int unsigned_var = 0;
if (signed_var < unsigned_var) {
    /* This block won't execute */
}

```

- In the above code, the comparison `-1 < 0U` seems like it should be true, but it's not. This is because `-1` gets implicitly cast to unsigned, which is `4294967295` for a 32-bit int. Therefore, the actual comparison becomes false.

## Expanding the Bit Representation of a Number

- When we move from a smaller to a larger integer type, the process involves adding extra bits to the representation. There are two primary methods, depending on whether the number is signed or unsigned:
  - ZERO EXTENSION (FOR UNSIGNED NUMBERS): for unsigned numbers, simply add leading zeros
  - SIGN EXTENSION (FOR SIGNED NUMBERS): for two's-complement signed numbers, extend the number by copying the most significant bit (MSB)

```C
short sx = -12345; /* -12345 */
2 unsigned short usx = sx; /* 53191 */
3 int x = sx; /* -12345 */
4 unsigned ux = usx; /* 53191 */
5
6 printf("sx = %d:\t", sx);
7 show_bytes((byte_pointer) &sx, sizeof(short));
8 printf("usx = %u:\t", usx);
9 show_bytes((byte_pointer) &usx, sizeof(unsigned short));
10 printf("x = %d:\t", x);
```

```
sx = -12345: cf c7
usx = 53191: cf c7
x = -12345: ff ff cf c7
ux = 53191: 00 00 cf c7
```

- `sx` and `usx` both have representation `cf c7` when considered as 16-bit numbers.
- when `sx` is cast to a 32-bit integer, it is sign extended, resulting in `ff ff cf c7`
- when `usx` is cast to a 32-bit unsigned integer, it is zero extended, resulting in `00 00 cf c7`

* The order in which you change the size and type of a number matters in C. For instance, in the code snippet:

```C
short sx = -12345;
unsigned uy = sx;
```

- The value of `uy` isn't immediately obvious. What happens is that `sx` is first converted to a regular `int` (with sign extension) and then to an `unsigned` (which just reinterprets the bits). The conversion results in the value `4294954951` with a memory representation of `ff ff cf c7`
- In C, when you assign a smaller type to a larger type, the smaller type is first promoted to the larger type. In this case, `short` is promoted to `int`. Since `sx` is a negative short, sign extension occurs, and its `int` representation is negative as well. When this negative `int` is assigned to an `unsigned`, the bits don't change, ut the interpretation does. So, the two's complement representation of `-12345` as an `int` is interpreted as `4294954951` when viewed as an `unsigned`

## Truncation in Computer Arithmetic

When working with data types, the number of bits allocated for a value is fixed. However, sometimes, for various reasons, the number of bits representing a number might be reduced, leading to truncation. Truncation essentially removes the higher-order bits, which can alter the value.

### Unsigned numbers:

Truncating unsigned numbers is relatively straightforward since we're only dealing with positive integers. When you truncate an unsigned number, you are essentially "chopping off" the most significant bits.

- Principle:
  For an unsigned number x represented by the bit vector x = [xw−1, xw−2, ... , x0], when truncated to k bits to get x', the numeric value x' is x mod 2^k.
- Example:
  Suppose we have an 8-bit unsigned number `x` represented as `11010101` (decimal: 213). Truncating this to 4 bits would give `x` as `0101` (decimal 5). The numeric value is equivalent to `213 mod 2^4 = 5`.

### Two's-Complement Numbers

Two's-complement numbers include both positive and negative numbers, with the MSB determining the sign. When truncating, the MSB might shift, effectively changing the number's sign and magnitude.

- Principle:
  For `x` in two's-complement form, when truncated to `k` bits to get `x`, the value is: `x` = U2Tk(x mod 2^k)`
- Example:
  Consider the number `x = 53191` (in 32-bit `int`). This value in binary is: `0000 0000 0000 1100 1101 1111 0111`
  If we truncate this to a 16-bit `short`, we only consider: `1100 1101 1111 0111`
  This binary represents `-12345` in two's-complement form, thus `x = -12345`

### Practical Scenarios

- 1. Memory Limitations: On embedded systems with limited memory, sometimes, to save space, developers might truncate larger data types into smaller ones
- 2. Network Communications: When sending data over a network, a device might truncate values to adhere to specific protocols or to improve transmission speed
- 3. Data Compression: In compression algorithms, truncation might be used to achieve higher compression rations
- 4. Data Type Casting: In programming, when you cast a larger data type to a smaller one(like `int` to `short` in C), truncation can occur

## Understanding Implicit Casting In C

Implicit casting in C is where the compiler automatically convers one data type into another without explicit instruction. This can lead to unintended behavior.

```C
float sum_elements(float a[], unsigned length) {
    int i;
    float result = 0;
    for (i = 0; i <= length-1; i++)
        result += a[i];
    return result;
}
```

`PROBLEM`: When `length` is 0, the loop condition `i <= length - 1` wraps around because `length - 1` is unsigned. Thus, instead of terminating, the loop accesses memory out-of-bounds, leading to an error.

Solution:

```C
for (i = 0; i < length; i++)
```

- C has both signed and unsigned integers. Unsigned integers are mainly used when considering words as collections of bits
- Java, however, doesn't have unsigned integers. It exclusively uses signed two's-complement integers. The usual shift operation `>>` in Java is arithmetic, while `>>>` performs a logical shift

## Integer Arithmetic

Arithmetic operations on a computer can sometimes produce unexpected results due to finite word sizes.

### Unsigned Addition

When two non-negative integers, `x` and `y` (each less than `2^w`), are added, their sum can be in the range `0` to `2^(w+1) - 2`. This sum might require more than `w` bits. To handle this, C uses modular arithmetic.

- Example:
  Consider a 4-bit representation of numbers:

```makefile
x = 9  -> 1001
y = 12 -> 1100
```

Their integer sum is 21 (10101 in binary). Since this is a 5-bit number, and we're using a 4-bit representation, we drop the highest bit and get `0101`, which is 5 in decimal. So, `9 + 12 = 5` when considering 4-bit unsigned addition.

- Detecting Overflow: An overflow in unsigned addition occurs if the result is less than either of the operands. If `s = x + y` and `s < x`, then an overflow has occurred.

### Unsigned Negation

In C, negating an unsigned number doesn't simply invert its bits. Instead, the result is computed as the modulus minus the number.

- Example:
  For 4-bit numbers:

```makefile
x = 3 -> 0011
-u4 x = 2^4 -3 = 13 -> 1101
```

The negation of `3` in a 4-bit representation is `13`.

## Two's-Complement Addition Simplified:

Two's complement representation is commonly used in computers to represent signed integers. The highest bit represents the sign (0 for positive and 1 for negative), and the remaining bits represent the magnitude.
For instance, for a 3-bit number:

- `010` is +2, `110` is -2.

When adding two numbers in two's-complement representation, the sum might fall outside the range that can be represented with the given number of bits. In such cases, we get an overflow.

- Positive Overflow: Occurs when we add two positive numbers but get a negative result
- Negative Overflow: Occurs when we add two negative numbers but get a positive result

Given a w-bit two's complement system:

- range for numbers: -2^(w-1) to 2^(w-1)-1
- the sum of two numbers in this range can be from -2^w to 2^w - 2

There are three main scenarios:

- Normal Scenario: The sum falls within the representable range. No overflow occurs.
- Positive Overflow: The sum exceeds the positive range and wraps around from the highest positive to the smallest negative
- Negative Overflow: The sum exceeds the negative range and wraps around from the most negative to the largest positive

- Examples:

* 010 (+2) + 001 (+1) = 011 (+3)
* 011 (+3) + 001 (+1) = 100 (-4). Here, the actual sum, but it can't be represented, so it wraps to -4
* 101 (-3) + 110 (-2) = 011 (+3). Here, the actual sum is -5, but it wraps to +3.

### Detecting Overflow

- Positive Overflow: If both numbers are positive, but the sum is negative or zero.
- Negative Overflow: If both numbers are negative, but the sum is positive or zero.

## Two's Complement Negation

Two's-complement is a system used to represent both positive and negative integers in binary. This system was developed so that computers can do subtraction by addition operations.

### Special Bit Patterns

For an 8-bit representation:

- The largest positive number we can represent is `01111111`, which is 127 in decimal.
- The smallest negative number (the largest magnitude negative) is `10000000`, which is -128 in decimal.

### Negating in Two's-complement

To negate (or find the additive inverse) of a number in two's complement:

- Flip all the bits - one's complement
- Add 1 to the result

Let's apply this negation technique to our smallest 8-bit number, -128, which has the binary representation `10000000`.

- flip all the bits: 01111111
- add 1 to the result: 10000000

This phenomenon occurs because in two's-complement arithmetic, the smallest representable number is its own additive inverse. In other words, the negative of the most negative number is still that number. This is a unique property of two's-complement representation. It doesn't mean that the negative of -128 is -128 in the usual mathematical sense; it's just that in the confines of 8-bit two's-complement representation, that's how it works.

## Unsigned Multiplication:

When multiplying unsigned numbers, we are sometimes concerned that the result may need more bits than we have space for. As a result, the product is taken modulo 2^w where w is the bit width. For example, if you multiply two 8-bit numbers and the result needs 10 bits, only the lowest 8 bits of the result are kept.

Let's multiply two 8-bit numbers: A = 10011010 and B = 11010101.

```scss
      10011010   (154 in decimal)
    x 11010101   (213 in decimal)
  ______________
      10011010   (A shifted 0 places)
     00000000    (A shifted 1 place since the corresponding bit in B is 0)
    10011010     (A shifted 2 places)
   00000000      (A shifted 3 places)
  10011010       (A shifted 4 places)
 00000000        (A shifted 5 places)
00000000         (A shifted 6 places)
10011010         (A shifted 7 places)
________________
  1010111101110   = 28,782 in decimal
```

But since we are only keeping the lowest 8 bits, the result is `1110110` = 238 in decimal.

## Two's Complement Multiplication:

Multiplying two numbers in two's complement notation is similar to multiplying them in standard binary. However, when working in a fixed bit-width like 8-bits, overflow can occur, and the product may need to be truncated or wrapped around.

Let's compute the product of -3 and -5 using 8-bi two's complement:

- -3 in 8-bit two's complement: 11111101
- -5 in 8-bit two's complement: 11111011

Multiplication:
11111101 (-3 in decimal)
x 11111011 (-5 in decimal)

---

     11111101   (multiplied by 1, the rightmost bit of -5)
    11111101   (multiplied by 1, shifted 1 place to the left)

00000000 (multiplied by 0, shifted 2 places to the left)
00000000 (multiplied by 0, shifted 3 places to the left)
00000000 (multiplied by 0, shifted 4 places to the left)
00000000 (multiplied by 0, shifted 5 places to the left)
00000000 (multiplied by 0, shifted 6 places to the left)
11111101 (multiplied by 1, shifted 7 places to the left)

---

1111101011

Now, since we're working with 8-bits, we take the rightmost 8 bits, which is 11101011 => -85.

### Multiplying by Constants

Multiplication by a power of 2 is efficiently done using bit shifting. For example, multiplying a number `x` by `2^k` is the same as shifting `x` to the left by `k` positions.

When a program has expressions like `x * 14`, a smart compiler can replace this multiplication with a combination of shifting, addition, and subtractions, since it's faster.

- EXAMPLE: `x * 14` can be re-written as `(x << 3) + (x << 2) + (x << 1)` which translates to three shift operations and two addition operations, replacing the slower multiplication operation.

In assembly language, there's an instruction called `lea` (Load Effective Address) that can also be used for certain multiplication operations, especially when the multiplier is a small constant.

- To compute `3 * x`, the expression can be re-written as `(x << 1) + x`, which is two times `x` plus `x`. This can be computed with a single `lea` instruction.

### Division and Right Shifting in C

In computing, division is relatively slow compared to other operations like addition, subtraction, and multiplication. However, division by a power of 2 can be significantly faster by utilizing bit shifting operations. In C, this is achieved with the `>>` operator.

- Division by Power of 2 for Unsigned Integers:

* For unsigned integer division, a logical right shift can be used to divide a number by a power of 2. The operation `x >> k` in C is equivalent to the division `x / 2^k`.

- Division by a Power of 2 for Signed Integers:

* When dividing signed integers, it's important to consider how they are represented in binary. In most systems, signed integers are represented using two's complement notation. In this notation, the leftmost bit (most significant bit) is used to represent the sign of the number: 0 for positive and 1 for negative.
* When you right shift a signed integer, the operation fills in the leftmost bits with the sign bit(an operation known as sign extension) to keep the sign of the number the same => AIRTHMETIC RIGHT SHIFT.
* However, there's a caveat with negative numvers. Integer division in C rounds towards 0, but right shifting rounds down. So, if you right shift -9, you might not get the expected result:

```C
int x = -9;  // Binary: 11110111
int result = x >> 1;  // Binary: 11111011 = -5 (but -9 / 2 = -4.5, rounded towards 0 = -4)

```

To fix this rounding issue, you can add a "bias" to the negative number before right shifting.

```C
int k = 1;
int result = (x + (1 << k) - 1) >> k;  // (1 << k) - 1 = 1, so (-9 + 1) >> 1 = -4

```

This adjusts the rounding for negative x. The expression (1 << k) - 1 computes a bias, which when added to x, ensures that the division rounds towards zero.

## Understanding Floating-Point Representation

Floating-point representation is a way to write real numbers that allows for a wide range of values with a consistent number of digits. It is especially useful when dealing with very large or very small numbers, or when approximating real numbers in calculations. The IEEE 754 standard has been widely adopted since 1985 to ensure consistency and accuracy in representing and operating on floating-point numbers across different computer systems.

The IEEE 754 Standard specifies the representation for floating-point numbers including the bit layour and the operations on them, ensuring consistency across different computing systems. This format separates the bits into three parts:

- Sign bit(s): 1 bit
- Exponent (e): 8 or 11 bits
- Fraction (f): 23 or 52 bits
  The value of the number is calculated as (-1)^s _ (1 + f) _ 2^(e - 127)
