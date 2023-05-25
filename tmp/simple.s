section .data

section .text

global _start

_start:
    mov rax, 'DEADBEEF'

	mov rax, 0x1181391
    push rax          ; register to print

;     push 'A'

    mov rax, 0x01       ; sys_write
    mov rdi, 0x01       ; stdout
    mov rsi, rsp 	; pointer to top of stack where value is stored
    mov rdx, 0x08       ; length of string. 8 bytes for 64 bit register
    syscall


    mov rax, 0x3c	; 60
    mov rdi, 0x00 	; exit code
    syscall

