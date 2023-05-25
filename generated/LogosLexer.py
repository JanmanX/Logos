# Generated from Logos.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,14,80,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,
        1,9,1,10,1,10,1,11,4,11,65,8,11,11,11,12,11,66,1,12,4,12,70,8,12,
        11,12,12,12,71,1,13,4,13,75,8,13,11,13,12,13,76,1,13,1,13,0,0,14,
        1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,
        27,14,1,0,3,2,0,65,90,97,122,1,0,48,57,3,0,9,10,13,13,32,32,82,0,
        1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,
        0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,
        0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,1,29,1,0,0,0,3,32,1,
        0,0,0,5,38,1,0,0,0,7,41,1,0,0,0,9,46,1,0,0,0,11,51,1,0,0,0,13,53,
        1,0,0,0,15,55,1,0,0,0,17,57,1,0,0,0,19,59,1,0,0,0,21,61,1,0,0,0,
        23,64,1,0,0,0,25,69,1,0,0,0,27,74,1,0,0,0,29,30,5,58,0,0,30,31,5,
        61,0,0,31,2,1,0,0,0,32,33,5,112,0,0,33,34,5,114,0,0,34,35,5,105,
        0,0,35,36,5,110,0,0,36,37,5,116,0,0,37,4,1,0,0,0,38,39,5,105,0,0,
        39,40,5,102,0,0,40,6,1,0,0,0,41,42,5,116,0,0,42,43,5,104,0,0,43,
        44,5,101,0,0,44,45,5,110,0,0,45,8,1,0,0,0,46,47,5,101,0,0,47,48,
        5,120,0,0,48,49,5,105,0,0,49,50,5,116,0,0,50,10,1,0,0,0,51,52,5,
        42,0,0,52,12,1,0,0,0,53,54,5,47,0,0,54,14,1,0,0,0,55,56,5,43,0,0,
        56,16,1,0,0,0,57,58,5,45,0,0,58,18,1,0,0,0,59,60,5,40,0,0,60,20,
        1,0,0,0,61,62,5,41,0,0,62,22,1,0,0,0,63,65,7,0,0,0,64,63,1,0,0,0,
        65,66,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,24,1,0,0,0,68,70,7,
        1,0,0,69,68,1,0,0,0,70,71,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,
        26,1,0,0,0,73,75,7,2,0,0,74,73,1,0,0,0,75,76,1,0,0,0,76,74,1,0,0,
        0,76,77,1,0,0,0,77,78,1,0,0,0,78,79,6,13,0,0,79,28,1,0,0,0,4,0,66,
        71,76,1,6,0,0
    ]

class LogosLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    ID = 12
    INT = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'print'", "'if'", "'then'", "'exit'", "'*'", "'/'", 
            "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "ID", "INT", "WS" ]

    grammarFileName = "Logos.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


