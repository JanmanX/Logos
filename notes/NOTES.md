# Notes

## Building
To generate parsers:
```
$ antlr4 -Dlanguage=Python3 -visitor -o ./generated Logos.g4
```

## Assembling
```
$ as -o program.o program.as
```

## Linking
```
$ ld -o program program.o
```


## Debugging
### LLDB

Setting breakpoint
```
(lldb) breakpoint set --name main
```

Reading registers:
```
(lldb) register read
```
