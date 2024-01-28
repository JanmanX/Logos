# Generated from Logos.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,30,74,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,44,8,1,1,2,1,2,1,2,3,2,49,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,69,8,2,10,2,12,
        2,72,9,2,1,2,0,1,4,3,0,2,4,0,6,1,0,18,19,1,0,16,17,1,0,22,25,1,0,
        20,21,1,0,26,28,1,0,29,30,85,0,7,1,0,0,0,2,43,1,0,0,0,4,48,1,0,0,
        0,6,8,3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,
        11,1,0,0,0,11,12,5,0,0,1,12,1,1,0,0,0,13,14,5,10,0,0,14,15,5,1,0,
        0,15,44,3,4,2,0,16,17,5,2,0,0,17,18,3,4,2,0,18,22,5,3,0,0,19,21,
        3,2,1,0,20,19,1,0,0,0,21,24,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,
        23,25,1,0,0,0,24,22,1,0,0,0,25,26,5,4,0,0,26,44,1,0,0,0,27,28,5,
        5,0,0,28,29,3,4,2,0,29,30,5,6,0,0,30,31,3,2,1,0,31,44,1,0,0,0,32,
        33,5,7,0,0,33,44,5,10,0,0,34,35,5,8,0,0,35,44,5,13,0,0,36,37,5,9,
        0,0,37,38,5,10,0,0,38,39,5,1,0,0,39,44,3,4,2,0,40,41,5,9,0,0,41,
        42,5,11,0,0,42,44,5,10,0,0,43,13,1,0,0,0,43,16,1,0,0,0,43,27,1,0,
        0,0,43,32,1,0,0,0,43,34,1,0,0,0,43,36,1,0,0,0,43,40,1,0,0,0,44,3,
        1,0,0,0,45,46,6,2,-1,0,46,49,5,10,0,0,47,49,5,11,0,0,48,45,1,0,0,
        0,48,47,1,0,0,0,49,70,1,0,0,0,50,51,10,8,0,0,51,52,7,0,0,0,52,69,
        3,4,2,9,53,54,10,7,0,0,54,55,7,1,0,0,55,69,3,4,2,8,56,57,10,6,0,
        0,57,58,7,2,0,0,58,69,3,4,2,7,59,60,10,5,0,0,60,61,7,3,0,0,61,69,
        3,4,2,6,62,63,10,4,0,0,63,64,7,4,0,0,64,69,3,4,2,5,65,66,10,3,0,
        0,66,67,7,5,0,0,67,69,3,4,2,4,68,50,1,0,0,0,68,53,1,0,0,0,68,56,
        1,0,0,0,68,59,1,0,0,0,68,62,1,0,0,0,68,65,1,0,0,0,69,72,1,0,0,0,
        70,68,1,0,0,0,70,71,1,0,0,0,71,5,1,0,0,0,72,70,1,0,0,0,6,9,22,43,
        48,68,70
    ]

