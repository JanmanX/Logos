from IL import *
from consts import REGISTER_SIZE
from utils.graph import Graph


def lists_of_sets_equal(l1, l2):
    if len(l1) != len(l2):
        return False

    for set1, set2 in zip(l1, l2):
        if set1 != set2:
            return False

    return True


def get_gen(instruction: Instruction) -> set:
    # Iterate over types of instruction
    if isinstance(instruction, InstructionLabel):
        return set()
    elif isinstance(instruction, InstructionAssign):
        if isinstance(instruction.src, AtomId):
            return {instruction.src.id}
        else:
            return set()
    elif isinstance(instruction, InstructionAssignBinop):
        s = set()
        if isinstance(instruction.left, AtomId):
            s.add(instruction.left.id)
        if isinstance(instruction.right, AtomId):
            s.add(instruction.right.id)
        return s
    elif isinstance(instruction, InstructionAssignFromMem):
        if isinstance(instruction.atom, AtomId):
            return {instruction.atom.id}
    elif isinstance(instruction, InstructionAssignToMem):
        if isinstance(instruction.dest, AtomId):
            return {instruction.dest.id}
    elif isinstance(instruction, InstructionGoto):
        return set()
    elif isinstance(instruction, InstructionIf):
        if isinstance(instruction.atom, AtomId):
            return {instruction.atom.id}
        else:
            return set()
    elif isinstance(instruction, InstructionReturn):
        if isinstance(instruction.atom, AtomId):
            return {instruction.atom.id}
        else:
            return set()

    return set()


def get_kill(instruction: Instruction):
    # Iterate over types of instruction
    if isinstance(instruction, InstructionLabel):
        return set()
    elif isinstance(instruction, InstructionAssign):
        return {instruction.dest.id}
    elif isinstance(instruction, InstructionAssignBinop):
        return {instruction.dest.id}
    elif isinstance(instruction, InstructionAssignFromMem):
        return {instruction.dest.id}
    elif isinstance(instruction, InstructionAssignToMem):
        return set()
    elif isinstance(instruction, InstructionGoto):
        return set()
    elif isinstance(instruction, InstructionIf):
        if isinstance(instruction.atom, AtomId):
            return {instruction.atom.id}
        return set()
    elif isinstance(instruction, InstructionReturn):
        if isinstance(instruction.atom, AtomId):
            return {instruction.atom.id}
        return set()

    return set()


def get_in(gen: set, out: set, kill: set):
    # gen[i] U (out[i] \ kill[i])
    return gen.union(out.difference(kill))


def get_out(succ: set, live_in: list):
    # U_{j in succ} in[j]
    return set().union(*[live_in[j] for j in succ])


def get_successors(instructions: list):
    successors = [set() for _ in range(len(instructions))]

    for i, instruction in enumerate(instructions):
        if isinstance(instruction, InstructionGoto):
            for j, instruction2 in enumerate(instructions):
                if isinstance(instruction2, InstructionLabel) and instruction2.label_id == instruction.label_id:
                    successors[i] = {j}
                    break
        elif isinstance(instruction, InstructionIf):
            _succ = set()

            # Find the instruction with the label and get the index
            for j, instruction2 in enumerate(instructions):
                if isinstance(instruction2, InstructionLabel) and instruction2.label_id == instruction.true_label:
                    _succ.add(j)
                    break

            for j, instruction2 in enumerate(instructions):
                if isinstance(instruction2, InstructionLabel) and instruction2.label_id == instruction.false_label:
                    _succ.add(j)
                    break

            successors[i] = _succ

        elif isinstance(instruction, InstructionReturn):
            successors[i] = set()

        else:
            successors[i] = {i + 1}

    return successors


# Calculates interference graph for a program.
def get_interference_graph(
        instructions: list[Instruction],
        kill: list[set],
        out: list[set]) -> Graph:
    edges = []

    # A variable x interferes with a variable y if x != y and there is an
    # instruction i such that x in kill[i], y in out[i], and instruction i is not x = y
    for i, instruction in enumerate(instructions):
        # Iterate over combination of variables in kill[i] and out[i]
        for x in kill[i]:
            for y in out[i]:
                if (x != y
                        and not (isinstance(instruction, InstructionAssign)
                                 and instruction.dest.id == y
                                 and instruction.src.id == x)):
                    edges.append((x, y))

    return Graph.from_edges(edges)


def simplify(graph: Graph, N: int) -> list[tuple]:
    _graph = graph.copy()
    stack = []

    # Create a dictionary with the degree of each node
    degrees = {node: len(_graph.get_neighbours(node)) for node in _graph.nodes}

    # Sort by degree
    degrees = dict(sorted(degrees.items(), key=lambda item: item[1]))

    # To improve our chances of coloring, we try to first select nodes with degree < N
    nodes_with_degree_geq_N = [node for node, degree in degrees.items() if degree >= N]
    nodes_with_degree_lt_N = [node for node, degree in degrees.items() if degree < N]

    # Put node with degree < N on the stack
    for node in nodes_with_degree_lt_N:
        stack.append((node, _graph.get_neighbours(node)))

        # Remove node from graph
        _graph.remove_node(node)

    # Put the rest of the nodes on the stack. These will be spilled later
    for node in nodes_with_degree_geq_N:
        stack.append((node, _graph.get_neighbours(node)))

        # Remove node from graph
        _graph.remove_node(node)

    return stack


