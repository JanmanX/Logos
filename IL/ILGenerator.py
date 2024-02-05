from generated.LogosParser import LogosParser
from generated.LogosVisitor import LogosVisitor
from . import *


class ILGenerator(LogosVisitor):
    def newvar(self):
        name = 't' + str(self._newvar_index)
        self._newvar_index += 1
        return name

    def newlabel(self):
        name = 'l' + str(self._newlabel_index)
        self._newlabel_index += 1
        return name

    def bind(self, table, name, place):
        table[name] = place

    def visitProg(self, ctx:LogosParser.ProgContext):
        rituals = []
        for ritual in ctx.rituals():
            _ritual = self.visitRitual(ritual)
            if _ritual:
                rituals.append(_ritual)

        return Program(
            rituals=rituals,
        )

    # Visit a parse tree produced by LogosParser#ritual.
    def visitRitual(self, ctx:LogosParser.RitualContext):
        id = AtomId(ctx.ID().getText())
        args = [AtomId(x.getText()) for x in ctx.args]

        assert len(args) < 9, "More than 8 arguments are not supported yet."

        self.vtable = dict()
        self.ftable = dict()
        self.place = None
        self.label = None

        # internals
        self._newvar_index = 0
        self._newlabel_index = 0

        instructions = []
        for stmt in ctx.stmts:
            _instructions = self.visit(stmt)
            if _instructions:
                instructions += _instructions

        return Ritual(
            id=id,
            args=args,
            data=[],
            instructions=instructions,
            variable_colors={}
        )

    def visitAssign(self, ctx: LogosParser.AssignContext):
        id = ctx.ID().getText()

        # If id not in vtable, add it
        if id not in self.vtable:
            x = self.newvar()
            self.bind(self.vtable, id, x)
        else:
            x = self.vtable[id]

        # Set place
        self.place = self.newvar()
        place = self.place  # I need to do this because self.place will be changed by visit(ctx.expr())

        # Visit expression
        code = self.visit(ctx.expr())

        # Add assignment instruction
        return code + [InstructionAssign(AtomId(x), AtomId(place))]

    def visitAllocMem(self, ctx:LogosParser.AllocMemContext):
        code = []

        # If id not in vtable, add it
        id = ctx.ID().getText()
        if id not in self.vtable:
            x = self.newvar()
            self.bind(self.vtable, id, x)
        else:
            x = self.vtable[id]

        # Calculate stack offset
        size = int(ctx.INT().getText())
        stack_offset = self.stack_offset
        self.stack_offset += int(ctx.INT().getText())

        code = [
            InstructionAllocMem(dest=AtomId(x), stack_offset=stack_offset, size=size),
            InstructionAssign(dest=AtomId(x), src=AtomId(x))
        ]

        return code


    def visitWriteMem(self, ctx:LogosParser.WriteMemContext):
        return self.visitChildren(ctx)


    def visitReadMem(self, ctx:LogosParser.ReadMemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LogosParser#MulDiv.
    def visitMulDiv(self, ctx: LogosParser.MulDivContext):
        place0 = self.place

        # Visit left
        place1 = self.newvar()
        self.place = place1
        code1 = self.visit(ctx.expr(0))

        # Visit right
        place2 = self.newvar()
        self.place = place2
        code2 = self.visit(ctx.expr(1))

        # Add instruction
        op = Binop.MUL if ctx.op.type == LogosParser.OP_MUL else Binop.DIV
        code = code1 + code2 + [InstructionAssignBinop(AtomId(place0), op, AtomId(place1), AtomId(place2))]
        return code

    # Visit a parse tree produced by LogosParser#AddSub.
    def visitAddSub(self, ctx: LogosParser.AddSubContext):
        place0 = self.place

        # Visit left
        place1 = self.newvar()
        self.place = place1
        code1 = self.visit(ctx.expr(0))

        # Visit right
        place2 = self.newvar()
        self.place = place2
        code2 = self.visit(ctx.expr(1))

        # Add instruction
        op = Binop.ADD if ctx.op.type == LogosParser.OP_ADD else Binop.SUB
        code = code1 + code2 + [InstructionAssignBinop(AtomId(place0), op, AtomId(place1), AtomId(place2))]
        return code

    # Visit a parse tree produced by LogosParser#LeLeqGeGeq.
    def visitLeLeqGeGeq(self, ctx: LogosParser.LeLeqGeGeqContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LogosParser#EqNeq.
    def visitEqNeq(self, ctx: LogosParser.EqNeqContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LogosParser#LogicalAndOr.
    def visitLogicalAndOr(self, ctx: LogosParser.LogicalAndOrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LogosParser#AndXorOr.
    def visitAndXorOr(self, ctx: LogosParser.AndXorOrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LogosParser#Int.
    def visitInt(self, ctx: LogosParser.IntContext):
        return [InstructionAssign(AtomId(self.place), AtomNum(ctx.INT().getText()))]

    # Visit a parse tree produced by LogosParser#Id.
    def visitId(self, ctx: LogosParser.IdContext):
        id = ctx.ID().getText()
        x = self.vtable[id]

        return [InstructionAssign(AtomId(self.place), AtomId(x))]

    # Visit a parse tree produced by LogosParser#if.
    def visitIf(self, ctx: LogosParser.IfContext):
        label1 = self.newlabel()
        label2 = self.newlabel()

        # Visit condition
        place1 = self.newvar()
        self.place = place1
        code_cond = self.visit(ctx.expr())

        # Visit stmt
        code_stmts = []
        for stmt in ctx.stmts:
            code_stmt = self.visit(stmt)
            if code_stmt:
                code_stmts.extend(code_stmt)

        # Combine
        code = []
        code.extend(code_cond)
        code.append(InstructionIf(AtomId(place1), AtomId(label1), AtomId(label2)))
        code.append(InstructionLabel(AtomId(label1)))
        code.extend(code_stmts)
        code.append(InstructionLabel(AtomId(label2)))
        return code


    # Visit a parse tree produced by LogosParser#while.
    def visitWhile(self, ctx: LogosParser.WhileContext):
        label_cond = self.newlabel()
        label_body = self.newlabel()
        label_end = self.newlabel()

        # Visit condition
        place1 = self.newvar()
        self.place = place1
        code_cond = self.visit(ctx.expr())

        # Visit stmt
        code_stmts = []
        for stmt in ctx.stmts:
            code_stmt = self.visit(stmt)
            if code_stmt:
                code_stmts.extend(code_stmt)

        # Combine
        code = []
        code.append(InstructionLabel(AtomId(label_cond)))
        code.extend(code_cond)
        code.append(InstructionIf(AtomId(place1), AtomId(label_body), AtomId(label_end)))
        code.append(InstructionLabel(AtomId(label_body)))
        code.extend(code_stmts)
        code.append(InstructionGoto(AtomId(label_cond)))
        code.append(InstructionLabel(AtomId(label_end)))
        return code
