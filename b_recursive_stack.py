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


# Unsure how to change this to recurisive function when there are no for loops 
def push(data: Stack, value: int) -> Stack:
    new_node = Node(value, None)
    if data.first is None:
        data.first = new_node
        return data

    old = data.first
    data.first = new_node
    new_node.next = old
    return data

# Unsure how to change this to recurisive function when there are no for loops 
def pop(data: Stack) -> tuple[Node, Stack]:
    first = data.first
    data.first = first.next
    return first, data


def peek(data: Stack) -> Node:
    return data.first.value


def clear(data: Stack) -> Stack:
    data.first = None
    return data
