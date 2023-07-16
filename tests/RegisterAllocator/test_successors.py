from IL import *
from IL.RegisterAllocator import *

def test_get_successors():
    instructions = [
        InstructionLabel('label'),
        InstructionAssign(AtomId('a'), AtomId('b')),
        InstructionAssign(AtomId('b'), AtomId('c')),
        InstructionAssign(AtomId('c'), AtomId('a')),
    ]

    successors = get_successors(instructions)

    assert successors == [
        {1}, {2}, {3}, {4}
    ]

def test_get_successors_branching():
    instructions = [
        InstructionLabel(AtomId('label')),
        InstructionAssign(AtomId('a'), AtomId('b')),
        InstructionGoto(AtomId('label')),
        InstructionIf(AtomId('a'), AtomId('label'), AtomId('label_false')),
        InstructionLabel(AtomId('label_false')),
    ]

    successors = get_successors(instructions)

    assert successors == [
        {1}, {2}, {0}, {0, 4}, {5}
    ]