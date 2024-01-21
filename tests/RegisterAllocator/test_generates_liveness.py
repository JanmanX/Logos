from IL.RegisterAllocator import *


def test_gen_label():
    instruction = InstructionLabel('label')
    gen = get_gen(instruction)
    assert gen == set()


def test_gen_assign_var():
    instruction = InstructionAssign(AtomId('a'), AtomId('b'))
    gen = get_gen(instruction)
    assert gen == set('b')


def test_gen_assign_binop_vars():
    instruction = InstructionAssignBinop(AtomId('a'), Binop.ADD, AtomNum(1), AtomNum(2))
    gen = get_gen(instruction)
    assert gen == set()


def test_gen_assign_binop_var_num():
    instruction = InstructionAssignBinop(AtomId('a'), Binop.ADD, AtomId('b'), AtomNum(2))
    gen = get_gen(instruction)
    assert gen == set('b')


def test_gen_assign_binop_num_var():
    instruction = InstructionAssignBinop(AtomId('a'), Binop.ADD, AtomNum(1), AtomId('b'))
    gen = get_gen(instruction)
    assert gen == set('b')


def test_gen_assign_binop_vars():
    instruction = InstructionAssignBinop(AtomId('a'), Binop.ADD, AtomId('b'), AtomId('c'))
    gen = get_gen(instruction)
    assert gen == set(['b', 'c'])
