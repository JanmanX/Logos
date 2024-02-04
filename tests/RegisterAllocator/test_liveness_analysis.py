from IL.RegisterAllocator import *


def test_simple_ritual():


    ritual = Ritual(
        id = AtomId('main'),
        args = [],
        data=[],
        variable_colors={},
        instructions=[
            InstructionAssign(AtomId('a'), AtomNum(1)),
            InstructionAssign(AtomId('b'), AtomNum(2)),

            InstructionAssign(AtomId('c'), AtomId('a')),
            InstructionAssign(AtomId('c'), AtomId('b')),
            InstructionAssign(AtomId('c'), AtomId('a')),
        ]
    )

    # Test liveness analysis
    colors = allocate_registers(ritual=ritual, num_registers=2)

    assert colors
