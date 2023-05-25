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


    # Enter a parse tree produced by LogosParser#stmt.
    def enterStmt(self, ctx:LogosParser.StmtContext):
        pass

    # Exit a parse tree produced by LogosParser#stmt.
    def exitStmt(self, ctx:LogosParser.StmtContext):
        pass


    # Enter a parse tree produced by LogosParser#expr.
    def enterExpr(self, ctx:LogosParser.ExprContext):
        pass

    # Exit a parse tree produced by LogosParser#expr.
    def exitExpr(self, ctx:LogosParser.ExprContext):
        pass



del LogosParser