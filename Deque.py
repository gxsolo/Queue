class Deque:

    def __init__(self):
        self.deque = []
        self.len_deque = 0
    def push_front (self,conteudo):
        self.deque.insert(0,conteudo)
        self.len_deque += 1
    def push_back (self,conteudo):
        self.deque.append(conteudo)
        self.len_deque +=1
    def pop_front (self):
        if not self.empty():
            self.deque.pop(0)
            self.len_deque -= 1
    def pop_back (self):
        if not self.empty():
            self.deque.pop(self.len_deque - 1)
            self.len_deque -= 1
    def empty (self):
        if self.len_deque == 0:
            return True
        return False
    def front (self):
        if not self.empty():
            return self.deque[0]
    def back (self):
        if self.len_deque != 0:
            return self.deque[-1]
    def lenght (self):
        return self.len_deque
    def show (self):
        for c in self.deque:
            print(c, end=' | ')
        
