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
        4,1,33,119,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,41,8,1,10,1,
        12,1,44,9,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,52,8,1,10,1,12,1,55,9,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,64,8,1,10,1,12,1,67,9,1,1,1,1,1,
        1,1,1,1,5,1,73,8,1,10,1,12,1,76,9,1,1,1,1,1,1,1,3,1,81,8,1,1,2,1,
        2,1,2,5,2,86,8,2,10,2,12,2,89,9,2,1,3,1,3,1,3,3,3,94,8,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        5,3,114,8,3,10,3,12,3,117,9,3,1,3,0,1,6,4,0,2,4,6,0,6,1,0,21,22,
        1,0,19,20,1,0,25,28,1,0,23,24,1,0,29,31,1,0,32,33,135,0,9,1,0,0,
        0,2,80,1,0,0,0,4,82,1,0,0,0,6,93,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,
        0,10,11,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,13,1,0,0,0,13,14,5,
        0,0,1,14,1,1,0,0,0,15,16,5,13,0,0,16,17,5,1,0,0,17,81,3,6,3,0,18,
        19,5,13,0,0,19,20,5,1,0,0,20,21,5,2,0,0,21,81,5,14,0,0,22,23,5,13,
        0,0,23,24,5,3,0,0,24,25,3,6,3,0,25,26,5,4,0,0,26,27,5,1,0,0,27,28,
        3,6,3,0,28,81,1,0,0,0,29,30,5,13,0,0,30,31,5,1,0,0,31,32,5,13,0,
        0,32,33,5,3,0,0,33,34,3,6,3,0,34,35,5,4,0,0,35,81,1,0,0,0,36,37,
        5,5,0,0,37,38,3,6,3,0,38,42,5,6,0,0,39,41,3,2,1,0,40,39,1,0,0,0,
        41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,45,1,0,0,0,44,42,1,
        0,0,0,45,46,5,7,0,0,46,81,1,0,0,0,47,48,5,8,0,0,48,49,3,6,3,0,49,
        53,5,6,0,0,50,52,3,2,1,0,51,50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,
        0,53,54,1,0,0,0,54,56,1,0,0,0,55,53,1,0,0,0,56,57,5,7,0,0,57,81,
        1,0,0,0,58,59,5,13,0,0,59,60,5,1,0,0,60,61,5,13,0,0,61,65,5,9,0,
        0,62,64,3,4,2,0,63,62,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,
        1,0,0,0,66,68,1,0,0,0,67,65,1,0,0,0,68,81,5,10,0,0,69,70,5,13,0,
        0,70,74,5,9,0,0,71,73,3,4,2,0,72,71,1,0,0,0,73,76,1,0,0,0,74,72,
        1,0,0,0,74,75,1,0,0,0,75,77,1,0,0,0,76,74,1,0,0,0,77,81,5,10,0,0,
        78,79,5,11,0,0,79,81,5,16,0,0,80,15,1,0,0,0,80,18,1,0,0,0,80,22,
        1,0,0,0,80,29,1,0,0,0,80,36,1,0,0,0,80,47,1,0,0,0,80,58,1,0,0,0,
        80,69,1,0,0,0,80,78,1,0,0,0,81,3,1,0,0,0,82,87,3,6,3,0,83,84,5,12,
        0,0,84,86,3,6,3,0,85,83,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,
        1,0,0,0,88,5,1,0,0,0,89,87,1,0,0,0,90,91,6,3,-1,0,91,94,5,13,0,0,
        92,94,5,14,0,0,93,90,1,0,0,0,93,92,1,0,0,0,94,115,1,0,0,0,95,96,
        10,8,0,0,96,97,7,0,0,0,97,114,3,6,3,9,98,99,10,7,0,0,99,100,7,1,
        0,0,100,114,3,6,3,8,101,102,10,6,0,0,102,103,7,2,0,0,103,114,3,6,
        3,7,104,105,10,5,0,0,105,106,7,3,0,0,106,114,3,6,3,6,107,108,10,
        4,0,0,108,109,7,4,0,0,109,114,3,6,3,5,110,111,10,3,0,0,111,112,7,
        5,0,0,112,114,3,6,3,4,113,95,1,0,0,0,113,98,1,0,0,0,113,101,1,0,
        0,0,113,104,1,0,0,0,113,107,1,0,0,0,113,110,1,0,0,0,114,117,1,0,
        0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,7,1,0,0,0,117,115,1,0,0,
        0,10,11,42,53,65,74,80,87,93,113,115
    ]

