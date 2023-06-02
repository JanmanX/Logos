# Generated from Logos.g4 by ANTLR 4.13.0
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


    # Visit a parse tree produced by LogosParser#assign.
    def visitAssign(self, ctx:LogosParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#assignMem.
    def visitAssignMem(self, ctx:LogosParser.AssignMemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#print.
    def visitPrint(self, ctx:LogosParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#if.
    def visitIf(self, ctx:LogosParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#exit.
    def visitExit(self, ctx:LogosParser.ExitContext):
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



del LogosParser