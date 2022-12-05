stacks = [[], [], [], [], [], [], [], [], []]
stacks2 = []
stacklines = []

with open("05input") as file:
    lines = file.readlines()
    for line in lines:
        if "1" not in line:
            stacklines.insert(0, line)
        else:
            break
    for line in stacklines:
        lines.remove(line)
        for x in range(9):
            value = line[x*4+1]
            #print(value)
            if " " != value:
                stacks[x].append(value)

    for stack in stacks:
        stacks2.append(stack.copy())# Copy Stacks in to the object for two

    for line in lines[2:]:
        splitLine = line.split()
        moveCount = int(splitLine[1])
        fromStack = int(splitLine[3])-1
        toStack = int(splitLine[5])-1
        for x in range(moveCount):
            stacks[toStack].append(stacks[fromStack].pop())
        craneStack = stacks2[fromStack][-moveCount:]
        for x in range(moveCount):
            stacks2[fromStack].pop()
        stacks2[toStack] += craneStack
    for stack in stacks:
        print(stack[-1], end='')
    print()
    for stack in stacks2:
        print(stack[-1], end='')