import sys

script, file = sys.argv


loops, tape, tapeslct, cmdslct = [], [0], 0, 0
code = open(file)
program = filter(lambda x: x in ['.', ':', ',', ';', '[', ']', '<', '>', '+', '-', '|', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], code.read())
program = list(program)
condparse = 0
condition = []
loop = 0

debug = 0

def execute(cmd):
    global tape
    global tapeslct
    global cmdslct
    global condparse
    global condition
    global debug
    global loop
    if condparse == 1:
        if cmd != "|":
            condition.append(cmd)
            if debug == 1:
                print condition
        else:
            condparse = 0
            cond = int("".join(condition))
            while tape[tapeslct] != cond:
                execute(loop)
    elif cmd == "+":
        tape[tapeslct] += 1
    elif cmd == "-":
        tape[tapeslct] -= 1
    elif cmd == ">":
        tapeslct += 1
        if tapeslct == len(tape):
            tape.append(0)
    elif cmd == "<":
        tapeslct -= 1
    elif cmd == ".":
        sys.stdout.write(chr(tape[tapeslct]))
    elif cmd == ":":
        sys.stdout.write(tape[tapeslct])
    elif cmd == ",":
        tape[tapeslct] = ord(input())
    elif cmd == ";":
        tape[tapeslct] = int(input)
    elif cmd == "[":
        loops.append(cmdslct)
    elif cmd == "]":
        latestloop = len(loops) - 1
        if tape[tapeslct] != 0:
            cmdslct = loops[latestloop]
        else:
            loops.pop(latestloop)
    elif cmd == "|":
        loop = program[cmdslct - 1]
        condition = []
        condparse = 1
    if debug == 1:
        print cmd
        print tape

while len(program) > cmdslct:
    execute(program[cmdslct])
    cmdslct += 1
print "\n"

