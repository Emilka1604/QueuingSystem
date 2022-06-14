from operator import ge
from ServiceDevice import ServiceDevice
from ServiceQueue import *
from ServiceDevice import *
from random import random
import numpy as np


class QueuingSystem:
     

    def __init__(self, queues : list[ServiceQueue], devices : list[ServiceDevice], switchFunction, 
                    partitions):
        self.queues = queues
        self.devices = devices
        self.time = 0
        self.switchFunction = switchFunction
        self.partitions = partitions
        self.Q = np.matrix([[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0],], dtype=float)
        self.timeOfWork = [0,0,0,0]
        self.amountOfTacts = [0,0,0,0]


    def getTime(self):
        return self.time

    def execute(self, timeLimit : float):
        while(self.time < timeLimit):
            i = self.switchFunction(self.queues)
            timeOfTact = 0
            if(i != len(self.devices) - 1):
                req = self.queues[i].get()
                timeOfTact += self.devices[i].execute()
                self._loadServiceQueues(i)
            else:
                timeOfTact += self.devices[i].execute()
            self.time += timeOfTact
            self.timeOfWork[i] += timeOfTact
            self.amountOfTacts[i] += 1
        for j in range(3):
            if self.amountOfTacts[j] != 0:
                self.Q[j] = self.Q[j] / self.amountOfTacts[j]


    def _loadServiceQueues(self, index : int):
        threads = self._generate(index)
        self.Q[index] += threads
        for i in range(len(threads)):
            for _ in range(threads[i]):
                self.queues[i].put(Requirement(self.time))

    
    def _generate(self, index):
        dot = random()
        i = 0
        sum = 0
        while self.partitions[index][i] + sum < dot:
            sum += self.partitions[index][i]
            i += 1
        return self._from_10_to_3(i)

    
    def _from_10_to_3(self, num_):
        num = num_
        new_num = ''
        while num > 0:
            new_num = str(num % 3) + new_num
            num //= 3
        while len(new_num) < 3:
            new_num = "0"+new_num
        return [int(ch) for ch in list(new_num)]


    def calculateQTheory(self):
        QTheory = np.matrix([[0,0,0],[0,0,0],[0,0,0]], dtype=float)
        for i, partition in enumerate(self.partitions):
            for j, elem in enumerate(partition):
                QTheory[i] += np.matrix(self._from_10_to_3(j)) * elem
        return QTheory


    def getNumberOfReqsInQueues(self):
        return [queue.size() for queue in self.queues]

    def getQ(self):
        return self.Q

    def getAmountOfTacts(self):
        return self.amountOfTacts
    
    def getTimeOfWork(self):
        return self.timeOfWork
                

    


    


