import argparse

from antlr4 import *

from IL.ILGenerator import ILGenerator
from IL.RegisterAllocator import allocate_registers
from codegen import Architecture, TargetConfig, codegen
from generated.LogosLexer import LogosLexer
from generated.LogosParser import LogosParser


def main(program_path: str, config: TargetConfig, output_path: str, output_ast: bool = False):
    input_stream = FileStream(program_path)
    lexer = LogosLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LogosParser(stream)
    tree = parser.prog()

    # Parse
    visitor = ILGenerator()
    program = visitor.visit(tree)

    # Analyze
    for ritual in program.rituals:
        ritual.variable_register_map = allocate_registers(ritual, num_registers=config.num_registers)

    # Codegen
    code = codegen(program, config)

    # Output
    with open(output_path, 'w') as f:
        f.write(code)

    if output_ast:
        with open(output_path + '.ast', 'w') as f:
            for ritual in program.rituals:
                for instruction in ritual.instructions:
                    f.write(str(instruction))
                    f.write('\n')
                f.write('\n')

    print(code)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Logos compiler')
    parser.add_argument("program", help="program")
    parser.add_argument('-a', '--arch', help='Target architecture', default='arm')
    parser.add_argument('-o', '--output', help='Output file', default='program.as')
    parser.add_argument('-d', '--debug', help='Output debug file', action='store_true')
    args = parser.parse_args()

    # Setup config
    target_config = TargetConfig.from_architecture(Architecture[args.arch.upper()])

    # Go!
    main(args.program, target_config, args.output, args.debug)
