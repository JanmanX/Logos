# Generated from Logos.g4 by ANTLR 4.13.1
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


    # Enter a parse tree produced by LogosParser#ritual.
    def enterRitual(self, ctx:LogosParser.RitualContext):
        pass

    # Exit a parse tree produced by LogosParser#ritual.
    def exitRitual(self, ctx:LogosParser.RitualContext):
        pass


    # Enter a parse tree produced by LogosParser#assign.
    def enterAssign(self, ctx:LogosParser.AssignContext):
        pass

    # Exit a parse tree produced by LogosParser#assign.
    def exitAssign(self, ctx:LogosParser.AssignContext):
        pass


    # Enter a parse tree produced by LogosParser#allocMem.
    def enterAllocMem(self, ctx:LogosParser.AllocMemContext):
        pass

    # Exit a parse tree produced by LogosParser#allocMem.
    def exitAllocMem(self, ctx:LogosParser.AllocMemContext):
        pass


    # Enter a parse tree produced by LogosParser#writeMem.
    def enterWriteMem(self, ctx:LogosParser.WriteMemContext):
        pass

    # Exit a parse tree produced by LogosParser#writeMem.
    def exitWriteMem(self, ctx:LogosParser.WriteMemContext):
        pass


    # Enter a parse tree produced by LogosParser#readMem.
    def enterReadMem(self, ctx:LogosParser.ReadMemContext):
        pass

    # Exit a parse tree produced by LogosParser#readMem.
    def exitReadMem(self, ctx:LogosParser.ReadMemContext):
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


    # Enter a parse tree produced by LogosParser#return.
    def enterReturn(self, ctx:LogosParser.ReturnContext):
        pass

    # Exit a parse tree produced by LogosParser#return.
    def exitReturn(self, ctx:LogosParser.ReturnContext):
        pass


    # Enter a parse tree produced by LogosParser#ids.
    def enterIds(self, ctx:LogosParser.IdsContext):
        pass

    # Exit a parse tree produced by LogosParser#ids.
    def exitIds(self, ctx:LogosParser.IdsContext):
        pass


    # Enter a parse tree produced by LogosParser#exprs.
    def enterExprs(self, ctx:LogosParser.ExprsContext):
        pass

    # Exit a parse tree produced by LogosParser#exprs.
    def exitExprs(self, ctx:LogosParser.ExprsContext):
        pass


    # Enter a parse tree produced by LogosParser#call.
    def enterCall(self, ctx:LogosParser.CallContext):
        pass

    # Exit a parse tree produced by LogosParser#call.
    def exitCall(self, ctx:LogosParser.CallContext):
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


    # Enter a parse tree produced by LogosParser#LtLeqGtGeq.
    def enterLtLeqGtGeq(self, ctx:LogosParser.LtLeqGtGeqContext):
        pass

    # Exit a parse tree produced by LogosParser#LtLeqGtGeq.
    def exitLtLeqGtGeq(self, ctx:LogosParser.LtLeqGtGeqContext):
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