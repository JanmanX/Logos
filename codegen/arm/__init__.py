from IL import Binop, Program, InstructionLabel, InstructionAssign, InstructionAssignBinop, InstructionAssignFromMem, \
    InstructionAssignToMem, InstructionGoto, InstructionIf, InstructionFunctionCall, InstructionReturn, AtomId

REGISTER_MAP = {
    't0': 'X0',
    't1': 'X1',
    't2': 'X2',
    't3': 'X3',
    't4': 'X4',
    't5': 'X5',
    't6': 'X6',
    't7': 'X7',
    't8': 'X8',
    't9': 'X9',
    't10': 'X10',
    't11': 'X11',
    't12': 'X12',
    't13': 'X13',
    't14': 'X14',
    't15': 'X15',
    't16': 'X16',
    't17': 'X17',
    't18': 'X18',
    't19': 'X19',
    't20': 'X20',
    't21': 'X21',
    't22': 'X22',
    't23': 'X23',
    't24': 'X24',
    't25': 'X25',
    't26': 'X26',
    't27': 'X27',
    't28': 'X28',
    't29': 'X29',
    't30': 'X30',
    't31': 'X31',
}


def codegen_binop(instruction: InstructionAssignBinop):
    code = []
    if instruction.op == Binop.ADD:
        if isinstance(instruction.left, AtomId):
            code.append(f'MOV {REGISTER_MAP[instruction.dest.id]}, {REGISTER_MAP[instruction.left.id]}')
        else:
            code.append(f'MOV {REGISTER_MAP[instruction.dest.id]}, #{instruction.left.num}')

        if isinstance(instruction.right, AtomId):
            code.append(f'ADD {REGISTER_MAP[instruction.dest.id]}, {REGISTER_MAP[instruction.dest.id]}, {REGISTER_MAP[instruction.right.id]}')
        else:
            code.append(f'ADD {REGISTER_MAP[instruction.dest.id]}, {REGISTER_MAP[instruction.dest.id]}, #{instruction.right.num}')

    elif instruction.op == Binop.SUB:
        if isinstance(instruction.left, AtomId):
            code.append(f'MOV {REGISTER_MAP[instruction.dest.id]}, {REGISTER_MAP[instruction.left.id]}')
        else:
            code.append(f'MOV {REGISTER_MAP[instruction.dest.id]}, #{instruction.left.num}')

        if isinstance(instruction.right, AtomId):
            code.append(f'SUB {REGISTER_MAP[instruction.dest.id]}, {REGISTER_MAP[instruction.dest.id]}, {REGISTER_MAP[instruction.right.id]}')
        else:
            code.append(f'SUB {REGISTER_MAP[instruction.dest.id]}, {REGISTER_MAP[instruction.dest.id]}, #{instruction.right.num}')

    else:
        raise NotImplemented

    return code


def codegen(program: Program) -> str:
    prolog = [
        '.text',
        '.global _start',
        '_start:',
    ]
    epilog = []
    code = []

    for instruction in program.instructions:
        if isinstance(instruction, InstructionLabel):
            raise NotImplemented
        elif isinstance(instruction, InstructionAssign):
            if isinstance(instruction.src, AtomId):
                code.append(f'MOV {REGISTER_MAP[instruction.dest.id]}, {REGISTER_MAP[instruction.src.id]}')
            else:
                code.append(f'MOV {REGISTER_MAP[instruction.dest.id]}, #{instruction.src.num}')
        elif isinstance(instruction, InstructionAssignBinop):
            code.extend(codegen_binop(instruction))
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
            code.append('RET')
        #    code.append(f'RET {REGISTER_MAP[instruction.atom.id]}')
        else:
            raise Exception("Unknown instruction")

    code = prolog + code + epilog
    return '\n'.join(code) + '\n'
