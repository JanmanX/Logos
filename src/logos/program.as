.text
.global _main
_main:
    sub sp, sp, #0
    main:
    mov x9, #1
    mov x9, x9
    mov x9, x9
    mov x9, #2
    sub sp, sp, #64
    str x8, [sp, #0]
    str x9, [sp, #8]
    str x10, [sp, #16]
    str x11, [sp, #24]
    str x12, [sp, #32]
    str x13, [sp, #40]
    str x14, [sp, #48]
    str x15, [sp, #56]
    bl test
    ldr x8, [sp, #0]
    ldr x9, [sp, #8]
    ldr x10, [sp, #16]
    ldr x11, [sp, #24]
    ldr x12, [sp, #32]
    ldr x13, [sp, #40]
    ldr x14, [sp, #48]
    ldr x15, [sp, #56]
    add sp, sp, #64
    mov x9, x0

mov     X16, #1  // System call number 1 terminates this program
svc     #0x80  // Call kernel to terminate the program
    
