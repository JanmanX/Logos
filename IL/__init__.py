from dataclasses import dataclass
from enum import Enum


# --- Operators
class Binop(Enum):
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'
    MOD = '%'

    # Logical
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
    label_id: AtomId

    def __repr__(self) -> str:
        return f'{self.label_id}:'


@dataclass
class InstructionAssign(Instruction):
    dest: AtomId
    src: AtomId | AtomNum

    def __repr__(self) -> str:
        if isinstance(self.src, AtomId):
            return f'{self.dest} = Atom[{self.src}]'

        return f'{self.dest} = {self.src}'

@dataclass
class InstructionAllocMem(Instruction):
    dest: AtomId
    size: int

    def __repr__(self) -> str:
        return f'{self.dest} = ALLOC_MEM({self.size})'

@dataclass
class InstructionWriteMem(Instruction):
    dest: AtomId
    src: AtomId | AtomNum

    def __repr__(self) -> str:
        return f'MEM[{self.dest}] = {self.src}'

@dataclass
class InstructionReadMem(Instruction):
    dest: AtomId
    src: AtomId | AtomNum

    def __repr__(self) -> str:
        return f'{self.dest} = MEM[{self.src}]'

@dataclass
class InstructionAssignBinop(Instruction):
    dest: AtomId
    op: Binop
    left: AtomId
    right: AtomId

    def __repr__(self) -> str:
        return f'{self.dest} = {self.left} {self.op.value} {self.right}'


@dataclass
class InstructionAssignFromMem(Instruction):
    dest: AtomId
    addr: AtomId 

    def __repr__(self) -> str:
        return f'{self.dest} = MEM[{self.addr}]'


@dataclass
class InstructionAssignToMem(Instruction):
    dest: AtomId
    atom: AtomId 

    def __repr__(self) -> str:
        return f'MEM[{self.dest}] = {self.atom}'


@dataclass
class InstructionGoto(Instruction):
    label_id: AtomId


@dataclass
class InstructionIf(Instruction):
    atom: AtomId
    true_label: AtomId
    false_label: AtomId

    def __repr__(self) -> str:
        return f'if {self.atom} goto {self.true_label} else goto {self.false_label}'


@dataclass
class InstructionFunctionCall(Instruction):
    dest: AtomId
    function: AtomId
    args: list


@dataclass
class InstructionReturn(Instruction):
    atom: AtomId | AtomNum


# --- Data
@dataclass
class StackEntry:
    label: str
    value: str
    size: int

    def __repr__(self) -> str:
        return f'{self.label}: .{self.size} {self.value}'


# --- Other
@dataclass
class Ritual:
    id: AtomId
    args: list[AtomId]

    instructions: list
    variable_colors: dict
    vtable: dict

    # internals
    place = None
    label = None
    _newvar_index: int = 0
    _newlabel_index: int = 0

    def newvar(self):
        name = 't' + str(self._newvar_index)
        self._newvar_index += 1
        return name

    def newlabel(self):
        name = 'l' + str(self._newlabel_index)
        self._newlabel_index += 1
        return name

    def lookup(self, name):
        if name not in self.vtable:
            x = self.newvar()
            self.vtable[name] = x
        else:
            x = self.vtable[name]

        return x

    def __repr__(self) -> str:
        signature = f'{self.id} ({",".join([a.id for a in self.args])})\n'
        body = '  \n'.join([str(i) for i in self.instructions])
        return signature + body

@dataclass
class Program:
    rituals: list[Ritual]

    def __repr__(self) -> str:
        return '\n\n '.join([str(r) for r in self.rituals])
