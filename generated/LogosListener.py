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


    # Enter a parse tree produced by LogosParser#return.
    def enterReturn(self, ctx:LogosParser.ReturnContext):
        pass

    # Exit a parse tree produced by LogosParser#return.
    def exitReturn(self, ctx:LogosParser.ReturnContext):
        pass


    # Enter a parse tree produced by LogosParser#expr.
    def enterExpr(self, ctx:LogosParser.ExprContext):
        pass

    # Exit a parse tree produced by LogosParser#expr.
    def exitExpr(self, ctx:LogosParser.ExprContext):
        pass



del LogosParser