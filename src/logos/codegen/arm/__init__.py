from logos.IL import AtomNum, Binop, Program, InstructionLabel, InstructionAssign, InstructionAssignBinop, InstructionReadMem, \
    InstructionWriteMem, InstructionGoto, InstructionIf, InstructionFunctionCall, InstructionReturn, AtomId, \
    InstructionAllocMem, Ritual, StackEntry
from logos.utils.math import round_up

BINOP_INSTRUCTION_MAP = {
    Binop.ADD: 'add',
    Binop.SUB: 'sub',
    Binop.MUL: 'mul',
    Binop.DIV: 'sdiv',

    Binop.LT: 'LT',
    Binop.LEQ: 'LE',
    Binop.GT: 'GT',
    Binop.GEQ: 'GE',
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

    # Map argument registers to the ARM64 X0-X7 registers
    for i in range(8):
        name = f'arg_{i}'
        real_registers_map[name] = f'x{i}'


    for variable in variable_register_map:
        if variable in real_registers_map:
            continue
        real_registers_map[variable] = AVAILABLE_REGISTERS[variable_register_map[variable]]

    return real_registers_map


def codegen_binop(instruction: InstructionAssignBinop, register_map: dict):
    code = []
    op_instruction = BINOP_INSTRUCTION_MAP[instruction.op]

    # add / sub / mul / div
    if instruction.op in [Binop.ADD, Binop.SUB, Binop.MUL, Binop.DIV]: 
        code.append(
            f'{op_instruction} {register_map[instruction.dest.id]}, {register_map[instruction.left.id]}, {register_map[instruction.right.id]}')

    # lt / leq / gt / geq
    if instruction.op in [Binop.LT, Binop.LEQ, Binop.GT, Binop.GEQ]:
        # cmp left, right
        # cset dest, condition
        code.extend([
            f'cmp {register_map[instruction.left.id]}, {register_map[instruction.right.id]}',
            f'cset {register_map[instruction.dest.id]}, {op_instruction}'
        ])

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



def codegen_function_call(instruction: InstructionFunctionCall, register_map: dict):
    code = []

    # Move arguments to registers
    for i, arg in enumerate(instruction.args):
        if isinstance(arg, AtomId):
            code.append(f'mov x{i}, {register_map[arg.id]}')
        else:
            code.append(f'mov x{i}, #{arg.num}')

    # Dump registers x8 - x15 and x30 to the stack
    code.extend([
        f"sub sp, sp, #80", 
        f"str x8, [sp, #0]",
        f"str x9, [sp, #8]",
        f"str x10, [sp, #16]",
        f"str x11, [sp, #24]",
        f"str x12, [sp, #32]",
        f"str x13, [sp, #40]",
        f"str x14, [sp, #48]",
        f"str x15, [sp, #56]",
        f"str x30, [sp, #64]"
    ])

    code.extend([
        f'bl {instruction.ritual.id}'
    ])

    # Restore registers x8 - x15 from the stack
    code.extend([
        f"ldr x8, [sp, #0]",
        f"ldr x9, [sp, #8]",
        f"ldr x10, [sp, #16]",
        f"ldr x11, [sp, #24]",
        f"ldr x12, [sp, #32]",
        f"ldr x13, [sp, #40]",
        f"ldr x14, [sp, #48]",
        f"ldr x15, [sp, #56]",
        f"ldr x30, [sp, #64]",
        f"add sp, sp, #80"
    ])

    if instruction.dest:
        code.extend([
            f'mov {register_map[instruction.dest.id]}, x0'
        ])

    return code


def codegen_return(instruction: InstructionReturn, register_map: dict):
    code = []

    if instruction.atom:
        if isinstance(instruction.atom, AtomId):
            code.extend([
                f'mov x0, {register_map[instruction.atom.id]}'
            ])
        else:
            code.extend([
                f'mov x0, #{instruction.atom.num}'
            ])
    else:
        code.extend([
            f'mov x0, #0'
        ])

    
    return code + [
        f'ret'
    ]


def codegen_alloc_mem(instruction: InstructionAllocMem, register_map: dict, stack_size: int):
    # Pseudo instruction
    stack_offset = instruction.offset 
    code = [
        f'sub {register_map[instruction.dest.id]}, sp, #{stack_offset}'
    ]
    return code


def codegen_ritual(ritual: Ritual, add_annotations=False):
    register_map = assign_registers(ritual.variable_register_map)

    code = []

    # Add ritual label
    code.extend(codegen_label(InstructionLabel(ritual.name)))

    # Align the stack to 16 bytes
    ritual.stack_size = round_up(ritual.stack_size, 16)
    code.extend([
        f"sub sp, sp, #{ritual.stack_size}"
    ])

    for instruction in ritual.instructions:
        if add_annotations:
            # Add annotations to code
            code.append(f"/* {instruction} */")

        if isinstance(instruction, InstructionLabel):
            if instruction.label_id.id != ritual.name.id:
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
            code.extend(codegen_goto(instruction))
        elif isinstance(instruction, InstructionIf):
            code.extend(codegen_if(instruction, register_map))
        elif isinstance(instruction, InstructionFunctionCall):
            code.extend(codegen_function_call(instruction, register_map))
        elif isinstance(instruction, InstructionReturn):
            code.extend(codegen_return(instruction, register_map))
        else:
            raise Exception(f"Unknown instruction: {type(instruction)}: {instruction}")

    return code

def codegen(program: Program) -> str:
    prolog = [
        '.text',
        '.global _start',
        '_start:',
        'bl main',
        'mov x8, #0x5d',
        'svc #0'
    ]

    code = []

    for ritual in program.rituals:
        code.extend(codegen_ritual(ritual))

    # Add spaces in front of each line if it is not a label
    for i in range(len(code)):
        if not code[i].endswith(':'):
            code[i] = '    ' + code[i]

    code = prolog + code
    return '\n'.join(code) + '\n'
