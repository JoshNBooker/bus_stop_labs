class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = []
    
    def queue_add(self, name):
        self.queue.append(name)
    
    def queue_clear(self):
        self.queue.clear()
    
