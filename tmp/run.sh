#!/bin/bash

# Compile
nasm -f elf64 -o output.o simple.s

# Link
ld -m elf_x86_64 -o output output.o

# run
./output
