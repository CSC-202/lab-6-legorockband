class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack:
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


def initialize() -> Stack:
    return Stack()


def isEmpty(data: Stack) -> bool:
    return data.first == None


def push(data: Stack, value: int) -> Stack:
    def helper(v: Node):
        first = v
        data.first = Node(value, first)
        return data
    if isEmpty(data):
        data.first = Node(value, None)
        return data
    else:
        return helper(data.first)


def pop(data: Stack) -> tuple[Node, Stack]:
    def helper(v: Node):
        v = data.first
        data.first = v.next
        return v, data
    if isEmpty(data):
        return None
    else:
        return helper(data.first)
    


def peek(data: Stack) -> Node:
    return data.first.value


def clear(data: Stack) -> Stack:
    data.first = None
    return data
