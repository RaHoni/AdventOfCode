class monky:
    name: str
    parent = ""
    containsHuman = False

    def __init__(self, name):
        self.name = name
        self.parent = self

    def setup(self, monkys, parent):
        pass

    def yell(self):
        return 0

    def resolve(self):
        return 0


def add(left: int, right: int, flip: bool = False):
    value = left + right
    return value


def sub(left: int, right: int, flip: bool = False):
    value = left - right
    return value


def mult(left: int, right: int, flip: bool = False):
    value = left * right
    return value


def div(left: int, right: int, flip: bool = False):
    value = left / right
    return int(value)

def inversDiv(resoved, a, left: bool ):
    value = 0
    if left:
        value = resoved*a
    else:
        value = a/resoved
    return value


class simple(monky):
    number = 0

    def __init__(self, value: int, name):
        super().__init__(name)
        self.number = value

    def setup(self, monkys: dict[str, monky], parent: monky):
        self.parent = parent
        if self.name == "humn":
            self.containsHuman = True
        return self.containsHuman

    def yell(self):
        return self.number

    def resolve(self):
        return self.parent.resolve()


class math(monky):
    left: str
    leftMonkey: monky
    right: str
    rightMonkey: monky
    calc = add
    invers = sub


    def __init__(self, name, left: str, right: str, calc: str):
        super().__init__(name)
        self.left = left
        self.right = right

        if (calc == "+"):
            self.calc = add
            self.invers = sub
        elif (calc == "-"):
            self.calc = sub
            self.invers = add
        elif (calc == "*"):
            self.calc = mult
            self.invers = div
        else:
            self.calc = div
            self.invers = inversDiv

    def setup(self, monkys: dict[str, monky], parent: monky):
        self.parent = parent
        self.leftMonkey = monkys[self.left]
        self.rightMonkey = monkys[self.right]
        left = self.leftMonkey.setup(monkys, self)
        right = self.rightMonkey.setup(monkys, self)
        if left or right:
            self.containsHuman = True
        return self.containsHuman

    def yell(self):
        return self.calc(self.leftMonkey.yell(), self.rightMonkey.yell())

    def resolve(self):
        left = self.leftMonkey.containsHuman
        parent: monky = self.parent

        if self.name == "root":
            if left:
                return self.rightMonkey.yell()
            else:
                return self.leftMonkey.yell()

        parentValue = parent.resolve()
        value = 0
        if left:
            value = self.rightMonkey.yell()
        else:
            value = self.leftMonkey.yell()
        return self.invers(parentValue, value,left)


monkeys: dict[str, monky] = dict()
root: math = math("", "", "", "")

with open("21input") as filr:
    for line in filr.readlines():
        name = line[:4]
        funktion = line[6:-1]
        try:
            number = int(funktion)
            monkeys[name] = simple(number, name)
        except:
            left = funktion[:4]
            right = funktion[-4:]
            calc = funktion[5]
            monkey = math(name, left, right, calc)
            if name == "root":
                root = monkey
            monkeys[name] = monkey

human = monkeys["humn"]
root.setup(monkeys, root)
print(root.yell())

print(f"{root.leftMonkey.containsHuman} {root.rightMonkey.containsHuman}")

value = 0
if root.leftMonkey.containsHuman:
    value = root.leftMonkey.yell()
else:
    value = root.rightMonkey.yell()

print(human.resolve())
