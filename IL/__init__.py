from dataclasses import dataclass

# --- Atoms
@dataclass
class AtomId:
    id: str

@dataclass
class AtomNum:
    num: int


# --- Instructions
@dataclass
class InstructionLabel:
    id: str

@dataclass
class AssignmentInstruction:
    id: str
    atom: AtomId | AtomNum

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
    id: str
    op: str
    atom: AtomId | AtomNum
    trueGotoLabel: str
    falseGotoLabel: str

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
    functions: list

