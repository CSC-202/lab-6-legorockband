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
    return data.first == None


def addAtIndex(data: List, index: int, value: int) -> List:
    def helper(v: Node, index: int, i: int):
        if index == 0:
            addToFront(data, value)
            return data
        elif i == index - 1:
            new_node = Node(value, v.next)
            v.next = new_node
            return data
        else:
            return helper(v.next, index, i + 1)
    if isEmpty(data):
        return None
    else:
        return helper(data.first, index, i = 0)


def removeAtIndex(data: List, index: int) -> tuple[Node, List]:
    def helper(v: Node, index: int, i: int):
        if i + 1 == index:
            target: Node = v.next
            v.next = target.next
            return data
        else:
            return helper(v.next, index, i + 1)
    if isEmpty(data):
        return None
    elif index < 0 or index >= len(data):
        raise IndexError('bad')
    else:
        return helper(data.first, index, i = 0)


def addToFront(data: List, value: int) -> List:
    if data.first == None:
        data.first = Node(value, None)
        return data
    else:
        new_node = Node(value, data.first)
        data.first = new_node
        return data


def addToBack(data: List, value: int) -> List:
    def helper(v: Node, i: int):
        if i == len(data) - 1:
            new_node = Node(value, v.next)
            v.next = new_node
            return data
        else:
            return helper(v.next, i + 1)
    if isEmpty(data):
        data.first = Node(value, None)
        return data
    else:
        return helper(data.first,  i = 0)


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
    data.first = None
    return data
