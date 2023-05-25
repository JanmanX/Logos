# https://faculty.nps.edu/cseagle/assembly/sys_call.html



PROG_START = """
section .data
    output db "%x", 0x10, 0x00  

section .text 

global _start

_start:
"""


PROG_END = """
    mov rax, 0x01       ; sys_exit
    mov rbx, 0x00       ; exit code
    INT 0x80
"""

ASSIGN_FMT = """
    mov {reg}, {val}
"""


PRINT_FMT = """
    push {reg}          ; register to print

    mov rax, 0x01       ; sys_write
    mov rdi, 0x01       ; stdout
    mov rsi, rsp        ; pointer to top of stack where value is stored
    mov rdx, 0x08       ; length of string. 8 bytes for 64 bit register
    syscall    

    add rsp, 0x08       ; pop the stack

    """
