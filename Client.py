from QueuingSystem import *
from math import log
from random import random
from queue import Queue
import numpy as np

def foo():
    return -log(1-random())/5

m = 3
serviceQueues = [ServiceQueue(size=1000) for i in range(m)]

serviceDevices = [ServiceDevice(foo) for i in range(m+1)]

def switchFunction(queues):
    indexOfMax = 0
    max = queues[0].size()
    for i in range(len(queues)):
        if queues[i].size() > max:
            indexOfMax = i
            max = queues[i].size()
    return len(queues) if max == 0 else indexOfMax


#['000', '001', '002', '010', '011', '012', '020', '021', '022', '100', '101', '102', '110',
#  '111', '112', '120', '121', '122', '200', '201', '202', '210', '211', '212', '220', '221', '222']


partitions = [[0.25, 0.25, 0, 0.25, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0.25, 0.25, 0, 0.25, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0.25, 0.25, 0, 0.25, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]



queuingSystem = QueuingSystem(serviceQueues, serviceDevices,switchFunction, partitions)

QTheory = queuingSystem.calculateQTheory()

print(QTheory)

queuingSystem.execute(100000)

Q = queuingSystem.Q

w,v = np.linalg.eig(np.eye(3) - Q)
print(Q)
print(w)


print(queuingSystem.getNumberOfReqsInQueues())

print(queuingSystem.getAmountOfTacts())

print(queuingSystem.getTimeOfWork())