class LogosParser ( Parser ):

    grammarFileName = "Logos.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'if'", "'{'", "'}'", "'while'", 
                     "'do'", "'exit'", "'include'", "'mem'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", 
                     "'>'", "'>='", "'<'", "'<='", "'&'", "'^'", "'|'", 
                     "'||'", "'&&'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "FLOAT", "STRING", 
                      "COMMENT", "WS", "OP_ADD", "OP_SUB", "OP_MUL", "OP_DIV", 
                      "OP_EQ", "OP_NEQ", "OP_GT", "OP_GEQ", "OP_LT", "OP_LEQ", 
                      "OP_AND", "OP_XOR", "OP_OR", "OP_LOGICAL_OR", "OP_LOGICAL_AND" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stmt", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    ID=10
    INT=11
    FLOAT=12
    STRING=13
    COMMENT=14
    WS=15
    OP_ADD=16
    OP_SUB=17
    OP_MUL=18
    OP_DIV=19
    OP_EQ=20
    OP_NEQ=21
    OP_GT=22
    OP_GEQ=23
    OP_LT=24
    OP_LEQ=25
    OP_AND=26
    OP_XOR=27
    OP_OR=28
    OP_LOGICAL_OR=29
    OP_LOGICAL_AND=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LogosParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogosParser.StmtContext)
            else:
                return self.getTypedRuleContext(LogosParser.StmtContext,i)


        def getRuleIndex(self):
            return LogosParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = LogosParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.stmt()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1956) != 0)):
                    break

            self.state = 11
            self.match(LogosParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LogosParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExitContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LogosParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExit" ):
                listener.enterExit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExit" ):
                listener.exitExit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExit" ):
                return visitor.visitExit(self)
            else:
                return visitor.visitChildren(self)


    class IncludeContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(LogosParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInclude" ):
                listener.enterInclude(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInclude" ):
                listener.exitInclude(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInclude" ):
                return visitor.visitInclude(self)
            else:
                return visitor.visitChildren(self)


    class AssignMemContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.StmtContext
            super().__init__(parser)
            self.size = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LogosParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(LogosParser.ExprContext,0)

        def INT(self):
            return self.getToken(LogosParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignMem" ):
                listener.enterAssignMem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignMem" ):
                listener.exitAssignMem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignMem" ):
                return visitor.visitAssignMem(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LogosParser.ExprContext,0)

        def stmt(self):
            return self.getTypedRuleContext(LogosParser.StmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.StmtContext
            super().__init__(parser)
            self._stmt = None # StmtContext
            self.stmts = list() # of StmtContexts
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LogosParser.ExprContext,0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogosParser.StmtContext)
            else:
                return self.getTypedRuleContext(LogosParser.StmtContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LogosParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(LogosParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = LogosParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = LogosParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.match(LogosParser.ID)
                self.state = 14
                self.match(LogosParser.T__0)
                self.state = 15
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = LogosParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(LogosParser.T__1)
                self.state = 17
                self.expr(0)
                self.state = 18
                self.match(LogosParser.T__2)
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1956) != 0):
                    self.state = 19
                    localctx._stmt = self.stmt()
                    localctx.stmts.append(localctx._stmt)
                    self.state = 24
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 25
                self.match(LogosParser.T__3)
                pass

            elif la_ == 3:
                localctx = LogosParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.match(LogosParser.T__4)
                self.state = 28
                self.expr(0)
                self.state = 29
                self.match(LogosParser.T__5)
                self.state = 30
                self.stmt()
                pass

            elif la_ == 4:
                localctx = LogosParser.ExitContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.match(LogosParser.T__6)
                self.state = 33
                self.match(LogosParser.ID)
                pass

            elif la_ == 5:
                localctx = LogosParser.IncludeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 34
                self.match(LogosParser.T__7)
                self.state = 35
                self.match(LogosParser.STRING)
                pass

            elif la_ == 6:
                localctx = LogosParser.AssignMemContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 36
                self.match(LogosParser.T__8)
                self.state = 37
                self.match(LogosParser.ID)
                self.state = 38
                self.match(LogosParser.T__0)
                self.state = 39
                self.expr(0)
                pass

            elif la_ == 7:
                localctx = LogosParser.AssignMemContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 40
                self.match(LogosParser.T__8)
                self.state = 41
                localctx.size = self.match(LogosParser.INT)
                self.state = 42
                self.match(LogosParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LogosParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class LeLeqGeGeqContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogosParser.ExprContext)
            else:
                return self.getTypedRuleContext(LogosParser.ExprContext,i)

        def OP_LT(self):
            return self.getToken(LogosParser.OP_LT, 0)
        def OP_LEQ(self):
            return self.getToken(LogosParser.OP_LEQ, 0)
        def OP_GT(self):
            return self.getToken(LogosParser.OP_GT, 0)
        def OP_GEQ(self):
            return self.getToken(LogosParser.OP_GEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeLeqGeGeq" ):
                listener.enterLeLeqGeGeq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeLeqGeGeq" ):
                listener.exitLeLeqGeGeq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeLeqGeGeq" ):
                return visitor.visitLeLeqGeGeq(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogosParser.ExprContext)
            else:
                return self.getTypedRuleContext(LogosParser.ExprContext,i)

        def OP_MUL(self):
            return self.getToken(LogosParser.OP_MUL, 0)
        def OP_DIV(self):
            return self.getToken(LogosParser.OP_DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogosParser.ExprContext)
            else:
                return self.getTypedRuleContext(LogosParser.ExprContext,i)

        def OP_ADD(self):
            return self.getToken(LogosParser.OP_ADD, 0)
        def OP_SUB(self):
            return self.getToken(LogosParser.OP_SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class LogicalAndOrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogosParser.ExprContext)
            else:
                return self.getTypedRuleContext(LogosParser.ExprContext,i)

        def OP_LOGICAL_AND(self):
            return self.getToken(LogosParser.OP_LOGICAL_AND, 0)
        def OP_LOGICAL_OR(self):
            return self.getToken(LogosParser.OP_LOGICAL_OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAndOr" ):
                listener.enterLogicalAndOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAndOr" ):
                listener.exitLogicalAndOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndOr" ):
                return visitor.visitLogicalAndOr(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LogosParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class AndXorOrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogosParser.ExprContext)
            else:
                return self.getTypedRuleContext(LogosParser.ExprContext,i)

        def OP_AND(self):
            return self.getToken(LogosParser.OP_AND, 0)
        def OP_XOR(self):
            return self.getToken(LogosParser.OP_XOR, 0)
        def OP_OR(self):
            return self.getToken(LogosParser.OP_OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndXorOr" ):
                listener.enterAndXorOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndXorOr" ):
                listener.exitAndXorOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndXorOr" ):
                return visitor.visitAndXorOr(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(LogosParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class EqNeqContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogosParser.ExprContext)
            else:
                return self.getTypedRuleContext(LogosParser.ExprContext,i)

        def OP_EQ(self):
            return self.getToken(LogosParser.OP_EQ, 0)
        def OP_NEQ(self):
            return self.getToken(LogosParser.OP_NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqNeq" ):
                listener.enterEqNeq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqNeq" ):
                listener.exitEqNeq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqNeq" ):
                return visitor.visitEqNeq(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LogosParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = LogosParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 46
                self.match(LogosParser.ID)
                pass
            elif token in [11]:
                localctx = LogosParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 47
                self.match(LogosParser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 68
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = LogosParser.MulDivContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 50
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 51
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 52
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = LogosParser.AddSubContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 53
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 54
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 55
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = LogosParser.LeLeqGeGeqContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 56
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 57
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62914560) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 58
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = LogosParser.EqNeqContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 59
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 60
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 61
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = LogosParser.AndXorOrContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 62
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 63
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 64
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 6:
                        localctx = LogosParser.LogicalAndOrContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 65
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 66
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==29 or _la==30):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 67
                        localctx.right = self.expr(4)
                        pass

             
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         




