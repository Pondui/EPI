Integers in python are represented in **bit arrays**. Python uses variable length bit arrays to represent numbers. Internally, python represents negative integers through an operation called **2s complement**, which is a map that takes the binary representation of the positive integer and generates the corresponding binary representation of the negative integer.

Binary is a base 2 counting system, with each bit representing a numerical value of 2^n where n is position of the bit. So the 0th bit, when set - meaning when it is not empty, represents 2^0 = 1. The 1st bit represents 2^1 = 2, the 2nd bit represnets 2^2 = 4, and so on. For example, the nunmber 5 in binary would be 101 which is equivalent to 1\*2^2 + 0\*2^1 + 1\*2^0. To get the binary representation of the negative integer, i.e. -5, we take the 2s complement of the positive binary representation.

To take the 2s complement, perform take the NOT of the word and then add 1. For example 6 in binary is 0110, it's 2s complement is ~0110 + 1 = 1001 + 1 = 1010, which represents the decimal -6. It doesn't matter what your word size is, but typically the word size is a power of two. We also always leave the leftmost bit empty for positive numbers, and set it for negative numbers. The table below illustrates this with a word size of 4.


|Decimal|Binary|
|---|---|
|-4|1100|
|-3|1101|
|-2|1110|
|-1|1111|
|0|0000|
|1|0001|
|2|0010|
|3|0011|
|4|0100|

Operators that act directly on bits are called **bitwise operators**. All bitwise operators are binary operators, meaning they take two inputs and return a single output, except for the NOT operator, which is unary. They are as follows:

|Name|Symbol|
|---|---|
|AND|&|
|OR|\||
|NOT|~|
|XOR|^|
|RIGHT SHIFT|>>|
|LEFT SHIFT|<<|

Note that when counting bits, I count from right to left starting from 0. This convention is also used when clearing/setting the first/last n bits.