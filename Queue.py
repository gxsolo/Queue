class Queue:

    def __init__(self):
        self.queue = []
        self.len_queue = 0
    def add (self,conteudo):
        self.queue.append(conteudo)
        self.len_queue += 1
    def remove (self):
        if not self.empty():
            self.queue.pop(0)
            self.len_queue -= 1
    def empty (self):
        if self.len_queue == 0:
            return True
        return False
    def front (self):
        if not self.empty():
            return self.queue[0]
        return None
    def rear (self):
        if self.len_queue != 0:
            return self.queue[-1]
        return None
    def lenght (self):
        return self.len_queue
        

