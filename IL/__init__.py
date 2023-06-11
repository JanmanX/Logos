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
class InstructionLabel:
    id: str

    def __repr__(self) -> str:
        return f'{self.id}:'

@dataclass
class AssignmentAtomInstruction:
    id: str
    atom: AtomId | AtomNum

    def __repr__(self) -> str:
        return f'{self.id} = {self.atom}'

@dataclass
class AssignmentBinopInstruction:
    id: str
    op: Binop 
    atom1: AtomId | AtomNum
    atom2: AtomId | AtomNum

    def __repr__(self) -> str:
        return f'{self.id} = {self.atom1} {self.op.value} {self.atom2}'
 
@dataclass
class AssignmentFromMemInstruction:
    id: str
    atom: AtomId | AtomNum

@dataclass
class AssignmentToMemInstruction:
    id: str
    atom: AtomId | AtomNum

@dataclass
class GotoInstruction:
    id: str

@dataclass
class IfInstruction:
    atom: AtomId | AtomNum
    trueGotoLabel: str
    falseGotoLabel: str

    def __repr__(self) -> str:
        return f'if {self.atom} goto {self.trueGotoLabel} else goto {self.falseGotoLabel}'

@dataclass
class FunctionCallInstruction:
    id: str
    function: str
    args: list

@dataclass
class ReturnInstruction:
    id: str


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

