import os
import sys
from antlr4 import *
from generated.LogosLexer import LogosLexer 
from generated.LogosParser import LogosParser 
from X86.x86Listener import X86Listener
from X86.x86Visitor import X86Visitor
from IL.ILGenerator import ILGenerator
from IL.RegisterAllocator import liveness_analysis

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = LogosLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LogosParser(stream)
    tree = parser.prog()

#     listener = X86Listener()
#     walker = ParseTreeWalker()
#     walker.walk(listener, tree)

    visitor = ILGenerator()
    program = visitor.visit(tree)

    print("Binary code:")
    print(str(program))


    liveness_analysis(program)

#     # Output to file
#     with open("out.asm", "w") as f:
#         f.write(code)
#     
#     # Compile
#     os.system("nasm -f elf64 out.asm -o out.o")
# 
#     # Link
#     os.system("ld -m elf_x86_64 out.o -o out")




if __name__ == '__main__':
    main(sys.argv)