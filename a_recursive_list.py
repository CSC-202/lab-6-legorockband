class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class List:
    first: Node
    last: Node

    def __init__(self):
        self.first = None
        self.last = None

    def __len__(self):
        n: int = 0
        current = self.first
        while current != None:
            n += 1
            current = current.next
        return n

    def toPythonList(self):
        result: list = []
        current = self.first
        while current != None:
            result.append(current.value)
            current = current.next
        return result


def initialize() -> List:
    return List()


def isEmpty(data: List) -> bool:
    raise NotImplementedError("List.isEmpty() not defined")


def addAtIndex(data: List, index: int, value: int) -> List:
    raise NotImplementedError("List.addAtIndex() not defined")


def removeAtIndex(data: List, index: int) -> tuple[Node, List]:
    raise NotImplementedError("List.removeAtIndex() not defined")


def addToFront(data: List, value: int) -> List:
    raise NotImplementedError("List.addToFront() not defined")


def addToBack(data: List, value: int) -> List:
    raise NotImplementedError("List.addToBack() not defined")


def getElementAtIndex(data: List, index: int) -> Node:
    def helper(v: Node, index: int, i: int):
        if i == index:
            return v
        elif i > index:
            raise IndexError('bad')
        else:
            return helper(v.next, index, i + 1)
    if isEmpty(data):
        return None
    elif index < 0 or index >= len(data):
        raise IndexError('bad')
    else:
        return helper(data.first, index, i = 0)



def clear(data: List) -> List:
    raise NotImplementedError("List.clear() not defined")
