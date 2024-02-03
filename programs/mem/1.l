# Notes
# - It _has_ to be on stack, because otherwise functions being called
#   recursivelly might overwrite static addresses
#

# notation
mem <NAME> <SIZE>

# Example
mem buffer_addr 20
mem buffer_addr2 30

# Usage
mem[buffer_addr + 10] = 10
mem[buffer_addr] = 20

a = mem[buffer_addr]
b = mem[buffer_addr + 10]


# Then I could probably do something like
i = 0
while i < 2:
    mem[i] = a
    i = i + 1
