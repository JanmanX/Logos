from generated import LogosVisitor, LogosParser
from . import *

class ILGenerator(LogosVisitor):
    def visitProg(self, ctx:LogosParser.ProgContext) -> Program:
        self.program = Program()
        self.visitChildren(ctx)

        return self.program


    def visitAssign(self, ctx:LogosParser.AssignContext):
        
        return self.visitChildren(ctx)





