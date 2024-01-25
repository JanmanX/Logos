from dataclasses import dataclass
from enum import Enum
from .arm import codegen as codegen_arm


class Architecture(Enum):
    ARM = 1 # actually AArch64 / A64...
    X86_64 = 2


@dataclass
class TargetConfig:
    architecture: Architecture
    num_registers: int

    @staticmethod
    def from_architecture(architecture: Architecture):
        if architecture == Architecture.ARM:
            return TargetConfig(architecture, 32)
        elif architecture == Architecture.X86_64:
            raise NotImplemented
        else:
            raise Exception("Unknown architecture")


def codegen(program, config: TargetConfig):
    if config.architecture == Architecture.ARM:
        return codegen_arm(program)