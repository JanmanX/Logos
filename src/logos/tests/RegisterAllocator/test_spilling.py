from IL.RegisterAllocator import *

def test_spilling():
    ritual = Ritual('test', [], [], {}, {})
    ritual.instructions = [
        InstructionAssign(AtomId('a'), AtomNum(1)),
        InstructionAssign(AtomId('b'), AtomNum(1)),
        InstructionAssign(AtomId('c'), AtomNum(1)),

        # Ensure liveness, so read from a, b, c
        InstructionAssign(AtomId('d'), AtomId('a')),
        InstructionAssign(AtomId('e'), AtomId('b')),
        InstructionAssign(AtomId('f'), AtomId('c')),
    ]

    c = allocate_registers(ritual, num_registers=2)

    print(c)
 

