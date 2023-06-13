from IL import *


def get_gen(instruction: Instruction) -> set:
    # Iterate over types of instruction
    if isinstance(instruction, InstructionLabel):
        return set()
    elif isinstance(instruction, AssignmentAtomInstruction):
        if isinstance(instruction.src, AtomId):
            return {instruction.src.id}
        else:
            return set()
    elif isinstance(instruction, AssignmentBinopInstruction):
        s = set()
        if isinstance(instruction.left, AtomId):
            s.add(instruction.left.id)
        if isinstance(instruction.right, AtomId):
            s.add(instruction.right.id)
        return s
    elif isinstance(instruction, AssignmentFromMemInstruction):
        if isinstance(instruction.atom, AtomId):
            return {instruction.atom.id}
    elif isinstance(instruction, AssignmentToMemInstruction):
        s = {instruction.mem}
        if isinstance(instruction.atom, AtomId):
            s.add(instruction.atom.id)
        return s
    elif isinstance(instruction, GotoInstruction):
        return set()
    elif isinstance(instruction, IfInstruction):
        if isinstance(instruction.atom, AtomId):
            return {instruction.atom.id}
        else:
            return set()
    elif isinstance(instruction, ReturnInstruction):
        return {instruction.atom.id}
        

def get_kill(instruction: Instruction):
    # Iterate over types of instruction
    if isinstance(instruction, InstructionLabel):
        return set()
    elif isinstance(instruction, AssignmentAtomInstruction):
        return {instruction.dest.id}
    elif isinstance(instruction, AssignmentBinopInstruction):
        return {instruction.dst.id}
    elif isinstance(instruction, AssignmentFromMemInstruction):
        return {instruction.dst.id}
    elif isinstance(instruction, AssignmentToMemInstruction):
        return set()
    elif isinstance(instruction, GotoInstruction):
        return set()
    elif isinstance(instruction, IfInstruction):
        if isinstance(instruction.atom, AtomId):
            return {instruction.atom.id}
        return set()
    elif isinstance(instruction, ReturnInstruction):
        if isinstance(instruction.atom, AtomId):
            return {instruction.atom.id}
        return set()


def _in(gen: set, out: set, kill: set):
    # gen[i] U (out[i] \ kill[i])
    return gen.union(out.difference(kill))

def _out(succ: list, _in: set):
    # U_{j in succ[i]} in[j]
    return set.union(*[succ[i] for i in _in])

def liveness_analysis(program: Program):
    # Successors, indexed by instruction index. These are the instructions that can be reached from the current instruction.
    succ = []

    # List of instructions that may be read from the current instruction
    # eg., gen[i] = {x} means that x is read from instruction i
    gen = []

    # A set that lists that may be written to by the current instruction
    # eg., kill[i] = set(x,y) means that x and y are written to by instruction i
    kill = []

    # _in[i] holds the variables that are live at the start of i
    _in = []

    # out[i] holds the variables that are live at the end of i
    out = []

    # Iterate
    prev_in = []
    prev_out = []
    for i, instruction in reversed(list(enumerate(program.instructions))):

        out = _out(succ, _in)
        _in = _in(gen, out, kill)


