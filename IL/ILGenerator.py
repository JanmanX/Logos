import random

from generated import LogosVisitor, LogosParser
from . import *

class ILGenerator(LogosVisitor):
    def newvar(self, vtable: set):
        # Find a unique name for the variable, store it in the
        # variable table, and return it.
        for x in range(10000):
            name = "t" + x 
            if name not in vtable:
                vtable.add(name)
                return name

    def getVtable(self):
        return self.vtables[-1]

    def pushVtable(self):
        self.vtables.push(self.vtables[-1].copy())

    def popVtable(self):
        self.vtables.pop()

    def getFtable(self):
        return self.ftables[-1]

    def pushFtable(self):
        self.ftables.push(self.ftables[-1].copy())

    def popFtable(self):
        self.ftables.pop()

    def getPlace(self):
        return self.places[-1]
    
    def pushPlace(self, place):
        self.places.append(place)

    def popPlace(self):
        return self.places.pop()


    def visitProg(self, ctx:LogosParser.ProgContext) -> Program:
        self.program = Program()
        self.vtables = [set()]
        self.ftables = [set()]
        self.places = []

        self.visitChildren(ctx)

        return self.program

    def visitAssign(self, ctx:LogosParser.AssignContext):
        self.pushVtable()
        self.pushFtable()
       
        self.visitChildren(ctx)


    def visitAddSub(self, ctx:LogosParser.AddSubContext):
        place1 = self.newvar(self.getVtable()) 
        self.visit(ctx.left())

        place2 = self.newvar(self.getVtable())
        self.visit(ctx.right())

         

        return self.visitChildren(ctx)

    # Visit a parse tree produced by LogosParser#Int.
    def visitInt(self, ctx:LogosParser.IntContext):
        place = self.popPlace()
        self.program.instructions.append(AssignmentInstruction(place, AtomNum(ctx.INT().getText())))

    # Visit a parse tree produced by LogosParser#Id.
    def visitId(self, ctx:LogosParser.IdContext):
        place = self.popPlace()
        self.program.instructions.append(AssignmentInstruction(place, AtomId(ctx.ID().getText())))
