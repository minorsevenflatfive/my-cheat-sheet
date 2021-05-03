from Stack import Stack

if __name__ == "__main__":
    s = Stack()
    print(s.isEmpty())
    
    s.push(10)
    print(s.peek())

    print(s.data)
    print(s.pop())
    print(s.pop())