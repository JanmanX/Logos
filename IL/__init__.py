from dataclasses import dataclass
from enum import Enum

# --- Operators
class Binop(Enum):
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'
    MOD = '%'

class Relop(Enum):
    EQ = '=='
    NE = '!='
    LT = '<'
    LE = '<='
    GT = '>'
    GE = '>='

# --- Atoms
@dataclass
class AtomId:
    id: str

    def __repr__(self) -> str:
        return self.id


@dataclass
class AtomNum:
    num: int

    def __repr__(self) -> str:
        return str(self.num)

# --- Instructions
@dataclass
class Instruction:
    pass


@dataclass
class InstructionLabel(Instruction):
    label_id: str

    def __repr__(self) -> str:
        return f'{self.label_id}:'

@dataclass
class AssignmentAtomInstruction(Instruction):
    dest: AtomId
    src: AtomId | AtomNum

    def __repr__(self) -> str:
        return f'{self.dest} = {self.src}'

@dataclass
class AssignmentBinopInstruction(Instruction):
    dst: AtomId
    op: Binop 
    left: AtomId | AtomNum
    right: AtomId | AtomNum

    def __repr__(self) -> str:
        return f'{self.dst} = {self.left} {self.op.value} {self.right}'
 
@dataclass
class AssignmentFromMemInstruction(Instruction):
    dst: AtomId
    atom: AtomId | AtomNum

@dataclass
class AssignmentToMemInstruction(Instruction):
    mem: AtomId
    atom: AtomId | AtomNum

@dataclass
class GotoInstruction(Instruction):
    label_id: AtomId

@dataclass
class IfInstruction(Instruction):
    atom: AtomId | AtomNum
    true_label: AtomId
    false_label: AtomId

    def __repr__(self) -> str:
        return f'if {self.atom} goto {self.true_label} else goto {self.false_label}'

@dataclass
class FunctionCallInstruction(Instruction):
    dst: AtomId
    function: AtomId
    args: list

@dataclass
class ReturnInstruction(Instruction):
    atom: AtomId | AtomNum


# --- Other
@dataclass
class Function:
    header: str
    body: list

@dataclass
class Program:
    instructions: list

    def __repr__(self) -> str:
        return '\n'.join([str(i) for i in self.instructions])

