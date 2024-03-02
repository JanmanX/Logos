from typing import List, Tuple
from generated.LogosParser import LogosParser
from generated.LogosVisitor import LogosVisitor
from . import *


class ILGenerator(LogosVisitor):
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

        parameters = []

        if ctx.ids():
            parameters = [AtomId(x.getText()) for x in ctx.ids().ID()]
            assert len(parameters) < 9, "More than 8 arguments are not supported yet."

        ritual = Ritual(
            name=id,
            params=parameters,
            instructions=[],
            variable_register_map={},
            vtable={},
        )

        self.ritual = ritual
        self.place = None
        self.label = None

        instructions = [
            InstructionLabel(id),
        ]

        # Assign parameters to vtable
        setup_code = []
        for i, p in enumerate(parameters):
            place = self.ritual.lookup(p.id)
            setup_code.append(InstructionAssign(AtomId(place), AtomId(f'arg_{i}'))) 

        instructions.extend(setup_code)

        for stmt in ctx.stmts:
            _instructions = self.visit(stmt)
            if _instructions:
                instructions += _instructions

        ritual.instructions = instructions

        return ritual

    def visitAssign(self, ctx: LogosParser.AssignContext):
        id = ctx.ID().getText()

        # If id not in vtable, add it
        x = self.ritual.lookup(id)

        # Set place
        self.place = self.ritual.newvar()
        place = self.place  # I need to do this because self.place will be changed by visit(ctx.expr())

        # Visit expression
        code = self.visit(ctx.expr())

        # Add assignment instruction
        return code + [InstructionAssign(AtomId(x), AtomId(place))]


    def visitAllocMem(self, ctx:LogosParser.AllocMemContext):
        code = []

        id = ctx.ID().getText()
        x = self.ritual.lookup(id)

        offset = self.ritual.stack_size
        size = int(ctx.INT().getText())
        self.ritual.stack_size = self.ritual.stack_size + size


        code = [
            InstructionAllocMem(dest=AtomId(x), offset=offset, size=size),
        ]

        return code


    def visitWriteMem(self, ctx:LogosParser.WriteMemContext):
        id = ctx.ID().getText()
        x = self.ritual.lookup(id)

        place = self.ritual.newvar()
        self.place = place 
        code_value = self.visit(ctx.value)

        code = code_value + \
            [
                InstructionWriteMem(src=AtomId(place), addr=AtomId(x)),
            ]

        return code


    def visitReadMem(self, ctx:LogosParser.ReadMemContext):
        code = []

        dest = self.ritual.lookup(ctx.dest.text)
        src = self.ritual.lookup(ctx.source.text)

        code = [
            InstructionReadMem(dest=AtomId(dest), addr=AtomId(src)),
        ] 

        return code


    # Visit a parse tree produced by LogosParser#MulDiv.
    def visitMulDiv(self, ctx: LogosParser.MulDivContext):
        place0 = self.place

        # Visit left
        place1 = self.ritual.newvar()
        self.place = place1
        code1 = self.visit(ctx.expr(0))

        # Visit right
        place2 = self.ritual.newvar()
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
        place1 = self.ritual.newvar()
        self.place = place1
        code1 = self.visit(ctx.expr(0))

        # Visit right
        place2 = self.ritual.newvar()
        self.place = place2
        code2 = self.visit(ctx.expr(1))

        # Add instruction
        op = Binop.ADD if ctx.op.type == LogosParser.OP_ADD else Binop.SUB
        code = code1 + code2 + [InstructionAssignBinop(AtomId(place0), op, AtomId(place1), AtomId(place2))]
        return code

    # Visit a parse tree produced by LogosParser#LtLeqGtGeq.
    def visitLtLeqGtGeq(self, ctx:LogosParser.LtLeqGtGeqContext):
        place0 = self.place

        # labels
        label_true = self.ritual.newlabel()
        label_false = self.ritual.newlabel()

        # Visit left
        place1 = self.ritual.newvar()
        self.place = place1
        code1 = self.visit(ctx.expr(0))

        # Visit right
        place2 = self.ritual.newvar()
        self.place = place2
        code2 = self.visit(ctx.expr(1))

        # Get operator
        op = Binop.LT
        if ctx.op.type == LogosParser.OP_LT:
            op = Binop.LT
        elif ctx.op.type == LogosParser.OP_LEQ:
            op = Binop.LEQ
        elif ctx.op.type == LogosParser.OP_GEQ:
            op = Binop.GEQ
        elif ctx.op.type == LogosParser.OP_GT:
            op = Binop.GT

        # Add instruction
        code = []
        code.append(InstructionAssign(AtomId(place0), AtomNum(0)))
        code.extend(code1)
        code.extend(code2)

        code.extend([
            InstructionAssignBinop(AtomId(place0), op, AtomId(place1), AtomId(place2)),            
            InstructionIf(AtomId(place0), AtomId(label_true), AtomId(label_false)),
            InstructionLabel(AtomId(label_true)),
            InstructionAssign(AtomId(place0), AtomNum(1)),
            InstructionLabel(AtomId(label_false)),
        ])

        return code

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
        x = self.ritual.vtable[id]

        return [InstructionAssign(AtomId(self.place), AtomId(x))]

    # Visit a parse tree produced by LogosParser#if.
    def visitIf(self, ctx: LogosParser.IfContext):
        label1 = self.ritual.newlabel()
        label2 = self.ritual.newlabel()

        # Visit condition
        place1 = self.ritual.newvar()
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
        label_cond = self.ritual.newlabel()
        label_body = self.ritual.newlabel()
        label_end = self.ritual.newlabel()

        # Visit condition
        place1 = self.ritual.newvar()
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


    # Visit a parse tree produced by LogosParser#call.
    def visitCall(self, ctx:LogosParser.CallContext):
        place = self.place
        code = []

        target_ritual = ctx.func.text

        # Visit args 
        (code_args, places) = self.visitExprs(ctx.args)

        # Add instruction
        code.extend(code_args)
        code.append(
            InstructionFunctionCall(
                dest=AtomId(place), 
                ritual=AtomId(target_ritual), 
                args=places
                )
        )

        return code


    # Visit a parse tree produced by LogosParser#ids.
    def visitIds(self, ctx:LogosParser.IdsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LogosParser#exprs.
    def visitExprs(self, ctx:LogosParser.ExprsContext) -> Tuple[List[Instruction], List[str]]:
        code_exprs = []
        places = [] 

        if ctx is None:
            return ([], [])

        for expr in ctx.expr():
            self.place = self.ritual.newvar()
            place = self.place
            code_expr = self.visit(expr)

            if code_expr:
                code_exprs.extend(code_expr)
                places.append(AtomId(place))

        return (code_exprs, places)

    # Visit a parse tree produced by LogosParser#return.
    def visitReturn(self, ctx:LogosParser.ReturnContext):
        place = self.ritual.newvar()
        self.place = place
        code = self.visit(ctx.expr())

        return code + [
            InstructionReturn(AtomId(place))
            ]

