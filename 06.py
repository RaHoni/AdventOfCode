wagon = []
messageWagon = []
counter = 0
foundPackage = False

with open("06input") as file:
    for char in file.readline():
        wagon.append(char)
        messageWagon.append(char)
        counter+=1
        if len(wagon) >4:
            wagon.pop(0)
        if len(messageWagon) > 14:
            messageWagon.pop(0)

        if len(set(wagon)) == 4 and not foundPackage:
            print(f'Found start {wagon} with last index: {counter}')
            foundPackage = True
        if len(set(messageWagon)) == 14:
            print(f'Found message start {messageWagon} with last index: {counter}')
            break