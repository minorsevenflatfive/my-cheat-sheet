class Stack:

    def __init__(self):
        self.data = []

    def pop(self):
        if self.isEmpty():
            return 'empty!'
        else:
            element = self.data[-1]
            self.data = self.data[:-1]
            return element

    def push(self, val):
        self.data.append(val)
    
    def peek(self):
        return self.data[-1]
    
    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False