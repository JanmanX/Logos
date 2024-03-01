#!/bin/bash

echo "This script is just for testing purpose"

as -o program.o program.as
ld -o program program.o -lc 

echo "Done" 
