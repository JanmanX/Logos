import argparse

from antlr4 import *

from IL.ILGenerator import ILGenerator
from IL.RegisterAllocator import liveness_analysis
from codegen import Architecture, TargetConfig, codegen
from generated.LogosLexer import LogosLexer
from generated.LogosParser import LogosParser


def main(program_path: str, config: TargetConfig):
    input_stream = FileStream(program_path)
    lexer = LogosLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LogosParser(stream)
    tree = parser.prog()

    #     listener = X86Listener()
    #     walker = ParseTreeWalker()
    #     walker.walk(listener, tree)

    visitor = ILGenerator()
    program = visitor.visit(tree)

    program.variable_colors = liveness_analysis(program, num_registers=config.num_registers)


    print("Colors:")
    print(str(program.variable_colors))

    code = codegen(program, config)
    print("CODE: ")
    print("\n".join(code))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Logos compiler')
    parser.add_argument("program", help="program")
    parser.add_argument('-a', '--arch', help='Target architecture', default='arm')
    args = parser.parse_args()

    # Setup config
    target_config = TargetConfig.from_architecture(Architecture[args.arch.upper()])

    # Go!
    main(args.program, target_config)
