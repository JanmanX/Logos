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
        4,1,29,80,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,1,1,
        1,1,1,1,1,1,1,1,1,1,5,1,32,8,1,10,1,12,1,35,9,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,50,8,1,1,2,1,2,1,2,3,2,55,
        8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,5,2,75,8,2,10,2,12,2,78,9,2,1,2,0,1,4,3,0,2,4,0,6,1,
        0,17,18,1,0,15,16,1,0,21,24,1,0,19,20,1,0,25,27,1,0,28,29,92,0,7,
        1,0,0,0,2,49,1,0,0,0,4,54,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,9,1,
        0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,11,1,0,0,0,11,12,5,0,0,1,12,1,
        1,0,0,0,13,14,5,9,0,0,14,15,5,1,0,0,15,50,3,4,2,0,16,17,5,2,0,0,
        17,18,3,4,2,0,18,22,5,3,0,0,19,21,3,2,1,0,20,19,1,0,0,0,21,24,1,
        0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,25,1,0,0,0,24,22,1,0,0,0,25,
        26,5,4,0,0,26,50,1,0,0,0,27,28,5,5,0,0,28,29,3,4,2,0,29,33,5,3,0,
        0,30,32,3,2,1,0,31,30,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,
        1,0,0,0,34,36,1,0,0,0,35,33,1,0,0,0,36,37,5,4,0,0,37,50,1,0,0,0,
        38,39,5,6,0,0,39,50,5,9,0,0,40,41,5,7,0,0,41,50,5,12,0,0,42,43,5,
        8,0,0,43,44,5,9,0,0,44,45,5,1,0,0,45,50,3,4,2,0,46,47,5,8,0,0,47,
        48,5,10,0,0,48,50,5,9,0,0,49,13,1,0,0,0,49,16,1,0,0,0,49,27,1,0,
        0,0,49,38,1,0,0,0,49,40,1,0,0,0,49,42,1,0,0,0,49,46,1,0,0,0,50,3,
        1,0,0,0,51,52,6,2,-1,0,52,55,5,9,0,0,53,55,5,10,0,0,54,51,1,0,0,
        0,54,53,1,0,0,0,55,76,1,0,0,0,56,57,10,8,0,0,57,58,7,0,0,0,58,75,
        3,4,2,9,59,60,10,7,0,0,60,61,7,1,0,0,61,75,3,4,2,8,62,63,10,6,0,
        0,63,64,7,2,0,0,64,75,3,4,2,7,65,66,10,5,0,0,66,67,7,3,0,0,67,75,
        3,4,2,6,68,69,10,4,0,0,69,70,7,4,0,0,70,75,3,4,2,5,71,72,10,3,0,
        0,72,73,7,5,0,0,73,75,3,4,2,4,74,56,1,0,0,0,74,59,1,0,0,0,74,62,
        1,0,0,0,74,65,1,0,0,0,74,68,1,0,0,0,74,71,1,0,0,0,75,78,1,0,0,0,
        76,74,1,0,0,0,76,77,1,0,0,0,77,5,1,0,0,0,78,76,1,0,0,0,7,9,22,33,
        49,54,74,76
    ]

class LogosParser ( Parser ):

    grammarFileName = "Logos.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'if'", "'{'", "'}'", "'while'", 
                     "'exit'", "'include'", "'mem'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", "'>'", 
                     "'>='", "'<'", "'<='", "'&'", "'^'", "'|'", "'||'", 
                     "'&&'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "FLOAT", "STRING", "COMMENT", 
                      "WS", "OP_ADD", "OP_SUB", "OP_MUL", "OP_DIV", "OP_EQ", 
                      "OP_NEQ", "OP_GT", "OP_GEQ", "OP_LT", "OP_LEQ", "OP_AND", 
                      "OP_XOR", "OP_OR", "OP_LOGICAL_OR", "OP_LOGICAL_AND" ]

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
    ID=9
    INT=10
    FLOAT=11
    STRING=12
    COMMENT=13
    WS=14
    OP_ADD=15
    OP_SUB=16
    OP_MUL=17
    OP_DIV=18
    OP_EQ=19
    OP_NEQ=20
    OP_GT=21
    OP_GEQ=22
    OP_LT=23
    OP_LEQ=24
    OP_AND=25
    OP_XOR=26
    OP_OR=27
    OP_LOGICAL_OR=28
    OP_LOGICAL_AND=29

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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 996) != 0)):
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
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
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
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 996) != 0):
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
                self.match(LogosParser.T__2)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 996) != 0):
                    self.state = 30
                    localctx._stmt = self.stmt()
                    localctx.stmts.append(localctx._stmt)
                    self.state = 35
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 36
                self.match(LogosParser.T__3)
                pass

            elif la_ == 4:
                localctx = LogosParser.ExitContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.match(LogosParser.T__5)
                self.state = 39
                self.match(LogosParser.ID)
                pass

            elif la_ == 5:
                localctx = LogosParser.IncludeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 40
                self.match(LogosParser.T__6)
                self.state = 41
                self.match(LogosParser.STRING)
                pass

            elif la_ == 6:
                localctx = LogosParser.AssignMemContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 42
                self.match(LogosParser.T__7)
                self.state = 43
                self.match(LogosParser.ID)
                self.state = 44
                self.match(LogosParser.T__0)
                self.state = 45
                self.expr(0)
                pass

            elif la_ == 7:
                localctx = LogosParser.AssignMemContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 46
                self.match(LogosParser.T__7)
                self.state = 47
                localctx.size = self.match(LogosParser.INT)
                self.state = 48
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
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                localctx = LogosParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 52
                self.match(LogosParser.ID)
                pass
            elif token in [10]:
                localctx = LogosParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 53
                self.match(LogosParser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 76
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 74
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = LogosParser.MulDivContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 56
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 57
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 58
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = LogosParser.AddSubContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 59
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 60
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 61
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = LogosParser.LeLeqGeGeqContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 62
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 63
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31457280) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 64
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = LogosParser.EqNeqContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 65
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 66
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 67
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = LogosParser.AndXorOrContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 68
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 69
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 70
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 6:
                        localctx = LogosParser.LogicalAndOrContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 71
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 72
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==28 or _la==29):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 73
                        localctx.right = self.expr(4)
                        pass

             
                self.state = 78
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
         




