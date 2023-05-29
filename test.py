import a_recursive_list as List
import b_recursive_stack as Stack
import c_recursive_queue as Queue

l = List.initialize()

l = List.addToBack(l, 2)
l = List.addToFront(l, 0)
l = List.addAtIndex(l, 0, 1)
l = List.addAtIndex(l, 1, 3)
l = List.addToFront(l, 9)
l = List.addAtIndex(l, 1, 2)
l = List.addAtIndex(l, 3, 5)
l = List.addToBack(l, 2)

# l = List.removeAtIndex(l, 4)
print('List = ', l.toPythonList())
# [9, 2, 1, 5, 3, 0, 2, 2]

# get = List.getElementAtIndex(l, 2)
# print(get.value)

l = Stack.push(l, 10)
v, l = Stack.pop(l)
print(v.value)
print(l.toPythonList())


l = Queue.enqueue(l, -5)
l = Queue.enqueue(l, 8)
print(l.toPythonList())

