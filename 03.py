chars = "abcdefghijklmnopqrstuvwxyz"
chars += chars.upper()
chars = "0" + chars
score = 0
score2 = 0


def value(char):
    return chars.index(char)


with open("03input") as file:
    for line in file.readlines():
        first = set(line[:int((len(line) - 1) / 2)])
        second = set(line[int((len(line) - 1) / 2):len(line) - 1])
        intersect = first.intersection(second)
        #print(intersect)
        for x in intersect:
            score += value(x)
with open("03input") as file:
    lines = file.readlines()
    print(len(lines))
    for x in range(0,300,3):
        intersect = set(lines[x][:-1])
        intersect = intersect.intersection(lines[x+1])
        intersect = intersect.intersection(lines[x+2])
        for y in intersect:
            score2 += value(y)

print(score)
print(score2)
