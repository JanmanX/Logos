#!/bin/bash

echo "This script is just for testing purpose"

aarch64-linux-gnu-as -o program.o program.as
aarch64-linux-gnu-ld -o program program.o

echo "Done" 
