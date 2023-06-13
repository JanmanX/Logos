import random

from generated.LogosVisitor import LogosVisitor 
from generated.LogosParser import LogosParser
from . import *

class ILGenerator(LogosVisitor):
    def newvar(self):
        name = 't' + str(self._newvar_index)
        self._newvar_index += 1
        return name
    
    def newlabel(self):
        name = 'l' + str(self._newlabel_index)
        self._newlabel_index += 1
        return name

    def bind(self, table, name, place):
        table[name] = place

    def visitProg(self, ctx:LogosParser.ProgContext) -> Program:
        self.program = Program([])
        self.vtable = dict()
        self.ftable = dict()
        self.place = None
        self.label = None 

        # internals
        self._newvar_index = 0
        self._newlabel_index = 0

        code = []
        for child in ctx.children:
            _code = self.visit(child)
            if _code:
                code += _code

        self.program.instructions = code

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
        code = self.visit(ctx.expr())

        # Add assignment instruction
        return code + [AssignmentAtomInstruction(AtomId(x), AtomId(self.place))]


    # Visit a parse tree produced by LogosParser#MulDiv.
    def visitMulDiv(self, ctx:LogosParser.MulDivContext):
        place0 = self.place

        # Visit left
        place1 = self.newvar()
        self.place = place1
        code1 = self.visit(ctx.expr(0))

        # Visit right
        place2 = self.newvar()
        self.place = place2
        code2 = self.visit(ctx.expr(1))

        # Add instruction
        op = Binop.MUL if ctx.op.type == LogosParser.OP_MUL else Binop.DIV
        code = code1 + code2 + [AssignmentBinopInstruction(AtomId(place0), op, AtomId(place1), AtomId(place2))]
        return code


    # Visit a parse tree produced by LogosParser#AddSub.
    def visitAddSub(self, ctx:LogosParser.AddSubContext):
        place0 = self.place

        # Visit left
        place1 = self.newvar()
        self.place = place1
        code1 = self.visit(ctx.expr(0))

        # Visit right
        place2 = self.newvar()
        self.place = place2
        code2 = self.visit(ctx.expr(1))

        # Add instruction
        op = Binop.ADD if ctx.op.type == LogosParser.OP_ADD else Binop.SUB
        code = code1 + code2 + [AssignmentBinopInstruction(AtomId(place0), op, AtomId(place1), AtomId(place2))]
        return code


    # Visit a parse tree produced by LogosParser#LeLeqGeGeq.
    def visitLeLeqGeGeq(self, ctx:LogosParser.LeLeqGeGeqContext):


        return self.visitChildren(ctx)

    # Visit a parse tree produced by LogosParser#EqNeq.
    def visitEqNeq(self, ctx:LogosParser.EqNeqContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LogosParser#LogicalAndOr.
    def visitLogicalAndOr(self, ctx:LogosParser.LogicalAndOrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LogosParser#AndXorOr.
    def visitAndXorOr(self, ctx:LogosParser.AndXorOrContext):
        return self.visitChildren(ctx)



    # Visit a parse tree produced by LogosParser#Int.
    def visitInt(self, ctx:LogosParser.IntContext):
        return [AssignmentAtomInstruction(AtomId(self.place), AtomNum(ctx.INT().getText()))]


    # Visit a parse tree produced by LogosParser#Id.
    def visitId(self, ctx:LogosParser.IdContext):
        id = ctx.ID().getText()
        x = self.vtable[id]

        return [AssignmentAtomInstruction(AtomId(self.place), AtomId(x))]


    # Visit a parse tree produced by LogosParser#if.
    def visitIf(self, ctx:LogosParser.IfContext):
        label1 = self.newlabel()
        label2 = self.newlabel()

        # Visit condition
        place1 = self.newvar()
        self.place = place1
        code0 = self.visit(ctx.expr())

        # Visit stmt
        code1 = self.visit(ctx.stmt())

        return code0 + \
            [IfInstruction(AtomId(place1), AtomId(label1), AtomId(label2)), InstructionLabel(label1)]  \
            + code1  \
            + [InstructionLabel(label2)]

    # Visit a parse tree produced by LogosParser#while.
    def visitWhile(self, ctx:LogosParser.WhileContext):
        label1 = self.newlabel()
        label2 = self.newlabel()
        label3 = self.newlabel()

        # Visit condition
        place1 = self.newvar()
        self.place = place1
        code0 = self.visit(ctx.expr())

        # Visit stmt
        code1 = self.visit(ctx.stmt())

        return [InstructionLabel(label1)] \
            + code0 \
            + [IfInstruction(AtomId(place1), AtomId(label2), AtomId(label3)), InstructionLabel(label2)] \
            + code1 \
            + [GotoInstruction(AtomId(label1)), InstructionLabel(label3)]


