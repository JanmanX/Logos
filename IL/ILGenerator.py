import random

from generated.LogosVisitor import LogosVisitor 
from generated.LogosParser import LogosParser
from . import *

class ILGenerator(LogosVisitor):
    def newvar(self, table: dict, id: str):
        # Find a unique name for the variable, store it in the
        # variable table, and return it.
        for x in range(10000):
            name = "t" + x 
            if name not in table.values():
                table[id] = name
                return name

    def getVtable(self):
        return self.vtables[-1]

    def pushVtable(self):
        self.vtables.append(self.vtables[-1].copy())

    def popVtable(self):
        self.vtables.pop()

    def getFtable(self):
        return self.ftables[-1]

    def pushFtable(self):
        self.ftables.append(self.ftables[-1].copy())

    def popFtable(self):
        self.ftables.pop()

    def getPlace(self):
        return self.places[-1]
    
    def pushPlace(self, place):
        self.places.append(place)

    def popPlace(self):
        return self.places.pop()

    def visitProg(self, ctx:LogosParser.ProgContext) -> Program:
        self.program = Program([])
        self.vtables = [dict()]
        self.ftables = [dict()]
        self.places = []

        self.visitChildren(ctx)

        return self.program

    def visitAssign(self, ctx:LogosParser.AssignContext):
        self.pushVtable()
        self.pushFtable()
        self.visitChildren(ctx)


    def visitAddSub(self, ctx:LogosParser.AddSubContext):
        # Left
        place1 = self.newvar(self.getVtable()) 
        self.pushPlace(place1)
        self.visit(ctx.left())

        # Right
        place2 = self.newvar(self.getVtable())
        self.pushPlace(place2)
        self.visit(ctx.right())

        # Cleanup
        self.popPlace()
        self.popPlace()


    # Visit a parse tree produced by LogosParser#Int.
    def visitInt(self, ctx:LogosParser.IntContext):
        print("visit place")
        place = self.getPlace()
        self.program.instructions.append(AssignmentAtomInstruction(place, AtomNum(ctx.INT().getText())))

    # Visit a parse tree produced by LogosParser#Id.
    def visitId(self, ctx:LogosParser.IdContext):
        place = self.getPlace()
        x = self.getVtable()[ctx.ID().getText()]
        self.program.instructions.append(AssignmentAtomInstruction(place, AtomId(x)))


