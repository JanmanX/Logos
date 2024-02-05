from IL import Binop, Program, InstructionLabel, InstructionAssign, InstructionAssignBinop, InstructionAssignFromMem, \
    InstructionAssignToMem, InstructionGoto, InstructionIf, InstructionFunctionCall, InstructionReturn, AtomId, \
    InstructionAllocMem, Ritual, StackEntry
from utils.math import round_up

BINOP_INSTRUCTION_MAP = {
    Binop.ADD: 'ADD',
    Binop.SUB: 'SUB',
    Binop.MUL: 'MUL',
    Binop.DIV: 'SDIV',
}

# TODO: https://developer.apple.com/documentation/xcode/writing-arm64-code-for-apple-platforms
# Dont use register X18 (x18) for anything other than the platform's Thread Local Storage (TLS) pointer.

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
    op_instruction = BINOP_INSTRUCTION_MAP[instruction.op]

    code.append(
        f'{op_instruction} {REGISTER_MAP[instruction.dest.id]}, {REGISTER_MAP[instruction.left.id]}, {REGISTER_MAP[instruction.right.id]}')

    return code


def codegen_assign(instruction: InstructionAssign):
    code = []
    if isinstance(instruction.src, AtomId):
        code.append(f'MOV {REGISTER_MAP[instruction.dest.id]}, {REGISTER_MAP[instruction.src.id]}')
    else:
        code.append(f'MOV {REGISTER_MAP[instruction.dest.id]}, #{instruction.src.num}')
    return code


def codegen_label(instruction: InstructionLabel):
    code = [f'{instruction.label_id.id}:']
    return code


def codegen_assign_from_mem(instruction: InstructionAssignFromMem):
    code = [
        f'LDR {REGISTER_MAP[instruction.dest.id]}, [{REGISTER_MAP[instruction.src.id]}]'
    ]
    return code


def codegen_assign_to_mem(instruction: InstructionAssignToMem):
    code = [
        f'STR {REGISTER_MAP[instruction.src.id]}, [{REGISTER_MAP[instruction.addr.id]}]'
    ]
    return code


def codegen_goto(instruction: InstructionGoto):
    code = [
        f'B {instruction.label_id.id}'
    ]
    return code


def codegen_if(instruction: InstructionIf):
    code = [
        f'CMP {REGISTER_MAP[instruction.atom.id]}, #0',
        f'BEQ {instruction.false_label.id}',
        f'BNE {instruction.true_label.id}'
    ]

    return code


def codegen_function_call(instruction: InstructionFunctionCall):
    raise NotImplemented


def codegen_return(instruction: InstructionReturn):
    return []
#    return ['RET']

def codegen_alloc_stack(stack_entries: list[StackEntry]):
    return []


def codegen_alloc_stack(instructions: list):
    # Every instruction that allocates memory on the stack,
    # calculate the total size and allign to 16 bytes
    stack_size = sum([x.size for x in instructions if isinstance(x, InstructionAllocMem)]) 
    stack_size = round_up(stack_size, 16)

    return instructions

def codegen_ritual(ritual: Ritual):
    code = []

    # Calculate stack size and allign to 16 bytes
    stack_size = sum([x.size for x in ritual.instructions if isinstance(x, InstructionAllocMem)])
    stack_size = round_up(stack_size, 16)

    # Prolog
    code.extend([
        f'SUB SP, SP, #{stack_size}',
    ])

    for instruction in ritual.instructions:
        if isinstance(instruction, InstructionLabel):
            code.extend(codegen_label(instruction))
        elif isinstance(instruction, InstructionAssign):
            code.extend(codegen_assign(instruction))
        elif isinstance(instruction, InstructionAllocMem):
            code.extend(codegen_alloc_stack(instruction))
        elif isinstance(instruction, InstructionAssignBinop):
            code.extend(codegen_binop(instruction))
        elif isinstance(instruction, InstructionAssignFromMem):
            code.extend(codegen_assign_from_mem(instruction))
        elif isinstance(instruction, InstructionAssignToMem):
            code.extend(codegen_assign_to_mem(instruction))
        elif isinstance(instruction, InstructionGoto):
            code.extend(codegen_goto(instruction))
        elif isinstance(instruction, InstructionIf):
            code.extend(codegen_if(instruction))
        elif isinstance(instruction, InstructionFunctionCall):
            code.extend(codegen_function_call(instruction))
        elif isinstance(instruction, InstructionReturn):
            code.extend(codegen_return(instruction))
        else:
            raise Exception("Unknown instruction")

    return code

def codegen(program: Program) -> str:
    prolog = [
        '.text',
        '.global _main',
        '_main:',
    ]

    epilog = """
        MOV     X16, #1  // System call number 1 terminates this program
        SVC     #0x80  // Call kernel to terminate the program
    """.splitlines()

    code = []

    for ritual in program.rituals:
        code.extend(codegen_ritual(ritual))

    code = prolog + code + epilog
    return '\n'.join(code) + '\n'
