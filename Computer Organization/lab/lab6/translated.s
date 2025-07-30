ldr R0, =0xC0FFEE00
ldr R1, =0xC0FFEE00

lsr R0, R0, #8
lsr R1, R1, #7
and R2, R0, R1

ldr R4, =0xFF000000
orr R2, R1, R4
lsl R2, R2, #6
ldr R5, =0xFF
eor R2, R2, R5