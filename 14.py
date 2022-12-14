import numpy


def minmax(x1):
    return max(min(x1, 1), -1)


lines = []
xValues = [500]
yValues = [0]
with open("14input") as file:
    for line in file.readlines():
        lineValue = []
        for x in line.split(" -> "):
            x = x.split(",")
            xValues.append(int(x[0]))
            yValues.append(int(x[1]))
            lineValue.append((int(x[0]), int(x[1])))
        lines.append(lineValue)
print(lines)

xValues.sort()
yValues.sort()


sizeY = yValues[-1] + 3

minX = 500 - sizeY
sizeX = sizeY*2 + 2

grid = numpy.zeros((sizeX, sizeY), dtype=int)
transformed = grid.transpose()

for x in range(sizeX):
    grid[x, sizeY-1] = 1

for line in lines:
    for i in range(1, len(line)):
        placed = 0
        startX, startY = line[i - 1]
        startX -= minX
        endX, endY = line[i]
        endX -= minX
        print(f"Start: {startX}:{startY} End: {endX}:{endY}")
        dx, dy = endX - startX, endY - startY
        # if dx > 0 and dy > 0:
        print(f"{dx} {dy}")
        if dx != 0:
            for x in range(startX, endX + minmax(dx), minmax(dx)):
                grid[x, startY] = 1
                placed += 1
        else:
            for y in range(startY, endY + minmax(dy), minmax(dy)):
                grid[startX, y] = 1
                placed +=1
        print(placed)

numpy.set_printoptions(linewidth=300, edgeitems=10)
print(transformed)

sands = 1
while True:

    sandX, sandY = (500 - minX, 0)
    while True:
        if grid[sandX, sandY + 1] == 0:
            sandY += 1
        elif grid[sandX - 1, sandY + 1] == 0:
            sandX -= 1
            sandY += 1
        elif grid[sandX + 1, sandY + 1] == 0:
            sandX += 1
            sandY += 1
        else:
            #print(f"{sands}:  {sandX}.{sandY}")
            grid[sandX, sandY] = 2
            if sandX == 500-minX and sandY == 0:
                print(transformed)
                print(sands)
                exit()
            sands += 1
            break
