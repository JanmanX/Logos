.text
.global _main
_main:
stp x29, x30, [sp, #-16]!
bl main
mov x16, #1
svc #0x80
main:
    sub sp, sp, #0
    mov x9, #10
    mov x9, x9
    mov x9, #10
    mov x0, x9
    sub sp, sp, #80
    str x8, [sp, #0]
    str x9, [sp, #8]
    str x10, [sp, #16]
    str x11, [sp, #24]
    str x12, [sp, #32]
    str x13, [sp, #40]
    str x14, [sp, #48]
    str x15, [sp, #56]
    str x30, [sp, #64]
    bl fib
    ldr x8, [sp, #0]
    ldr x9, [sp, #8]
    ldr x10, [sp, #16]
    ldr x11, [sp, #24]
    ldr x12, [sp, #32]
    ldr x13, [sp, #40]
    ldr x14, [sp, #48]
    ldr x15, [sp, #56]
    ldr x30, [sp, #64]
    add sp, sp, #80
    mov x9, x0
    mov x9, x9
    mov x0, x9
    blr x30
    mov x0, #0
    blr x30
fib:
    sub sp, sp, #0
    mov x10, x0
    mov x9, #2
    cmp x9, #0
    beq l1
    bne l0
l0:
    mov x9, #1
    mov x0, x9
    blr x30
l1:
    mov x11, x10
    mov x9, #1
    sub x11, x11, x9
    mov x0, x9
    sub sp, sp, #80
    str x8, [sp, #0]
    str x9, [sp, #8]
    str x10, [sp, #16]
    str x11, [sp, #24]
    str x12, [sp, #32]
    str x13, [sp, #40]
    str x14, [sp, #48]
    str x15, [sp, #56]
    str x30, [sp, #64]
    bl fib
    ldr x8, [sp, #0]
    ldr x9, [sp, #8]
    ldr x10, [sp, #16]
    ldr x11, [sp, #24]
    ldr x12, [sp, #32]
    ldr x13, [sp, #40]
    ldr x14, [sp, #48]
    ldr x15, [sp, #56]
    ldr x30, [sp, #64]
    add sp, sp, #80
    mov x9, x0
    mov x11, x10
    mov x10, #2
    sub x11, x11, x10
    mov x0, x10
    sub sp, sp, #80
    str x8, [sp, #0]
    str x9, [sp, #8]
    str x10, [sp, #16]
    str x11, [sp, #24]
    str x12, [sp, #32]
    str x13, [sp, #40]
    str x14, [sp, #48]
    str x15, [sp, #56]
    str x30, [sp, #64]
    bl fib
    ldr x8, [sp, #0]
    ldr x9, [sp, #8]
    ldr x10, [sp, #16]
    ldr x11, [sp, #24]
    ldr x12, [sp, #32]
    ldr x13, [sp, #40]
    ldr x14, [sp, #48]
    ldr x15, [sp, #56]
    ldr x30, [sp, #64]
    add sp, sp, #80
    mov x10, x0
    mov x9, x9
    mov x10, x10
    add x9, x9, x10
    mov x0, x9
    blr x30
    mov x0, #0
    blr x30
