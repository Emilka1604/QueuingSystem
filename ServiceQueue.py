import queue
from Requirement import *

class ServiceQueue:

    def __init__(self, size : int):
        self.queue = queue.Queue()
        for i in range(size):
            self.put(Requirement())

    def get(self):
        return self.queue.get()

    def put(self, req : Requirement):
        self.queue.put(req)

    def size(self):
        return self.queue.qsize()
