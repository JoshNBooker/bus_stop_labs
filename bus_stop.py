class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = []
    
    def queue_add(self, name):
        self.queue.append(name)
        print(f"the queue is now{self.queue}")
    
    def queue_clear(self):
        self.queue.clear()
        if len(self.queue) == 0:
            print("bus stop empty")
    
