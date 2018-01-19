class StackMin:

    def __init__(self):
        self.data = []
        self.mins = []

    def isEmpty(self):
        return len(self.data) == 0

    def peek(self):
        if not self.isEmpty():
            return self.data[-1]

    def pop(self):
        if not self.isEmpty():
            element = self.data.pop()
            if element == self.mins[-1]:
                self.mins.pop()
            return element
        else:
            raise ValueError()

    def min(self):
        if not self.isEmpty():
            return self.mins[-1]

    def push(self, item):
        self.data.append(item)
        if not self.mins or item < self.mins[-1]:
            self.mins.append(item)

    def print_debug(self):
        print('Contents:', self.data)
        print('Mins:', self.mins)

stack = StackMin()
stack.push(10)
stack.push(4)
stack.push(8)
stack.push(6)
stack.push(2)

stack.print_debug()
stack.pop()
stack.print_debug()
stack.pop()
stack.print_debug()
print(stack.min())
