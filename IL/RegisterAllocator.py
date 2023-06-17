from IL import *


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
    elif isinstance(instruction, AssignmentAtomInstruction):
        if isinstance(instruction.src, AtomId):
            return {instruction.src.id}
        else:
            return set()
    elif isinstance(instruction, AssignmentBinopInstruction):
        s = set()
        if isinstance(instruction.left, AtomId):
            s.add(instruction.left.id)
        if isinstance(instruction.right, AtomId):
            s.add(instruction.right.id)
        return s
    elif isinstance(instruction, AssignmentFromMemInstruction):
        if isinstance(instruction.atom, AtomId):
            return {instruction.atom.id}
    elif isinstance(instruction, AssignmentToMemInstruction):
        s = {instruction.mem}
        if isinstance(instruction.atom, AtomId):
            s.add(instruction.atom.id)
        return s
    elif isinstance(instruction, GotoInstruction):
        return set()
    elif isinstance(instruction, IfInstruction):
        if isinstance(instruction.atom, AtomId):
            return {instruction.atom.id}
        else:
            return set()
    elif isinstance(instruction, ReturnInstruction):
        if isinstance(instruction.atom, AtomId):
            return {instruction.atom.id}
        else:
            return set()
        

def get_kill(instruction: Instruction):
    # Iterate over types of instruction
    if isinstance(instruction, InstructionLabel):
        return set()
    elif isinstance(instruction, AssignmentAtomInstruction):
        return {instruction.dest.id}
    elif isinstance(instruction, AssignmentBinopInstruction):
        return {instruction.dest.id}
    elif isinstance(instruction, AssignmentFromMemInstruction):
        return {instruction.dest.id}
    elif isinstance(instruction, AssignmentToMemInstruction):
        return set()
    elif isinstance(instruction, GotoInstruction):
        return set()
    elif isinstance(instruction, IfInstruction):
        if isinstance(instruction.atom, AtomId):
            return {instruction.atom.id}
        return set()
    elif isinstance(instruction, ReturnInstruction):
        if isinstance(instruction.atom, AtomId):
            return {instruction.atom.id}
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
        if isinstance(instruction, GotoInstruction):
            for j, instruction2 in enumerate(instructions):
                if isinstance(instruction2, InstructionLabel) and instruction2.label_id == instruction.label_id:
                    successors[i] = {j}
                    break
        elif isinstance(instruction, IfInstruction): 
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
        
        elif isinstance(instruction, ReturnInstruction):
            successors[i] = set()

        else:
            successors[i] = {i+1}

    return successors


# Calculates intereference graph for a program.
def get_interference_graph(
        instructions: list[Instruction], 
        kill: list[set], 
        out: list[set]) -> list[tuple]:
    interference = []

    # A varible x interferes with a variable y if x != y and there is an 
    # instruction i such that x in kill[i], y in out[i], and instruction i is not x = y
    for i, instruction in enumerate(instructions):
        # Iterate over combination of variables in kill[i] and out[i]
        for x in kill[i]:
            for y in out[i]:
                if (x != y 
                    and not (isinstance(instruction, AssignmentAtomInstruction) 
                             and instruction.dest.id == y 
                             and instruction.src.id == x)):

                    interference.append((x, y))

    return interference


def liveness_analysis(program: Program):
    program.instructions.append(ReturnInstruction(AtomNum(0)))

    num_instructions = len(program.instructions)
    print(f"Number of instructions: {num_instructions}")

    # Successors, indexed by instruction index. These are the instructions that can be reached from the current instruction.
    successors = get_successors(program.instructions)

    # List of instructions that may be read from the current instruction
    # eg., gen[i] = {x} means that x is read from instruction i
    gen = [get_gen(instruction) for instruction in program.instructions]

    # A set that lists that may be written to by the current instruction
    # eg., kill[i] = set(x,y) means that x and y are written to by instruction i
    kill = [get_kill(instruction) for instruction in program.instructions]

    # _in[i] holds the variables that are live at the start of i
    live_in = [set() for _ in range(num_instructions)]

    # out[i] holds the variables that are live at the end of i
    live_out = [set() for _ in range(num_instructions)]

    # Iterate
    prev_line_in = []
    prev_line_out = []

    iter_number = 0
    while not (lists_of_sets_equal(live_in, prev_line_in)
               and lists_of_sets_equal(live_out, prev_line_out)):
        prev_line_out = list(live_out)
        prev_line_in = list(live_in)

        for i, instruction in reversed(list(enumerate(program.instructions))):
            live_out[i] = get_out(successors[i], live_in)
            live_in[i] = get_in(gen[i], live_out[i], kill[i])

        # Limit number of iterations
        iter_number += 1
        if iter_number > 10:
            break


    # print the results
    print("Liveness analysis:")
    for i, instruction in enumerate(program.instructions):
        print(f"{i}: out: {live_out[i]}\t\t\t\t\tin: {live_in[i]}")


    # Print interference graph
    print("\nInterference graph:")
    interference = get_interference_graph(program.instructions, kill, live_out)
    print(interference)