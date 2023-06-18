from IL.RegisterAllocator import *
from IL import *
from utils.graph import *


graph = Graph.from_edges([('a', 'b'), ('b','c')])
simplified = simplify(graph, 6)
print(simplified)
exit(0)

program = Program([
    InstructionAssign(AtomId('n'), AtomNum(32)),
    InstructionAssign(AtomId('a'), AtomId('n')),
    InstructionAssign(AtomId('b'), AtomNum(1)),
    InstructionAssign(AtomId('z'), AtomNum(0)),

    InstructionAssignBinop(AtomId('_if'), Binop.EQ, AtomId('n'), AtomId('z')),
    InstructionLabel(AtomId('loop')),
    InstructionIf(AtomId('_if'), AtomId('_body'), AtomId('_end')),
    InstructionLabel(AtomId('_body')),
    InstructionAssignBinop(AtomId('t'), Binop.ADD, AtomId('a'), AtomId('b')),
    InstructionAssign(AtomId('a'), AtomId('b')),
    InstructionAssign(AtomId('b'), AtomId('t')),
    InstructionAssignBinop(AtomId('n'), Binop.SUB, AtomId('n'), AtomNum(1)),
    InstructionAssign(AtomId('z'), AtomNum(0)),
    InstructionGoto(AtomId('loop')),
    InstructionLabel(AtomId('_end')),
    InstructionReturn(AtomId('a'))
])

liveness_analysis(program)