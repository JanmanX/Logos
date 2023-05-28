from antlr4 import ParseTreeVisitor

from . import consts
from generated.LogosParser import LogosParser
from generated.LogosListener import LogosListener

from generated.LogosVisitor import LogosVisitor


class X86Visitor(LogosVisitor):

    def __init__(self) -> None:
        super().__init__()

        self.regs = {
            "r8": "",
            "r9": "",
            "r10": "",
            "r11": "",
            "r12": "",
            "r13": "",
            "r14": "",
            "r15": "",
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

    # Visit a parse tree produced by LogosParser#print.
    def visitPrint(self, ctx:LogosParser.PrintContext):
        return "AAAA"
        return self.visitChildren(ctx)

    def visitTerminal(self, ctx):
        # The `EOF` will now return this instead of `None`
        return '???'


    # Visit a parse tree produced by LogosParser#assign.
    def visitAssign(self, ctx:LogosParser.AssignContext):
        print("Visit Assign")
        reg = self.get_reg(ctx.ID().getText())

        expr = self.visit(ctx.expr())

        return "AAAA"

    # Visit a parse tree produced by LogosParser#AddSub.
    def visitAddSub(self, ctx:LogosParser.AddSubContext):
        return "AddSub"
        # Code I want to generate:
        # push rax
        # left = "mov rax, <left>"
        # push rax
        # right = "mov rax, <right>"
        # pop rbx
        # add rax, rbx

        code = """
        push rax
        """

        left = self.visit(ctx.expr(0))
        code += f"""
        {left}

        push rax
        """

        right = self.visit(ctx.expr(1))
        code += f"""
        {right}
        """

        op = ctx.op.text
        if op == '+':
            code += """
                pop rbx         ; left is in RBX
                add rax, rbx    ; add right to left
            """
        elif op == '-':
            code += """
                pop rbx         ; left is in RBX
                add rax, rbx    ; add right to left
            """

        return code
