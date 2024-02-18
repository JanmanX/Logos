.text
.global _main
_main:
    sub sp, sp, #32
    mov x10, #4
    mov x10, x10
    sub x9, sp, #32
    l0:
    mov x11, x10
    cmp x11, #0
    beq l2
    bne l1
    l1:
    mov x11, x10
    str x9, [x11]
    mov x10, x10
    mov x11, #1
    sub x10, x10, x11
    mov x10, x10
    mov x9, x9
    mov x11, #1
    add x9, x9, x11
    mov x9, x9
    b l0
    l2:

mov     X16, #1  // System call number 1 terminates this program
svc     #0x80  // Call kernel to terminate the program
    
