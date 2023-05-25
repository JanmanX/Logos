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

    # Exit a parse tree produced by LogosParser#print.
    def exitPrint(self, ctx:LogosParser.PrintContext):
        pass

    # Enter a parse tree produced by LogosParser#if.
    def enterIf(self, ctx:LogosParser.IfContext):
        pass

    # Exit a parse tree produced by LogosParser#if.
    def exitIf(self, ctx:LogosParser.IfContext):
        pass

    # Enter a parse tree produced by LogosParser#exit.
    def enterExit(self, ctx:LogosParser.ExitContext):
        reg = self.get_reg(ctx.ID().getText())
        self.code += consts.EXIT_FMT.format(reg=reg)

    # Exit a parse tree produced by LogosParser#exit.
    def exitExit(self, ctx:LogosParser.ExitContext):
        pass

    # Enter a parse tree produced by LogosParser#LeLeqGeGeq.
    def enterLeLeqGeGeq(self, ctx:LogosParser.LeLeqGeGeqContext):
        pass

    # Exit a parse tree produced by LogosParser#LeLeqGeGeq.
    def exitLeLeqGeGeq(self, ctx:LogosParser.LeLeqGeGeqContext):
        pass


    # Enter a parse tree produced by LogosParser#MulDiv.
    def enterMulDiv(self, ctx:LogosParser.MulDivContext):
        pass

    # Exit a parse tree produced by LogosParser#MulDiv.
    def exitMulDiv(self, ctx:LogosParser.MulDivContext):
        pass


    # Enter a parse tree produced by LogosParser#AddSub.
    def enterAddSub(self, ctx:LogosParser.AddSubContext):
        pass

    # Exit a parse tree produced by LogosParser#AddSub.
    def exitAddSub(self, ctx:LogosParser.AddSubContext):
        pass


    # Enter a parse tree produced by LogosParser#LogicalAndOr.
    def enterLogicalAndOr(self, ctx:LogosParser.LogicalAndOrContext):
        pass

    # Exit a parse tree produced by LogosParser#LogicalAndOr.
    def exitLogicalAndOr(self, ctx:LogosParser.LogicalAndOrContext):
        pass


    # Enter a parse tree produced by LogosParser#Id.
    def enterId(self, ctx:LogosParser.IdContext):
        pass

    # Exit a parse tree produced by LogosParser#Id.
    def exitId(self, ctx:LogosParser.IdContext):
        pass


    # Enter a parse tree produced by LogosParser#AndXorOr.
    def enterAndXorOr(self, ctx:LogosParser.AndXorOrContext):
        pass

    # Exit a parse tree produced by LogosParser#AndXorOr.
    def exitAndXorOr(self, ctx:LogosParser.AndXorOrContext):
        pass


    # Enter a parse tree produced by LogosParser#Int.
    def enterInt(self, ctx:LogosParser.IntContext):
        pass

    # Exit a parse tree produced by LogosParser#Int.
    def exitInt(self, ctx:LogosParser.IntContext):
        pass


    # Enter a parse tree produced by LogosParser#EqNeq.
    def enterEqNeq(self, ctx:LogosParser.EqNeqContext):
        pass

    # Exit a parse tree produced by LogosParser#EqNeq.
    def exitEqNeq(self, ctx:LogosParser.EqNeqContext):
        pass

