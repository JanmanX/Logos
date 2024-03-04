# The Logos programming language
The Logos programming language is a hobby language intended for extreme simplicity and
ease of interoperation with the OS.

## Features
### No types
Everything is 64 bits.

### Extensibility
Preprocess (m4, cpp, etc), assemble  and link any way you like.

You can link it with any library of your chosing. I usually use the Linux C
standard library. For MacOS, a template libc.a is provided in the `libc/`
directory.


## Build (optional)
```bash
pip install build
python -m build
```

## Installation
```bash
pip install dist/logos-0.0.1-py3-none-any.whl
```

## Usage
```bash
python -m logos program.l -o program.s
```

## Example (Apple Silicon)
```bash
python -m logos examples/fib.l -o fib.s
as -o fib.o fib.s
ld -o fib fib.o -lc -L libc/macos/arm64
./fib
echo $?
```

## Example (Linux)
```bash
python -m logos examples/fib.l -o fib.s
as -o fib.o fib.s
ld -o fib fib.o
./fib
echo $?
```


## To do
- [ ] Implement optimization step
- [ ] Testing for generated assembly
- [ ] Implement easier way to initialize large arrays with values
- [ ] RISC-V backend
- [ ] x86_64 backend

