# Generated from Logos.g4 by ANTLR 4.13.0
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
        4,1,26,56,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,26,8,1,1,
        2,1,2,1,2,3,2,31,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,51,8,2,10,2,12,2,54,9,2,1,2,0,1,
        4,3,0,2,4,0,6,1,0,14,15,1,0,12,13,1,0,18,21,1,0,16,17,1,0,22,24,
        1,0,25,26,63,0,7,1,0,0,0,2,25,1,0,0,0,4,30,1,0,0,0,6,8,3,2,1,0,7,
        6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,11,1,0,0,0,11,
        12,5,0,0,1,12,1,1,0,0,0,13,14,5,6,0,0,14,15,5,1,0,0,15,26,3,4,2,
        0,16,17,5,2,0,0,17,26,5,6,0,0,18,19,5,3,0,0,19,20,3,4,2,0,20,21,
        5,4,0,0,21,22,3,2,1,0,22,26,1,0,0,0,23,24,5,5,0,0,24,26,5,6,0,0,
        25,13,1,0,0,0,25,16,1,0,0,0,25,18,1,0,0,0,25,23,1,0,0,0,26,3,1,0,
        0,0,27,28,6,2,-1,0,28,31,5,6,0,0,29,31,5,7,0,0,30,27,1,0,0,0,30,
        29,1,0,0,0,31,52,1,0,0,0,32,33,10,8,0,0,33,34,7,0,0,0,34,51,3,4,
        2,9,35,36,10,7,0,0,36,37,7,1,0,0,37,51,3,4,2,8,38,39,10,6,0,0,39,
        40,7,2,0,0,40,51,3,4,2,7,41,42,10,5,0,0,42,43,7,3,0,0,43,51,3,4,
        2,6,44,45,10,4,0,0,45,46,7,4,0,0,46,51,3,4,2,5,47,48,10,3,0,0,48,
        49,7,5,0,0,49,51,3,4,2,4,50,32,1,0,0,0,50,35,1,0,0,0,50,38,1,0,0,
        0,50,41,1,0,0,0,50,44,1,0,0,0,50,47,1,0,0,0,51,54,1,0,0,0,52,50,
        1,0,0,0,52,53,1,0,0,0,53,5,1,0,0,0,54,52,1,0,0,0,5,9,25,30,50,52
    ]

class LogosParser ( Parser ):

    grammarFileName = "Logos.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'print'", "'if'", "'then'", "'exit'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", "'&'", 
                     "'^'", "'|'", "'||'", "'&&'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "WS", "FLOAT", 
                      "STRING", "COMMENT", "OP_ADD", "OP_SUB", "OP_MUL", 
                      "OP_DIV", "OP_EQ", "OP_NEQ", "OP_GT", "OP_GEQ", "OP_LT", 
                      "OP_LEQ", "OP_AND", "OP_XOR", "OP_OR", "OP_LOGICAL_OR", 
                      "OP_LOGICAL_AND" ]

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
    ID=6
    INT=7
    WS=8
    FLOAT=9
    STRING=10
    COMMENT=11
    OP_ADD=12
    OP_SUB=13
    OP_MUL=14
    OP_DIV=15
    OP_EQ=16
    OP_NEQ=17
    OP_GT=18
    OP_GEQ=19
    OP_LT=20
    OP_LEQ=21
    OP_AND=22
    OP_XOR=23
    OP_OR=24
    OP_LOGICAL_OR=25
    OP_LOGICAL_AND=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 108) != 0)):
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


    class PrintContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LogosParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)


    class IfContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LogosParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LogosParser.ExprContext,0)

        def stmt(self):
            return self.getTypedRuleContext(LogosParser.StmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)


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



    def stmt(self):

        localctx = LogosParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = LogosParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.match(LogosParser.ID)
                self.state = 14
                self.match(LogosParser.T__0)
                self.state = 15
                self.expr(0)
                pass
            elif token in [2]:
                localctx = LogosParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(LogosParser.T__1)
                self.state = 17
                self.match(LogosParser.ID)
                pass
            elif token in [3]:
                localctx = LogosParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 18
                self.match(LogosParser.T__2)
                self.state = 19
                self.expr(0)
                self.state = 20
                self.match(LogosParser.T__3)
                self.state = 21
                self.stmt()
                pass
            elif token in [5]:
                localctx = LogosParser.ExitContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 23
                self.match(LogosParser.T__4)
                self.state = 24
                self.match(LogosParser.ID)
                pass
            else:
                raise NoViableAltException(self)

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
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = LogosParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 28
                self.match(LogosParser.ID)
                pass
            elif token in [7]:
                localctx = LogosParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                self.match(LogosParser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 50
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = LogosParser.MulDivContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 32
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 33
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 34
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = LogosParser.AddSubContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 36
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 37
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = LogosParser.LeLeqGeGeqContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 39
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3932160) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 40
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = LogosParser.EqNeqContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 41
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 42
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 43
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = LogosParser.AndXorOrContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 44
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 45
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 46
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 6:
                        localctx = LogosParser.LogicalAndOrContext(self, LogosParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 47
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 48
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==25 or _la==26):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 49
                        localctx.right = self.expr(4)
                        pass

             
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
         




