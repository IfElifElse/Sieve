import sys

script, file = sys.argv


loops, tape, tapeslct, cmdslct = [], [0], 0, 0
code = open(file)
program = code.read()
stdin = list(input("Input: "))

debug = 0

if debug == 1: print(program)

def execute(cmd):
    global tape
    global tapeslct
    global cmdslct
    if cmd == "+":
        if debug == 1: print"inc"
        tape[tapeslct] += 1
    if cmd == "-":
        if debug == 1: print"dec"
        tape[tapeslct] -= 1
    if cmd == ">":
        if debug == 1: print"right"
        tapeslct += 1
        if tapeslct == len(tape):
            tape.append(0)
    if cmd == "<":
        if debug == 1: print"left"
        tapeslct -= 1
    if cmd == ".":
        if debug == 1: print"outASCII"
        sys.stdout.write(chr(tape[tapeslct]))
    if cmd == ":":
        if debug == 1: print"out"
        sys.stdout.write(tape[tapeslct])
    if cmd == ",":
        if debug == 1: print"inASCII"
        tape[tapeslct] = ord(stdin[0])
        stdin.pop(0)
    if cmd == ";":
        if debug == 1: print"in"
        tape[tapeslct] = int(stdin[0])
        stdin.pop(0)
    if cmd == "[":
        if debug == 1: print"openloop"
        loops.append(cmdslct)
    if cmd == "]":
        if debug == 1: print"closeloop"
        latestloop = len(loops) - 1
        if tape[tapeslct] != 0:
            cmdslct = loops[latestloop]
        else:
            loops.pop(latestloop)
    if cmd == "|":
        if debug == 1: print"sieve"
        sieve = []
        cmdslct += 1
        ctrl = 0
        number = 0
        while program[cmdslct] != "|":
            sieve.append(program[cmdslct])
            cmdslct += 1
        for i in sieve:
            if i == ">":
                ctrl += 1
            if i == "<":
                ctrl -= 1
            if i in "123456789":
                number = 1
                break
        if number == 1:
            until = int("".join(sieve))
        else:
            until = tape[tapeslct + ctrl]
        if debug == 1: print until
        cmdslct += 1
        if program[cmdslct] == "{":
            cmdslct += 1
            func = []
            while program[cmdslct] != "}":
                func.append(program[cmdslct])
                cmdslct += 1
        else:
            func = program[cmdslct]
        while tape[tapeslct] != until:
            if type(func) == type([]):
                for x in func:
                    execute(x)
            else:
                execute(func)
while len(program) > cmdslct:
    execute(program[cmdslct])
    cmdslct += 1
print
