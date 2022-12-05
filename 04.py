countContaining = 0
countOverlaping = 0

with open("04input") as file:
    for line in file.readlines():
        line = line.strip().replace(",","-")
        valuesStr = line.split('-')
        values = []
        for x in valuesStr:
            values.append(int(x))
        if (values[0] <= values[2] and values[1]>=values[3]) or (values[0] >= values[2] and values[1]<=values[3]):
            countContaining+=1
            # a1<=ende2
            # ende1 >= anfang2
        if (values[0] <= values[3] and values[1]>=values[2]) or (values[2] <= values[1] and values[3]>=values[0]):
            countOverlaping+=1

print(countContaining)
print(countOverlaping)