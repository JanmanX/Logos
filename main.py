import os
import sys
from antlr4 import *
from generated.LogosLexer import LogosLexer 
from generated.LogosParser import LogosParser 
from X86.x86Listener import X86Listener
from X86.x86Visitor import X86Visitor

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = LogosLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LogosParser(stream)
    tree = parser.prog()

#     listener = X86Listener()
#     walker = ParseTreeWalker()
#     walker.walk(listener, tree)

    visitor = X86Visitor()
    code = visitor.visit(tree)

    print("Binary code:")
    print(code)

    # Output to file
    with open("out.asm", "w") as f:
        f.write(code)
    
    # Compile
    os.system("nasm -f elf64 out.asm -o out.o")

    # Link
    os.system("ld -m elf_x86_64 out.o -o out")




if __name__ == '__main__':
    main(sys.argv)