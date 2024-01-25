#!/bin/bash

echo "This script is just for testing purpose"

aarch64-linux-gnu-as -o test test.S  
aarch64-linux-gnu-ld -o test.o test   

echo "Done" 