#include <stdio.h>
#include <assert.h>

// "Expression" means that you should write simple code
// that doesn't involve looping. Use bitwise operators like
// AND (&), OR(|), NOT(~), XOR(^), shift left logical (<<),
// shift right logical (>>>), shift right arithmetic (>>).

// You should try to solve each of these problems on paper before
// writing the code.

/* #1 Write an expression that results in the least significant
 byte of an integer x being preserved, but all other bits set to
 1. For example: 0x98234493 becomes 0xFFFFFF93.
 */
unsigned int Q1(unsigned int x) {
	unsigned int result = x | 0xFFFFFF00;
    return result;
}

/* #2 Write an expression that results in the least significant
byte of an integer x staying the same, but all other bits
complemented. For example: 0x98234493 becomes 0x67dcbb93.
*/
unsigned int Q2(unsigned int x) {
	unsigned int result = x ^ 0xFFFFFF00;
    return result;
}

/* #3 Write an expression that results in the least significant
    byte of an integer x being set to 0, but all other bits unchanged.
    For example: 0x98234493 becomes 0x98234400.
    */
unsigned int Q3(unsigned int x) {
	unsigned int result = x & 0xFFFFFF00;
    return result;
}

/* #4 Write an expression that is equivalent to x == y.
It should evaluate to 1 if and only if x and y are equal.
You may use the == operator but only if one of the operands is a constant
 */
unsigned int Q4(unsigned int x, unsigned int y) {
	if (x == y) {
		return 1;
	} else {
		return 0;
	}
}

/* #5 Write an expression that reverses the bytes of an
integer x. That is the least significant byte should be
swapped with the most significant byte, but the bits within
each byte should remain in their original order.
For example, 0xABCD1234 should be turned into 0x3412CDAB

HINTS: Try the problem without using hints. If you get really stuck you
can spoil one hint at a time using the converter at
http://www.geocachingtoolbox.com/index.php?lang=en&page=asciiConversion
Copy/paste the sequence of numbers into "Text:" and make sure to choose "from: decimal (base 10)" "to: Text (ASCII)"

Hint1: 84 114 121 32 116 111 32 99 111 109 112 117 116 101 32 101 97 99 104 32 111 102 32 116 104 101 32 52 32 110 101 119 32 98 121 116 101 115 32 115 101 112 97 114 97 116 101 108 121 32 97 110 100 32 116 104 101 110 32 99 111 109 98 105 110 101 32 116 104 101 109 32 105 110 116 111 32 97 32 115 105 110 103 108 101 32 105 110 116 46
Hint2: 84 111 32 99 111 109 112 117 116 101 32 116 104 101 32 112 97 114 116 105 97 108 32 97 110 115 119 101 114 32 119 104 101 114 101 32 116 104 101 32 109 111 115 116 32 115 105 103 110 105 102 105 99 97 110 116 32 98 121 116 101 32 105 115 32 99 111 114 114 101 99 116 32 97 110 100 32 116 104 101 32 114 101 115 116 32 111 102 32 116 104 101 32 98 105 116 115 32 97 114 101 32 48 44 32 121 111 117 32 119 111 117 108 100 32 115 104 105 102 116 32 108 101 102 116 32 116 104 101 32 108 101 97 115 116 32 115 105 103 110 105 102 105 99 97 110 116 32 98 121 116 101 32 111 102 32 120 32 98 121 32 104 111 119 32 109 97 110 121 32 98 105 116 115 63
Hint3: 70 111 114 32 65 66 67 68 49 50 51 52 44 32 121 111 117 114 32 102 111 117 114 32 112 97 114 116 105 97 108 32 97 110 115 119 101 114 115 32 109 97 121 32 98 101 32 51 52 48 48 48 48 48 48 44 32 48 48 49 50 48 48 48 48 48 48 44 32 48 48 48 48 67 68 48 48 44 32 97 110 100 32 48 48 48 48 48 48 65 66 46 32 72 111 119 32 100 111 32 121 111 117 32 99 111 109 98 105 110 101 32 116 104 101 115 101 32 102 111 117 114 32 105 110 116 115 32 105 110 116 111 32 116 104 101 32 102 105 110 97 108 32 97 110 115 119 101 114 63
*/
unsigned int Q5(unsigned int x) {
	unsigned int result = ((x & 0xFF) << 24) | (((x >> 8) & 0xff) << 16) | (((x >> 16) & 0xFF) << 8) | ((x >> 24) & 0xFF);
    return result;
}

int main() {
    // A few test cases are given here for the coding problems.
    // You should add additional test cases to provide yourself more evidence of correctness.

    // when debugging, if you want to print out an integer using hexadecimal
    // see example usage of printf in bitwiseOpsExamples.c

    // #1 complete Q1
    //    write more tests
    assert (Q1(0x98234493) == 0xFFFFFF93);
    assert (Q1(0x0F0ABC17) == 0xFFFFFF17);
    // #2 complete Q2
    //    write more tests
    assert (Q2(0x98234493) == 0x67dcbb93);
    assert (Q2(0xF0E0F03A) == 0x0F1F0F3A);
    // #3 complete Q3
    //    write more tests
    assert (Q3(0x98234493) == 0x98234400);
    assert (Q3(0xF0F0F1AB) == 0xF0F0F100);

    // #4 complete Q4
    //    write more tests
    assert (Q4(0xFFFF0000, 0xFFFF0000) == 1);
    assert (Q4(0xABCDEF00, 0xABCD1111) == 0);

    assert (Q5(0xABCD1234) == 0x3412CDAB);
    assert (Q5(0x01234567) == 0x67452301);
    
    /* #6 Reflect on your problem solving approach for the puzzles.
       What strategies did you use to decide on an initial implementation?
       What strategies did you use to revise or fix your initial implementation?
       */

    printf("Success\n");
}