class LogosParser ( Parser ):

    grammarFileName = "Logos.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'alloc'", "'['", "']'", "'if'", 
                     "'{'", "'}'", "'while'", "'('", "')'", "'include'", 
                     "','", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", "'&'", 
                     "'^'", "'|'", "'||'", "'&&'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "FLOAT", "STRING", "COMMENT", 
                      "WS", "OP_ADD", "OP_SUB", "OP_MUL", "OP_DIV", "OP_EQ", 
                      "OP_NEQ", "OP_GT", "OP_GEQ", "OP_LT", "OP_LEQ", "OP_AND", 
                      "OP_XOR", "OP_OR", "OP_LOGICAL_OR", "OP_LOGICAL_AND" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_exprs = 2
    RULE_expr = 3

    ruleNames =  [ "prog", "stmt", "exprs", "expr" ]

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
    T__9=10
    T__10=11
    T__11=12
    ID=13
    INT=14
    FLOAT=15
    STRING=16
    COMMENT=17
    WS=18
    OP_ADD=19
    OP_SUB=20
    OP_MUL=21
    OP_DIV=22
    OP_EQ=23
    OP_NEQ=24
    OP_GT=25
    OP_GEQ=26
    OP_LT=27
    OP_LEQ=28
    OP_AND=29
    OP_XOR=30
    OP_OR=31
    OP_LOGICAL_OR=32
    OP_LOGICAL_AND=33

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
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.stmt()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 10528) != 0)):
                    break

            self.state = 13
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



    class CallContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.StmtContext
            super().__init__(parser)
            self.func = None # Token
            self.args = None # ExprsContext
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LogosParser.ID, 0)
        def exprs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogosParser.ExprsContext)
            else:
                return self.getTypedRuleContext(LogosParser.ExprsContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)


    class IncludeContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.StmtContext
            super().__init__(parser)
            self.path = None # Token
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


    class WriteMemContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.StmtContext
            super().__init__(parser)
            self.index = None # ExprContext
            self.value = None # ExprContext
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LogosParser.ID, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogosParser.ExprContext)
            else:
                return self.getTypedRuleContext(LogosParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteMem" ):
                listener.enterWriteMem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteMem" ):
                listener.exitWriteMem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteMem" ):
                return visitor.visitWriteMem(self)
            else:
                return visitor.visitChildren(self)


    class AllocMemContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.StmtContext
            super().__init__(parser)
            self.size = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LogosParser.ID, 0)
        def INT(self):
            return self.getToken(LogosParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllocMem" ):
                listener.enterAllocMem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllocMem" ):
                listener.exitAllocMem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAllocMem" ):
                return visitor.visitAllocMem(self)
            else:
                return visitor.visitChildren(self)


    class CallReturnContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.StmtContext
            super().__init__(parser)
            self.func = None # Token
            self.args = None # ExprsContext
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LogosParser.ID)
            else:
                return self.getToken(LogosParser.ID, i)
        def exprs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogosParser.ExprsContext)
            else:
                return self.getTypedRuleContext(LogosParser.ExprsContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallReturn" ):
                listener.enterCallReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallReturn" ):
                listener.exitCallReturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallReturn" ):
                return visitor.visitCallReturn(self)
            else:
                return visitor.visitChildren(self)


    class ReadMemContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.StmtContext
            super().__init__(parser)
            self.dest = None # Token
            self.source = None # Token
            self.index = None # ExprContext
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LogosParser.ID)
            else:
                return self.getToken(LogosParser.ID, i)
        def expr(self):
            return self.getTypedRuleContext(LogosParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadMem" ):
                listener.enterReadMem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadMem" ):
                listener.exitReadMem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadMem" ):
                return visitor.visitReadMem(self)
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
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = LogosParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.match(LogosParser.ID)
                self.state = 16
                self.match(LogosParser.T__0)
                self.state = 17
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = LogosParser.AllocMemContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(LogosParser.ID)
                self.state = 19
                self.match(LogosParser.T__0)
                self.state = 20
                self.match(LogosParser.T__1)
                self.state = 21
                localctx.size = self.match(LogosParser.INT)
                pass

            elif la_ == 3:
                localctx = LogosParser.WriteMemContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.match(LogosParser.ID)
                self.state = 23
                self.match(LogosParser.T__2)
                self.state = 24
                localctx.index = self.expr(0)
                self.state = 25
                self.match(LogosParser.T__3)
                self.state = 26
                self.match(LogosParser.T__0)
                self.state = 27
                localctx.value = self.expr(0)
                pass

            elif la_ == 4:
                localctx = LogosParser.ReadMemContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 29
                localctx.dest = self.match(LogosParser.ID)
                self.state = 30
                self.match(LogosParser.T__0)
                self.state = 31
                localctx.source = self.match(LogosParser.ID)
                self.state = 32
                self.match(LogosParser.T__2)
                self.state = 33
                localctx.index = self.expr(0)
                self.state = 34
                self.match(LogosParser.T__3)
                pass

            elif la_ == 5:
                localctx = LogosParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 36
                self.match(LogosParser.T__4)
                self.state = 37
                self.expr(0)
                self.state = 38
                self.match(LogosParser.T__5)
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 10528) != 0):
                    self.state = 39
                    localctx._stmt = self.stmt()
                    localctx.stmts.append(localctx._stmt)
                    self.state = 44
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 45
                self.match(LogosParser.T__6)
                pass

            elif la_ == 6:
                localctx = LogosParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 47
                self.match(LogosParser.T__7)
                self.state = 48
                self.expr(0)
                self.state = 49
                self.match(LogosParser.T__5)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 10528) != 0):
                    self.state = 50
                    localctx._stmt = self.stmt()
                    localctx.stmts.append(localctx._stmt)
                    self.state = 55
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 56
                self.match(LogosParser.T__6)
                pass

            elif la_ == 7:
                localctx = LogosParser.CallReturnContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 58
                self.match(LogosParser.ID)
                self.state = 59
                self.match(LogosParser.T__0)
                self.state = 60
                localctx.func = self.match(LogosParser.ID)
                self.state = 61
                self.match(LogosParser.T__8)
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13 or _la==14:
                    self.state = 62
                    localctx.args = self.exprs()
                    self.state = 67
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 68
                self.match(LogosParser.T__9)
                pass

            elif la_ == 8:
                localctx = LogosParser.CallContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 69
                localctx.func = self.match(LogosParser.ID)
                self.state = 70
                self.match(LogosParser.T__8)
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13 or _la==14:
                    self.state = 71
                    localctx.args = self.exprs()
                    self.state = 76
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 77
                self.match(LogosParser.T__9)
                pass

            elif la_ == 9:
                localctx = LogosParser.IncludeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 78
                self.match(LogosParser.T__10)
                self.state = 79
                localctx.path = self.match(LogosParser.STRING)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogosParser.ExprContext)
            else:
                return self.getTypedRuleContext(LogosParser.ExprContext,i)


        def getRuleIndex(self):
            return LogosParser.RULE_exprs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprs" ):
                listener.enterExprs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprs" ):
                listener.exitExprs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprs" ):
                return visitor.visitExprs(self)
            else:
                return visitor.visitChildren(self)




    def exprs(self):

        localctx = LogosParser.ExprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_exprs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.expr(0)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 83
                self.match(LogosParser.T__11)
                self.state = 84
                self.expr(0)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                localctx = LogosParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 91
                self.match(LogosParser.ID)
                pass
            elif token in [14]:
                localctx = LogosParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 92
                self.match(LogosParser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 115
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 113
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = LogosParser.MulDivContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 95
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 96
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 97
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = LogosParser.AddSubContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 98
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 99
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 100
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = LogosParser.LeLeqGeGeqContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 101
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 102
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 503316480) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 103
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = LogosParser.EqNeqContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 104
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 105
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 106
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = LogosParser.AndXorOrContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 107
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 108
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 109
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 6:
                        localctx = LogosParser.LogicalAndOrContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 110
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 111
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==32 or _la==33):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 112
                        localctx.right = self.expr(4)
                        pass

             
                self.state = 117
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
        self._predicates[3] = self.expr_sempred
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
         




