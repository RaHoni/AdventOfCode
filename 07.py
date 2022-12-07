import abc
from typing import cast


class filesystem():
    name = ""
    parent: dir
    isDir = False

    def toString(self):
        return self.name

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def size(self):
        pass


class file(filesystem):
    filesize: int = 0

    def __init__(self, size: int, name):
        super().__init__(name)
        self.filesize = size

    def size(self):
        return self.filesize


class dir(filesystem):
    childs: dict[str, filesystem]

    isDir = True

    def __init__(self, name):
        self.childs = dict()
        super().__init__(name)

    def addChild(self, child):
        if child.name in self.childs.keys():
            raise EnvironmentError("Trying to override file")
        self.childs[child.name] = child
        child.parent = self

    def getChild(self, name: str):
        child = self.childs[name]
        if child.isDir:
            return cast(dir, child)
        else:
            raise ReferenceError("Not a dir")

    def forChild(self, bedingung, funct, *test):
        for child in self.childs.values():
            if child.isDir:
                child.forChild(bedingung, funct, *test)
            if bedingung(child):
                funct(child, test)

    def size(self):
        size = 0
        for child in self.childs.values():
            size += child.size()
        return size


def maxSize(child: filesystem):
    # print(f"{child.name} has size {child.size()}")
    return child.size() <= 100000 and child.isDir


def add(child: filesystem, *null):
    global valueStepOne
    valueStepOne += child.size()


def isDir(child: filesystem):
    global needToFree
    return child.isDir and child.size() >= needToFree


def appendDir(child: dir, *null):
    global dirs
    dirs.append((child.size(),child.name))


lines = []
commands = []
dirs = list(())
valueStepOne = 0
filesystemSize = 70000000
requiredSpace = 30000000
needToFree = 0

if __name__ == "__main__":
    root: dir = dir("/")
    root.parent = root
    current: dir = root
    with open("07input") as input:
        for line in input.readlines():
            line = line.strip().split(" ")
            if line[0] == "$":
                commands.append(line)
                if line[1] == "cd":
                    if line[2] == "/":
                        current = root
                    elif line[2] == "..":
                        # print(f"{current.name} has parent {current.parent.name}")
                        current = current.parent
                    else:
                        current = current.getChild(line[2])
                elif line[0] == "ls":
                    pass
            else:
                if line[0] == "dir":
                    current.addChild(dir(line[1]))
                else:
                    size = int(line[0])
                    current.addChild(file(size, line[1]))
            lines.append(line)

    root.forChild(maxSize, add)
    print(valueStepOne)
    needToFree = requiredSpace - (filesystemSize-root.size())
    root.forChild(isDir, appendDir)
    dirs.sort()
    print(dirs)
