# Generated from Logos.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LogosParser import LogosParser
else:
    from LogosParser import LogosParser

# This class defines a complete listener for a parse tree produced by LogosParser.
class LogosListener(ParseTreeListener):

    # Enter a parse tree produced by LogosParser#prog.
    def enterProg(self, ctx:LogosParser.ProgContext):
        pass

    # Exit a parse tree produced by LogosParser#prog.
    def exitProg(self, ctx:LogosParser.ProgContext):
        pass


    # Enter a parse tree produced by LogosParser#assign.
    def enterAssign(self, ctx:LogosParser.AssignContext):
        pass

    # Exit a parse tree produced by LogosParser#assign.
    def exitAssign(self, ctx:LogosParser.AssignContext):
        pass


    # Enter a parse tree produced by LogosParser#assignMem.
    def enterAssignMem(self, ctx:LogosParser.AssignMemContext):
        pass

    # Exit a parse tree produced by LogosParser#assignMem.
    def exitAssignMem(self, ctx:LogosParser.AssignMemContext):
        pass


    # Enter a parse tree produced by LogosParser#print.
    def enterPrint(self, ctx:LogosParser.PrintContext):
        pass

    # Exit a parse tree produced by LogosParser#print.
    def exitPrint(self, ctx:LogosParser.PrintContext):
        pass


    # Enter a parse tree produced by LogosParser#if.
    def enterIf(self, ctx:LogosParser.IfContext):
        pass

    # Exit a parse tree produced by LogosParser#if.
    def exitIf(self, ctx:LogosParser.IfContext):
        pass


    # Enter a parse tree produced by LogosParser#while.
    def enterWhile(self, ctx:LogosParser.WhileContext):
        pass

    # Exit a parse tree produced by LogosParser#while.
    def exitWhile(self, ctx:LogosParser.WhileContext):
        pass


    # Enter a parse tree produced by LogosParser#exit.
    def enterExit(self, ctx:LogosParser.ExitContext):
        pass

    # Exit a parse tree produced by LogosParser#exit.
    def exitExit(self, ctx:LogosParser.ExitContext):
        pass


    # Enter a parse tree produced by LogosParser#LeLeqGeGeq.
    def enterLeLeqGeGeq(self, ctx:LogosParser.LeLeqGeGeqContext):
        pass

    # Exit a parse tree produced by LogosParser#LeLeqGeGeq.
    def exitLeLeqGeGeq(self, ctx:LogosParser.LeLeqGeGeqContext):
        pass


    # Enter a parse tree produced by LogosParser#MulDiv.
    def enterMulDiv(self, ctx:LogosParser.MulDivContext):
        pass

    # Exit a parse tree produced by LogosParser#MulDiv.
    def exitMulDiv(self, ctx:LogosParser.MulDivContext):
        pass


    # Enter a parse tree produced by LogosParser#AddSub.
    def enterAddSub(self, ctx:LogosParser.AddSubContext):
        pass

    # Exit a parse tree produced by LogosParser#AddSub.
    def exitAddSub(self, ctx:LogosParser.AddSubContext):
        pass


    # Enter a parse tree produced by LogosParser#LogicalAndOr.
    def enterLogicalAndOr(self, ctx:LogosParser.LogicalAndOrContext):
        pass

    # Exit a parse tree produced by LogosParser#LogicalAndOr.
    def exitLogicalAndOr(self, ctx:LogosParser.LogicalAndOrContext):
        pass


    # Enter a parse tree produced by LogosParser#Id.
    def enterId(self, ctx:LogosParser.IdContext):
        pass

    # Exit a parse tree produced by LogosParser#Id.
    def exitId(self, ctx:LogosParser.IdContext):
        pass


    # Enter a parse tree produced by LogosParser#AndXorOr.
    def enterAndXorOr(self, ctx:LogosParser.AndXorOrContext):
        pass

    # Exit a parse tree produced by LogosParser#AndXorOr.
    def exitAndXorOr(self, ctx:LogosParser.AndXorOrContext):
        pass


    # Enter a parse tree produced by LogosParser#Int.
    def enterInt(self, ctx:LogosParser.IntContext):
        pass

    # Exit a parse tree produced by LogosParser#Int.
    def exitInt(self, ctx:LogosParser.IntContext):
        pass


    # Enter a parse tree produced by LogosParser#EqNeq.
    def enterEqNeq(self, ctx:LogosParser.EqNeqContext):
        pass

    # Exit a parse tree produced by LogosParser#EqNeq.
    def exitEqNeq(self, ctx:LogosParser.EqNeqContext):
        pass



del LogosParser