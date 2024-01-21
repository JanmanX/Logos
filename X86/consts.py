# https://faculty.nps.edu/cseagle/assembly/sys_call.html


PROG_START = """
section .data

section .text 
global _start

_start:
"""

PROG_END = """
    mov rax, 0x3c       ; sys_exit
    mov rdi, 0x00       ; exit code
    syscall
"""

ASSIGN_FMT = """
    mov {reg}, {val}    ; assign {val} to {reg}
"""

PRINT_FMT = """
    push 0x0A
    push {reg}          ; register to print

    mov rax, 0x01       ; sys_write
    mov rdi, 0x01       ; stdout
    mov rsi, rsp        ; pointer to top of stack where value is stored
    mov rdx, 0x09       ; length of string. 8 bytes for 64 bit register
    syscall    

    add rsp, 0x09       ; pop the stack

    """

EXIT_FMT = """
    mov rax, 0x3c       ; sys_exit
    mov rdi, {reg}      ; exit code   
    syscall
    """
