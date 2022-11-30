

class Stack:
    def __init__(self):
        self.list_seq = []        

    def is_empty(self):
        return self.size() == 0
        
    def push(self, bracket):
        self.list_seq.append(bracket)

    def pop(self):
        if self.size() > 0:
            return self.list_seq.pop()

    def peek(self):
        if self.size() > 0:
            return self.list_seq[-1]

    def size(self):
        return len(self.list_seq)