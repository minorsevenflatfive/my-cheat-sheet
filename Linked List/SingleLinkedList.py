class Node:

    def __init__(self, val):
        self.next = None
        self.val = val

    def addNode(self, val):
        new_node = Node(val)
        this = self
        while(this.next != None):
            this = this.next
        this.next = new_node