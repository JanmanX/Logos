# Generated from Logos.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LogosParser import LogosParser
else:
    from LogosParser import LogosParser

# This class defines a complete generic visitor for a parse tree produced by LogosParser.

class LogosVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LogosParser#prog.
    def visitProg(self, ctx:LogosParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#ritual.
    def visitRitual(self, ctx:LogosParser.RitualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#assign.
    def visitAssign(self, ctx:LogosParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#allocMem.
    def visitAllocMem(self, ctx:LogosParser.AllocMemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#writeMem.
    def visitWriteMem(self, ctx:LogosParser.WriteMemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#readMem.
    def visitReadMem(self, ctx:LogosParser.ReadMemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#if.
    def visitIf(self, ctx:LogosParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#while.
    def visitWhile(self, ctx:LogosParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#return.
    def visitReturn(self, ctx:LogosParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#ids.
    def visitIds(self, ctx:LogosParser.IdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#exprs.
    def visitExprs(self, ctx:LogosParser.ExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#call.
    def visitCall(self, ctx:LogosParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#MulDiv.
    def visitMulDiv(self, ctx:LogosParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#AddSub.
    def visitAddSub(self, ctx:LogosParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#LtLeqGtGeq.
    def visitLtLeqGtGeq(self, ctx:LogosParser.LtLeqGtGeqContext):
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



del LogosParser