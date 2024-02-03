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
        4,1,35,152,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,0,1,0,1,1,1,1,1,1,1,1,5,1,24,8,1,10,1,12,
        1,27,9,1,1,1,1,1,1,1,5,1,32,8,1,10,1,12,1,35,9,1,1,1,1,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,64,8,2,10,2,12,2,67,9,2,1,2,1,2,
        1,2,1,2,1,2,1,2,5,2,75,8,2,10,2,12,2,78,9,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,5,2,87,8,2,10,2,12,2,90,9,2,1,2,1,2,1,2,1,2,5,2,96,8,2,10,
        2,12,2,99,9,2,1,2,1,2,1,2,1,2,1,2,3,2,106,8,2,1,3,1,3,1,3,5,3,111,
        8,3,10,3,12,3,114,9,3,1,4,1,4,1,4,5,4,119,8,4,10,4,12,4,122,9,4,
        1,5,1,5,1,5,3,5,127,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,147,8,5,10,5,12,5,150,9,5,1,
        5,0,1,10,6,0,2,4,6,8,10,0,6,1,0,23,24,1,0,21,22,1,0,27,30,1,0,25,
        26,1,0,31,33,1,0,34,35,170,0,13,1,0,0,0,2,19,1,0,0,0,4,105,1,0,0,
        0,6,107,1,0,0,0,8,115,1,0,0,0,10,126,1,0,0,0,12,14,3,2,1,0,13,12,
        1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,17,1,0,0,0,
        17,18,5,0,0,1,18,1,1,0,0,0,19,20,5,1,0,0,20,21,5,15,0,0,21,25,5,
        2,0,0,22,24,3,6,3,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,
        26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,29,5,3,0,0,29,33,5,4,0,
        0,30,32,3,4,2,0,31,30,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,
        1,0,0,0,34,36,1,0,0,0,35,33,1,0,0,0,36,37,5,5,0,0,37,3,1,0,0,0,38,
        39,5,15,0,0,39,40,5,6,0,0,40,106,3,10,5,0,41,42,5,15,0,0,42,43,5,
        6,0,0,43,44,5,7,0,0,44,106,5,16,0,0,45,46,5,15,0,0,46,47,5,8,0,0,
        47,48,3,10,5,0,48,49,5,9,0,0,49,50,5,6,0,0,50,51,3,10,5,0,51,106,
        1,0,0,0,52,53,5,15,0,0,53,54,5,6,0,0,54,55,5,15,0,0,55,56,5,8,0,
        0,56,57,3,10,5,0,57,58,5,9,0,0,58,106,1,0,0,0,59,60,5,10,0,0,60,
        61,3,10,5,0,61,65,5,4,0,0,62,64,3,4,2,0,63,62,1,0,0,0,64,67,1,0,
        0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,65,1,0,0,0,68,69,
        5,5,0,0,69,106,1,0,0,0,70,71,5,11,0,0,71,72,3,10,5,0,72,76,5,4,0,
        0,73,75,3,4,2,0,74,73,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,
        1,0,0,0,77,79,1,0,0,0,78,76,1,0,0,0,79,80,5,5,0,0,80,106,1,0,0,0,
        81,82,5,15,0,0,82,83,5,6,0,0,83,84,5,15,0,0,84,88,5,2,0,0,85,87,
        3,8,4,0,86,85,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,
        89,91,1,0,0,0,90,88,1,0,0,0,91,106,5,3,0,0,92,93,5,15,0,0,93,97,
        5,2,0,0,94,96,3,8,4,0,95,94,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,
        97,98,1,0,0,0,98,100,1,0,0,0,99,97,1,0,0,0,100,106,5,3,0,0,101,102,
        5,12,0,0,102,106,5,18,0,0,103,104,5,13,0,0,104,106,3,10,5,0,105,
        38,1,0,0,0,105,41,1,0,0,0,105,45,1,0,0,0,105,52,1,0,0,0,105,59,1,
        0,0,0,105,70,1,0,0,0,105,81,1,0,0,0,105,92,1,0,0,0,105,101,1,0,0,
        0,105,103,1,0,0,0,106,5,1,0,0,0,107,112,5,15,0,0,108,109,5,14,0,
        0,109,111,5,15,0,0,110,108,1,0,0,0,111,114,1,0,0,0,112,110,1,0,0,
        0,112,113,1,0,0,0,113,7,1,0,0,0,114,112,1,0,0,0,115,120,3,10,5,0,
        116,117,5,14,0,0,117,119,3,10,5,0,118,116,1,0,0,0,119,122,1,0,0,
        0,120,118,1,0,0,0,120,121,1,0,0,0,121,9,1,0,0,0,122,120,1,0,0,0,
        123,124,6,5,-1,0,124,127,5,15,0,0,125,127,5,16,0,0,126,123,1,0,0,
        0,126,125,1,0,0,0,127,148,1,0,0,0,128,129,10,8,0,0,129,130,7,0,0,
        0,130,147,3,10,5,9,131,132,10,7,0,0,132,133,7,1,0,0,133,147,3,10,
        5,8,134,135,10,6,0,0,135,136,7,2,0,0,136,147,3,10,5,7,137,138,10,
        5,0,0,138,139,7,3,0,0,139,147,3,10,5,6,140,141,10,4,0,0,141,142,
        7,4,0,0,142,147,3,10,5,5,143,144,10,3,0,0,144,145,7,5,0,0,145,147,
        3,10,5,4,146,128,1,0,0,0,146,131,1,0,0,0,146,134,1,0,0,0,146,137,
        1,0,0,0,146,140,1,0,0,0,146,143,1,0,0,0,147,150,1,0,0,0,148,146,
        1,0,0,0,148,149,1,0,0,0,149,11,1,0,0,0,150,148,1,0,0,0,13,15,25,
        33,65,76,88,97,105,112,120,126,146,148
    ]

