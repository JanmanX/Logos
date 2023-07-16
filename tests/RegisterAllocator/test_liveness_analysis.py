from IL.RegisterAllocator import *
from IL import *


def test_simple_program():
    program = Program(
        data=[],
        instructions=[
            InstructionAssign(AtomId('a'), AtomNum(1)),
            InstructionAssign(AtomId('b'), AtomNum(2)),

            InstructionAssign(AtomId('c'), AtomId('a')),
            InstructionAssign(AtomId('c'), AtomId('b')),
            InstructionAssign(AtomId('c'), AtomId('a')),
        ]
    )

    # Test liveness analysis
    colors = liveness_analysis(program, 2)


    assert colors