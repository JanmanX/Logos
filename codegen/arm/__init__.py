from IL import AtomNum, Binop, Program, InstructionLabel, InstructionAssign, InstructionAssignBinop, InstructionReadMem, \
    InstructionWriteMem, InstructionGoto, InstructionIf, InstructionFunctionCall, InstructionReturn, AtomId, \
    InstructionAllocMem, Ritual, StackEntry
from utils.math import round_up

BINOP_INSTRUCTION_MAP = {
    Binop.ADD: 'add',
    Binop.SUB: 'sub',
    Binop.MUL: 'mul',
    Binop.DIV: 'sdiv',
}

# TODO: https://developer.apple.com/documentation/xcode/writing-arm64-code-for-apple-platforms
# Dont use register X18 (x18) for anything other than the platform's Thread Local Storage (TLS) pointer.

AVAILABLE_REGISTERS = {
    0: 'x9',
    1: 'x10',
    2: 'x11',
    3: 'x12',
    4: 'x13',
    5: 'x14',
    6: 'x15',
}

def assign_registers(variable_register_map: list[str]) -> dict:
    # Real registers
    real_registers_map = {}

    for variable in variable_register_map:
        print(variable)
        real_registers_map[variable] = AVAILABLE_REGISTERS[variable_register_map[variable]]


    return real_registers_map


def codegen_binop(instruction: InstructionAssignBinop, register_map: dict):
    code = []
    op_instruction = BINOP_INSTRUCTION_MAP[instruction.op]

    code.append(
        f'{op_instruction} {register_map[instruction.dest.id]}, {register_map[instruction.left.id]}, {register_map[instruction.right.id]}')

    return code


def codegen_assign(instruction: InstructionAssign, register_map: dict):
    code = []
    if isinstance(instruction.src, AtomId):
        code.append(f'mov {register_map[instruction.dest.id]}, {register_map[instruction.src.id]}')
    else:
        code.append(f'mov {register_map[instruction.dest.id]}, #{instruction.src.num}')
    return code


def codegen_label(instruction: InstructionLabel):
    code = [f'{instruction.label_id.id}:']
    return code


def codegen_read_mem(instruction: InstructionReadMem, register_map: dict, stack_size: int):
    code = []

    # If we are reading from a memory address
    if isinstance(instruction.addr, AtomId):
        code = [
            f'ldr {register_map[instruction.dest.id]}, [{register_map[instruction.addr.id]}]'
        ]
    # If we are reading from stack offset
    elif isinstance(instruction.addr, AtomNum):
        # Remember that the stack grows downwards, so take that into account
        stack_offset = stack_size - (instruction.addr.num + 8)
        code = [
            f'ldr {register_map[instruction.dest.id]}, [sp, #{stack_offset}]'
        ]

    return code


def codegen_write_mem(instruction: InstructionWriteMem, register_map: dict, stack_size: int):
    # ST{U}R    rt, [addr]      [addr] = rt
    code = []

    # If we are writing to a memory address
    if isinstance(instruction.addr, AtomId):
        code = [
            f'str {register_map[instruction.src.id]}, [{register_map[instruction.addr.id]}]'
        ]
    # If we are writing to a stack offset
    elif isinstance(instruction.addr, AtomNum):
        # Remember that the stack grows downwards, so take that into account
        stack_offset = stack_size - (instruction.addr.num + 8)
        code = [
            f'str {register_map[instruction.src.id]}, [sp, #{stack_offset}]'
        ]

    return code


def codegen_goto(instruction: InstructionGoto):
    code = [
        f'b {instruction.label_id.id}'
    ]
    return code


def codegen_if(instruction: InstructionIf, register_map: dict):
    code = [
        f'cmp {register_map[instruction.atom.id]}, #0',
        f'beq {instruction.false_label.id}',
        f'bne {instruction.true_label.id}'
    ]

    return code


def codegen_function_call(instruction: InstructionFunctionCall):
    raise NotImplemented


def codegen_return(instruction: InstructionReturn, register_map: dict):
    return []


def codegen_alloc_mem(instruction: InstructionAllocMem, register_map: dict, stack_size: int):
    # Pseudo instruction
    # dest = SP - (stack_offset + offset)

    stack_offset = stack_size - instruction.offset 
    code = [
        f'sub {register_map[instruction.dest.id]}, sp, #{stack_offset}'
    ]
    return code


def codegen_ritual(ritual: Ritual):
    register_map = assign_registers(ritual.variable_register_map)

    code = []

    # Align the stack to 16 bytes
    ritual.stack_size = round_up(ritual.stack_size, 16)
    code.extend([
        f"sub sp, sp, #{ritual.stack_size}"
    ])

    for instruction in ritual.instructions:
        if isinstance(instruction, InstructionLabel):
            code.extend(codegen_label(instruction))
        elif isinstance(instruction, InstructionAssign):
            code.extend(codegen_assign(instruction, register_map))
        elif isinstance(instruction, InstructionAllocMem):
            code.extend(codegen_alloc_mem(instruction, register_map, ritual.stack_size))
        elif isinstance(instruction, InstructionAssignBinop):
            code.extend(codegen_binop(instruction, register_map))
        elif isinstance(instruction, InstructionReadMem):
            code.extend(codegen_read_mem(instruction, register_map, ritual.stack_size))
        elif isinstance(instruction, InstructionWriteMem):
            code.extend(codegen_write_mem(instruction, register_map, ritual.stack_size))
        elif isinstance(instruction, InstructionGoto):
            code.extend(codegen_goto(instruction, register_map))
        elif isinstance(instruction, InstructionIf):
            code.extend(codegen_if(instruction, register_map))
        elif isinstance(instruction, InstructionFunctionCall):
            code.extend(codegen_function_call(instruction, register_map))
        elif isinstance(instruction, InstructionReturn):
            code.extend(codegen_return(instruction, register_map))
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
mov     X16, #1  // System call number 1 terminates this program
svc     #0x80  // Call kernel to terminate the program
    """.splitlines()

    code = []

    for ritual in program.rituals:
        code.extend(codegen_ritual(ritual))

    # Just a nice formatting
    code = [f'    {line}' for line in code]

    code = prolog + code + epilog
    return '\n'.join(code) + '\n'
