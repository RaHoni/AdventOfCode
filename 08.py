import numpy

trees: list[list[int]] = []

with open("08input") as file:
    for line in file.readlines():
        treeline = []
        for tree in line[:-1]:
            treeline.append(int(tree))
        trees.append(treeline)

viewable: set[tuple[int, int]] = set()
nptrees = numpy.array(trees)

for x in range(len(trees)):
    row: list[int] = nptrees[x].tolist()
    column: list[int] = nptrees[:, x].tolist()
    reversedRow = row[::-1]
    reversedColumn = column[::-1]
    initvalue = [1000] * 4
    lastFront, lastBack, lastFrontColumn, lastBackColumn = initvalue
    for i in range(9, -1, -1):
        if i in row:
            currentFront = row.index(i)
            currentBack = reversedRow.index(i)
            if currentFront < lastFront:
                viewable.add((x, currentFront))
                lastFront = currentFront
            if currentBack < lastBack:
                viewable.add((x, len(trees) - 1 - currentBack))
                lastBack = currentBack
        if i in column:
            currentFront = column.index(i)
            currentBack = reversedColumn.index(i)
            if currentFront < lastFrontColumn:
                viewable.add((currentFront, x))
                lastFrontColumn = currentFront
            if currentBack < lastBackColumn:
                viewable.add((len(trees) - 1 - currentBack, x))
                lastBackColumn = currentBack

# printable = list(viewable)
# printable.sort()
# print(printable)
print(len(viewable))
viewdist: list[int] = []
test = numpy.zeros((len(trees),len(trees)),int)

for x in range(len(trees)):
    for y in range(len(trees)):
        row: list[int] = nptrees[x].tolist()
        column: list[int] = nptrees[:, y].tolist()
        high: int = nptrees[x, y]
        left = False
        leftCount = 0
        right = False
        rightCount = 0
        up = False
        upCount = 0
        down = False
        downCount = 0
        for i in range(1, len(trees)):
            left |= y - i < 0
            right |= y + i >= len(trees)
            up |= x - i < 0
            down |= x + i >= len(trees)

            if not left:
                leftCount += 1
                left = row[y - i] >= high
            if not right:
                rightCount += 1
                right = row[y + i] >= high
            if not up:
                upCount += 1
                up = column[x - i] >= high
            if not down:
                downCount += 1
                down = column[x + i] >= high
            if left and right and up and down:
                break
        viewdistance = leftCount * rightCount * upCount * downCount
        test[x,y] = viewdistance

numpy.set_printoptions(edgeitems=10,linewidth=1000)
print(test)


print(test.max())