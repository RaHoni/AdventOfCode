visited: set[tuple[int, int]] = set()

knots = [(0,0)]*10

def minmax(x1):
    return max(min(x1,1),-1)
def move():
    for x in range(1,len(knots)):
        head = knots[x-1]
        tail = knots[x]
        dx = head[0] - tail[0]
        dy = head[1] - tail[1]
        if abs(dx)>=2 or abs(dy) >=2 :
            knots[x] = (tail[0] + minmax(dx), tail[1] + minmax(dy))


with open("09input") as file:
    for line in file.readlines():
        direction, steps = line.split()
        steps = int(steps)
        for _ in range(steps):
            visited.add(knots[-1])
            if direction == "R":
                knots[0] = (knots[0][0] + 1, knots[0][1])
            elif direction == "L":
                knots[0] = (knots[0][0] - 1, knots[0][1])
            elif direction == "U":
                knots[0] = (knots[0][0], knots[0][1] + 1)
            elif direction == "D":
                knots[0] = (knots[0][0], knots[0][1] - 1)
            move()
            visited.add(knots[-1])
    visited.add(knots[-1])

list = list(visited)
print(len(visited))