def select(stack: list[tuple], N):
    available_colors = set(range(N))
    colors = {}

    while stack:
        node, neighbours = stack.pop()
        colors_taken = {colors[neighbour] for neighbour in neighbours if neighbour in colors}

        # Assign color
        candidate_colors = available_colors.difference(colors_taken)

        if len(candidate_colors) == 0:
            colors[node] = 'spill'
        else:
            colors[node] = candidate_colors.pop()

    return colors


def color_graph(graph: Graph, N: int) -> dict:
    stack = simplify(graph, N)
    colors = select(stack, N)

    return colors


def spill_registers(instructions: list[Instruction], variables: set[str], live_in: list[set], live_out: list[set]):
    instructions_updated = instructions.copy()

    for variable in variables:
        # 1. choose an address to store the variable address_x
        address_entry = StackEntry(f"address_{variable}", 0, REGISTER_SIZE)

        # 2. n every instruction i that reads or assigns x, we locally in this instruction
        #   rename x to x_i
        for i, instruction in enumerate(instructions):
            variable_replacement = f"{variable}_{i}"

            if isinstance(instruction, InstructionAssign):
                if instruction.dest.id == variable:
                    instruction.dest.id = variable_replacement
                if isinstance(instruction.src, AtomId) and instruction.src.id == variable:
                    instruction.src.id = variable_replacement

            elif isinstance(instruction, InstructionAssignBinop):
                if instruction.dest.id == variable:
                    instruction.dest.id = variable_replacement
                if isinstance(instruction.left, AtomId) and instruction.left.id == variable:
                    instruction.left.id = variable_replacement
                if isinstance(instruction.right, AtomId) and instruction.right.id == variable:
                    instruction.right.id = variable_replacement

        # 3. before an instruction i that reads x_i, insert the instruction x_i = MEM[address_x]
        for i, instruction in enumerate(instructions):
            variable_replacement = f"{variable}_{i}"

            if isinstance(instruction, InstructionAssign):
                if isinstance(instruction.src, AtomId) and instruction.src.id == variable_replacement:
                    instructions_updated.insert(i, InstructionAssignFromMem(instruction.src, address_entry))

            elif isinstance(instruction, InstructionAssignBinop):
                if isinstance(instruction.left, AtomId) and instruction.left.id == variable_replacement:
                    instructions_updated.insert(i, InstructionAssignFromMem(instruction.left, address_entry))
                if isinstance(instruction.right, AtomId) and instruction.right.id == variable_replacement:
                    instructions_updated.insert(i, InstructionAssignFromMem(instruction.right, address_entry))

        # 4. after an instruction i that assigns x_i, insert the instruction MEM[address_x] = x_i
        for i, instruction in enumerate(instructions):
            variable_replacement = f"{variable}_{i}"

            if isinstance(instruction, InstructionAssign):
                if instruction.dest.id == variable_replacement:
                    instructions_updated.insert(i + 1, InstructionAssignToMem(address_entry, instruction.dest))

            elif isinstance(instruction, InstructionAssignBinop):
                if instruction.dest.id == variable_replacement:
                    instructions_updated.insert(i + 1, InstructionAssignToMem(address_entry, instruction.dest))

        # 5. If x is live at the start of the program, add an instruction M[addressx] := x
        #   to the start of the program. Note that we use the original name for x here.
        if variable in live_in[0]:
            instructions_updated.insert(0, InstructionAssignToMem(address_entry, AtomId(variable)))

        # 6. If x is live at the end of the program, add an instruction x := M[address_x] to
        #   the end of the program. Note that we use the original name for x here.
        if variable in live_out[-1]:
            instructions_updated.append(InstructionAssignFromMem(AtomId(variable), address_entry))

    return instructions_updated


def get_live_in_out(instructions: list, successors: list[set], gen: list[set], kill: list[set]):
    live_in = [{} for _ in instructions]
    live_out = [{} for _ in instructions]

    # Iterate
    prev_live_in = None
    prev_live_out = None

    iter_number = 0
    while not (live_in == prev_live_in
               and live_out == prev_live_out):
        prev_live_out = list(live_out)
        prev_live_in = list(live_in)

        for i, instruction in reversed(list(enumerate(instructions))):
            live_out[i] = get_out(successors[i], live_in)
            live_in[i] = get_in(gen[i], live_out[i], kill[i])

        # Limit number of iterations
        iter_number += 1
        if iter_number > 10:
            raise Exception("Could not converge live_in and live_out")

    return live_in, live_out


def allocate_registers(ritual: Ritual, num_registers=6):
    ritual.instructions.append(InstructionReturn(AtomNum(0)))

    _breakpoint = 0
    while True:
        _breakpoint += 1
        if _breakpoint > 3:
            raise Exception("Could not color program using {} registers".format(num_registers))

        # Successors, indexed by instruction index. These are the instructions that can be reached from the current instruction.
        successors = get_successors(ritual.instructions)

        # List of instructions that may be read from the current instruction
        # eg., gen[i] = {x} means that x is read from instruction i
        gen = [get_gen(instruction) for instruction in ritual.instructions]

        # A set that lists that may be written to by the current instruction
        # eg., kill[i] = set(x,y) means that x and y are written to by instruction i
        kill = [get_kill(instruction) for instruction in ritual.instructions]

        # Get live_in and live_out
        live_in, live_out = get_live_in_out(ritual.instructions, successors, gen, kill)

        # Get inteference graph
        graph = get_interference_graph(ritual.instructions, kill, live_out)

        # Color graph
        colors = color_graph(graph, N=num_registers)

        if 'spill' in colors.values():
            regs = set([variable for variable, color in colors.items() if color == 'spill'])
            ritual.instructions = spill_registers(ritual.instructions, regs, live_in, live_out)
            continue
        else:
            break

    return colors
