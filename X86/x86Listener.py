from . import consts
from generated.LogosParser import LogosParser
from generated.LogosListener import LogosListener

class X86Listener(LogosListener):

    def __init__(self) -> None:
        super().__init__()

        self.code = ""
        self.regs = {
            "r8": "",
            "r9": "",
            "r10": "",
            "r11": "",
            "r12": "",
            "r13": "",
            "r14": "",
            "r15": "",

            # Not sure if I should use these registers for now
            # Perhaps system allocated?
#            "rax": "",
#            "rbx": "",
#            "rcx": "",
#            "rdx": "",
#            "rsi": "",
#            "rdi": "",


        }

    def get_reg(self, id):
        # Check if the ID is already allocated
        for reg in self.regs:
            if self.regs[reg] == id:
                return reg

        # Allocate a register for the ID
        for reg in self.regs:
            if self.regs[reg] == "":
                self.regs[reg] = id
                return reg

        raise Exception("No registers available")


    # Enter a parse tree produced by LogosParser#prog.
    def enterProg(self, ctx:LogosParser.ProgContext):
        self.code += consts.PROG_START

    # Exit a parse tree produced by LogosParser#prog.
    def exitProg(self, ctx:LogosParser.ProgContext):
        self.code += consts.PROG_END


    # Enter a parse tree produced by LogosParser#assign.
    def enterAssign(self, ctx:LogosParser.AssignContext):
        # Get the ID and allocate a register for it
        id = ctx.ID().getText()
        reg = self.get_reg(id)
        self.code += consts.ASSIGN_FMT.format(reg=reg, val=ctx.expr().getText())

    # Exit a parse tree produced by LogosParser#assign.
    def exitAssign(self, ctx:LogosParser.AssignContext):
        pass

    # Enter a parse tree produced by LogosParser#print.
    def enterPrint(self, ctx:LogosParser.PrintContext):
        reg = self.get_reg(ctx.ID().getText())
        self.code += consts.PRINT_FMT.format(reg=reg)
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

