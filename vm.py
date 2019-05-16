class VirtualMachine:
    def __init__(self):
        self.PC = 0
        self.stack = []
        self.curr = None
        self.registers = []

    def next_line(self):
        self.PC += 1


f = open("test", "r")
lines = f.readlines()
labelMap = {}
blocks = {}
for idx in range(len(lines)):
    line = lines[idx]
    line = line.split("\n")[0]
    lines[idx] = line
    if line.endswith(":"):
        labelMap[line.split(":")[0]] = idx
pc = 0

vm = VirtualMachine()

ins = [1, 2, 3]
outs = []
ins.reverse()
curr = None

jumpCmds = ["JUMP", "JUMPZ", "JUMPN"]

while pc < len(lines):
    line = lines[pc]
    if line.endswith(":"):
        pc += 1
        continue
    if line == "INBOX" or line == "OUTBOX":
        if line == "INBOX":
            if len(ins) == 0:
                break
            curr = ins.pop()
        else:
            if curr is None:
                print("error, curr == None")
            else:
                outs.append(curr)
                curr = None
        pc += 1
        continue
    cmd, data = line.split(" ")
    if cmd in jumpCmds:
        if cmd == "JUMP":
            pc = labelMap[data]
            continue
        elif cmd == "JUMPZ":
            if curr == 0:
                pc = labelMap[data]
                continue
        elif cmd == "JUMPN":
            if curr < 0:
                pc = labelMap[data]
                continue
    else:
        data = int(data)
        if cmd == "COPYTO":
            blocks[data] = curr
        elif cmd == "COPYFROM":
            curr = blocks[data]
        elif cmd == "SUB":
            curr = curr - blocks[data]
        elif cmd == "ADD":
            curr += blocks[data]
    pc += 1

print(outs)
