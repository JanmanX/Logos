import sys
from antlr4 import *
from generated.LogosLexer import LogosLexer 
from generated.LogosParser import LogosParser 
from X86.X86Listener import X86Listener

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = LogosLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LogosParser(stream)
    tree = parser.prog()

    listener = X86Listener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

 
if __name__ == '__main__':
    main(sys.argv)