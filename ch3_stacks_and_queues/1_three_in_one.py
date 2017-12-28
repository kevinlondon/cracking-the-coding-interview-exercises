class ArrayMultistack:

    def __init__(self, length, stacks):
        self.data = [None for x in range(length)]
        self.stack_size = length / stacks
        self.stacks = []

        for x in range(stacks):
            index = x * self.stack_size
            self.stacks.append(MiniStack(self.data, index, index+self.stack_size))

        self.stacks[-1].end = length


class MiniStack:

    def __init__(self, all_data, start, end):
        self.end = int(end)
        self.start = int(start)
        self.head = int(start - 1)
        self.all_data = all_data

    def peek(self):
        if not self.is_empty():
            return self.all_data[self.head]
        else:
            return None

    def pop(self):
        if self.head < self.start:
            raise ValueError()
        element = self.all_data[self.head]
        self.all_data[self.head] = None
        self.head -= 1
        return element

    def push(self, item):
        if self.head + 1 >= self.end:
            raise ValueError('Cannot push beyond stack.')
        self.all_data[self.head+1] = item
        self.head += 1

    def is_empty(self):
        return self.head < self.start

array = ArrayMultistack(length=13, stacks=3)
# Testing...
print(array.data)
print(array.stacks[0].peek())
print(array.stacks[0].is_empty())
print(array.stacks[0].head)
[array.stacks[2].push(x) for x in range(5)]
print(array.data)
[array.stacks[1].push(x) for x in range(3)]
print(array.data)
[array.stacks[2].pop() for x in range(4)]
print(array.data)
