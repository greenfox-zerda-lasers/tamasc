# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods

class Stack():
    stack = []

    def push(self, element):
        self.stack = self.stack + [element]

    def pop(self):
        last_element = self.stack[-1]
        self.stack = self.stack[:-1]
        return last_element

    def size(self):
        z = 0
        for i in self.stack:
            z += 1
        return z

h = Stack()
h.push(3)
h.push(4)
h.push(5)
h.pop()
h.push(6)
h.push(7)
h.push(8)
h.pop()
h.pop()
x=h.pop()

print(x)
print(h.size())
print(h.stack)