class LogosParser ( Parser ):

    grammarFileName = "Logos.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ritual'", "'('", "')'", "'{'", "'}'", 
                     "'='", "'alloc'", "'['", "']'", "'if'", "'while'", 
                     "'include'", "'return'", "','", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", "'>'", 
                     "'>='", "'<'", "'<='", "'&'", "'^'", "'|'", "'||'", 
                     "'&&'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "INT", 
                      "FLOAT", "STRING", "COMMENT", "WS", "OP_ADD", "OP_SUB", 
                      "OP_MUL", "OP_DIV", "OP_EQ", "OP_NEQ", "OP_GT", "OP_GEQ", 
                      "OP_LT", "OP_LEQ", "OP_AND", "OP_XOR", "OP_OR", "OP_LOGICAL_OR", 
                      "OP_LOGICAL_AND" ]

    RULE_prog = 0
    RULE_rituals = 1
    RULE_stmt = 2
    RULE_ids = 3
    RULE_exprs = 4
    RULE_expr = 5

    ruleNames =  [ "prog", "rituals", "stmt", "ids", "exprs", "expr" ]

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
    T__12=13
    T__13=14
    ID=15
    INT=16
    FLOAT=17
    STRING=18
    COMMENT=19
    WS=20
    OP_ADD=21
    OP_SUB=22
    OP_MUL=23
    OP_DIV=24
    OP_EQ=25
    OP_NEQ=26
    OP_GT=27
    OP_GEQ=28
    OP_LT=29
    OP_LEQ=30
    OP_AND=31
    OP_XOR=32
    OP_OR=33
    OP_LOGICAL_OR=34
    OP_LOGICAL_AND=35

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

        def rituals(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogosParser.RitualsContext)
            else:
                return self.getTypedRuleContext(LogosParser.RitualsContext,i)


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
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.rituals()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 17
            self.match(LogosParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RitualsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LogosParser.RULE_rituals

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RitualContext(RitualsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.RitualsContext
            super().__init__(parser)
            self.name = None # Token
            self._ids = None # IdsContext
            self.args = list() # of IdsContexts
            self._stmt = None # StmtContext
            self.stmts = list() # of StmtContexts
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LogosParser.ID, 0)
        def ids(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogosParser.IdsContext)
            else:
                return self.getTypedRuleContext(LogosParser.IdsContext,i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LogosParser.StmtContext)
            else:
                return self.getTypedRuleContext(LogosParser.StmtContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRitual" ):
                listener.enterRitual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRitual" ):
                listener.exitRitual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRitual" ):
                return visitor.visitRitual(self)
            else:
                return visitor.visitChildren(self)



    def rituals(self):

        localctx = LogosParser.RitualsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_rituals)
        self._la = 0 # Token type
        try:
            localctx = LogosParser.RitualContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(LogosParser.T__0)
            self.state = 20
            localctx.name = self.match(LogosParser.ID)
            self.state = 21
            self.match(LogosParser.T__1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 22
                localctx._ids = self.ids()
                localctx.args.append(localctx._ids)
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(LogosParser.T__2)
            self.state = 29
            self.match(LogosParser.T__3)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 48128) != 0):
                self.state = 30
                localctx._stmt = self.stmt()
                localctx.stmts.append(localctx._stmt)
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 36
            self.match(LogosParser.T__4)
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


    class ReturnContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LogosParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn" ):
                return visitor.visitReturn(self)
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
        self.enterRule(localctx, 4, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = LogosParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(LogosParser.ID)
                self.state = 39
                self.match(LogosParser.T__5)
                self.state = 40
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = LogosParser.AllocMemContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(LogosParser.ID)
                self.state = 42
                self.match(LogosParser.T__5)
                self.state = 43
                self.match(LogosParser.T__6)
                self.state = 44
                localctx.size = self.match(LogosParser.INT)
                pass

            elif la_ == 3:
                localctx = LogosParser.WriteMemContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.match(LogosParser.ID)
                self.state = 46
                self.match(LogosParser.T__7)
                self.state = 47
                localctx.index = self.expr(0)
                self.state = 48
                self.match(LogosParser.T__8)
                self.state = 49
                self.match(LogosParser.T__5)
                self.state = 50
                localctx.value = self.expr(0)
                pass

            elif la_ == 4:
                localctx = LogosParser.ReadMemContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                localctx.dest = self.match(LogosParser.ID)
                self.state = 53
                self.match(LogosParser.T__5)
                self.state = 54
                localctx.source = self.match(LogosParser.ID)
                self.state = 55
                self.match(LogosParser.T__7)
                self.state = 56
                localctx.index = self.expr(0)
                self.state = 57
                self.match(LogosParser.T__8)
                pass

            elif la_ == 5:
                localctx = LogosParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 59
                self.match(LogosParser.T__9)
                self.state = 60
                self.expr(0)
                self.state = 61
                self.match(LogosParser.T__3)
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 48128) != 0):
                    self.state = 62
                    localctx._stmt = self.stmt()
                    localctx.stmts.append(localctx._stmt)
                    self.state = 67
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 68
                self.match(LogosParser.T__4)
                pass

            elif la_ == 6:
                localctx = LogosParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 70
                self.match(LogosParser.T__10)
                self.state = 71
                self.expr(0)
                self.state = 72
                self.match(LogosParser.T__3)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 48128) != 0):
                    self.state = 73
                    localctx._stmt = self.stmt()
                    localctx.stmts.append(localctx._stmt)
                    self.state = 78
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 79
                self.match(LogosParser.T__4)
                pass

            elif la_ == 7:
                localctx = LogosParser.CallReturnContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 81
                self.match(LogosParser.ID)
                self.state = 82
                self.match(LogosParser.T__5)
                self.state = 83
                localctx.func = self.match(LogosParser.ID)
                self.state = 84
                self.match(LogosParser.T__1)
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15 or _la==16:
                    self.state = 85
                    localctx.args = self.exprs()
                    self.state = 90
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 91
                self.match(LogosParser.T__2)
                pass

            elif la_ == 8:
                localctx = LogosParser.CallContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 92
                localctx.func = self.match(LogosParser.ID)
                self.state = 93
                self.match(LogosParser.T__1)
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15 or _la==16:
                    self.state = 94
                    localctx.args = self.exprs()
                    self.state = 99
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 100
                self.match(LogosParser.T__2)
                pass

            elif la_ == 9:
                localctx = LogosParser.IncludeContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 101
                self.match(LogosParser.T__11)
                self.state = 102
                localctx.path = self.match(LogosParser.STRING)
                pass

            elif la_ == 10:
                localctx = LogosParser.ReturnContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 103
                self.match(LogosParser.T__12)
                self.state = 104
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LogosParser.ID)
            else:
                return self.getToken(LogosParser.ID, i)

        def getRuleIndex(self):
            return LogosParser.RULE_ids

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIds" ):
                listener.enterIds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIds" ):
                listener.exitIds(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds" ):
                return visitor.visitIds(self)
            else:
                return visitor.visitChildren(self)




    def ids(self):

        localctx = LogosParser.IdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ids)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(LogosParser.ID)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 108
                self.match(LogosParser.T__13)
                self.state = 109
                self.match(LogosParser.ID)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 8, self.RULE_exprs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.expr(0)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 116
                self.match(LogosParser.T__13)
                self.state = 117
                self.expr(0)
                self.state = 122
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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                localctx = LogosParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 124
                self.match(LogosParser.ID)
                pass
            elif token in [16]:
                localctx = LogosParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 125
                self.match(LogosParser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 148
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 146
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = LogosParser.MulDivContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 128
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 129
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 130
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = LogosParser.AddSubContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 131
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 132
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 133
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = LogosParser.LeLeqGeGeqContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 134
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 135
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2013265920) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 136
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = LogosParser.EqNeqContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 137
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 138
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==25 or _la==26):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 139
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = LogosParser.AndXorOrContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 140
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 141
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15032385536) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 142
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 6:
                        localctx = LogosParser.LogicalAndOrContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 143
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 144
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==34 or _la==35):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 145
                        localctx.right = self.expr(4)
                        pass

             
                self.state = 150
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self._predicates[5] = self.expr_sempred
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
         




