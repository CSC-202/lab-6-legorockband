class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Queue:
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


def initialize() -> Queue:
    return Queue()


def isEmpty(data: Queue) -> bool:
    return data.first == None


def enqueue(data: Queue, value: int) -> Queue:
    def helper(v: Node):
        new_node = Node(value, v.next)
        v.next = new_node
        return data
    if isEmpty(data):
        data.first = Node(value, None)
        return data
    else:
        return helper(data.first)
        

def dequeue(data: Queue) -> tuple[Node, Queue]:
    def helper(v: Node):
        v = data.first
        data.first = v.next
        return v, data
    if isEmpty(data):
        return None
    else:
        return helper(data)


def peek(data: Queue) -> Node:
    return data.first.value


def clear(data: Queue) -> Queue:
    data.first = None
    return data