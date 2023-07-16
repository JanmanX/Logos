from IL import *
from IL.RegisterAllocator import  *

def test_kill_label():
    instruction = InstructionLabel(AtomId('label'))
    kill = get_kill(instruction)
    assert kill == set()

def test_kill_assign():
    instruction = InstructionAssign(AtomId('a'), AtomId('b'))
    kill = get_kill(instruction)
    assert kill == set('a')

    instruction = InstructionAssign(AtomId('a'), AtomNum(1))
    kill = get_kill(instruction)
    assert kill == set('a')

def test_kill_assign_binop():
    instruction = InstructionAssignBinop(AtomId('a'), Binop.ADD, AtomId('b'), AtomId('c'))
    kill = get_kill(instruction)
    assert kill == set('a')

    instruction = InstructionAssignBinop(AtomId('a'), Binop.ADD, AtomId('b'), AtomNum(1))
    kill = get_kill(instruction)
    assert kill == set('a')

    instruction = InstructionAssignBinop(AtomId('a'), Binop.ADD, AtomNum(1), AtomId('b'))
    kill = get_kill(instruction)
    assert kill == set('a')

    instruction = InstructionAssignBinop(AtomId('a'), Binop.ADD, AtomNum(1), AtomNum(2))
    kill = get_kill(instruction)
    assert kill == set('a')
