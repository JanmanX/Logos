from IL import Program, InstructionLabel, InstructionAssign, InstructionAssignBinop, InstructionAssignFromMem, \
    InstructionAssignToMem, InstructionGoto, InstructionIf, InstructionFunctionCall, InstructionReturn, AtomId

REGISTER_MAP = {
    't0': 'R0',
    't1': 'R1',
    't2': 'R2',
    't3': 'R3',
    't4': 'R4',
    't5': 'R5',
    't6': 'R6',
    't7': 'R7',
    't8': 'R8',
    't9': 'R9',
    't10': 'R10',
    't11': 'R11',
    't12': 'R12',
}


def codegen(program: Program):
    epilog = '\n'.join([
        '.global _start',
        '_start:',
    ])
    prolog = '\n'.join([
    ])
    code = []

    for instruction in program.instructions:
        if isinstance(instruction, InstructionLabel):
            raise NotImplemented
        elif isinstance(instruction, InstructionAssign):
            if isinstance(instruction.src, AtomId):
                code.append(f'MOV {REGISTER_MAP[instruction.dest.id]}, {REGISTER_MAP[instruction.src.id]}')
            else:
                code.append(f'MOV {instruction.dest.id}, #{instruction.src.num}')
        elif isinstance(instruction, InstructionAssignBinop):
            code.append("TODO")
        elif isinstance(instruction, InstructionAssignFromMem):
            raise NotImplemented
        elif isinstance(instruction, InstructionAssignToMem):
            raise NotImplemented
        elif isinstance(instruction, InstructionGoto):
            raise NotImplemented
        elif isinstance(instruction, InstructionIf):
            raise NotImplemented
        elif isinstance(instruction, InstructionFunctionCall):
            raise NotImplemented
        elif isinstance(instruction, InstructionReturn):
            code.append("TODO")
        else:
            raise Exception("Unknown instruction")

        code.append(str(instruction))

    return code
