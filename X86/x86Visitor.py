from antlr4 import ParseTreeVisitor

from . import consts
from generated.LogosParser import LogosParser
from generated.LogosVisitor import LogosVisitor 

class X86Visitor(LogosVisitor):

    def __init__(self) -> None:
        super().__init__()

        self.regs = {
            "r8": "",
            "r9": "",
            "r10": "",
            "r11": "",
            "r12": "",
            "r13": "",
            "r14": "",
            "r15": "",
        }

    def get_reg(self, id):
        # Check if the ID is already allocated
        for reg in self.regs:
            if self.regs[reg] == id:
                return reg

        # Allocate a register for the ID
        for reg in self.regs:
            if self.regs[reg] == "":
                self.regs[reg] = id
                return reg

        raise Exception("No registers available")

    # Visit a parse tree produced by LogosParser#prog.
    def visitProg(self, ctx:LogosParser.ProgContext):
        acc = ""
        for child in ctx.children:
            acc += self.visit(child)
        
        return acc


    # Visit a parse tree produced by LogosParser#assign.
    def visitAssign(self, ctx:LogosParser.AssignContext):


        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#assignMem.
    def visitAssignMem(self, ctx:LogosParser.AssignMemContext):
        return "assignMem"
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#print.
    def visitPrint(self, ctx:LogosParser.PrintContext):
        return "print"
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#if.
    def visitIf(self, ctx:LogosParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#exit.
    def visitExit(self, ctx:LogosParser.ExitContext):
        return "exit"
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#LeLeqGeGeq.
    def visitLeLeqGeGeq(self, ctx:LogosParser.LeLeqGeGeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#MulDiv.
    def visitMulDiv(self, ctx:LogosParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#AddSub.
    def visitAddSub(self, ctx:LogosParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#LogicalAndOr.
    def visitLogicalAndOr(self, ctx:LogosParser.LogicalAndOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#Id.
    def visitId(self, ctx:LogosParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#AndXorOr.
    def visitAndXorOr(self, ctx:LogosParser.AndXorOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#Int.
    def visitInt(self, ctx:LogosParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#EqNeq.
    def visitEqNeq(self, ctx:LogosParser.EqNeqContext):
        return self.visitChildren(ctx)


    def visitTerminal(self, ctx):
        # The `EOF` will now return this instead of `None`
        return ''
