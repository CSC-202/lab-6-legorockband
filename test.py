import a_recursive_list as List
import b_recursive_stack as Stack

l = List.initialize()

l = List.addToFront(l, 0)
l = List.addAtIndex(l, 0, 1)
l = List.addAtIndex(l, 1, 3)
l = List.addAtIndex(l, 1, 2)
l = List.addAtIndex(l, 3, 5)
l = List.addToBack(l, 2)

l = List.removeAtIndex(l, 4)
print(l.toPythonList())


get = List.getElementAtIndex(l, 2)
print(get.value)

# v, l = Stack.pop(l)
# print(v.value)
# print(l.toPythonList())
