import random

from generated.LogosVisitor import LogosVisitor 
from generated.LogosParser import LogosParser
from . import *

class ILGenerator(LogosVisitor):
    def newvar(self):
        name = 't' + str(self._newvar_index)
        self._newvar_index += 1
        return name

    def bind(self, table, name, place):
        table[name] = place

    def visitProg(self, ctx:LogosParser.ProgContext) -> Program:
        self.program = Program([])
        self.vtable = dict()
        self.ftable = dict()
        self.place = None
        self._newvar_index = 0

        self.visitChildren(ctx)

        return self.program


    def visitAssign(self, ctx:LogosParser.AssignContext):
        id = ctx.ID().getText()

        # If id not in vtable, add it
        if id not in self.vtable:
            x = self.newvar()
            self.bind(self.vtable, id, x)
        else:
            x = self.vtable[id]

        # Set place
        self.place = self.newvar()

        # Visit expression
        self.visit(ctx.expr())

        # Add assignment instruction
        self.program.instructions.append(AssignmentAtomInstruction(x, AtomId(self.place)))


    # Visit a parse tree produced by LogosParser#Int.
    def visitInt(self, ctx:LogosParser.IntContext):
        print("visit place")
        self.program.instructions.append(AssignmentAtomInstruction(self.place, AtomNum(ctx.INT().getText())))

