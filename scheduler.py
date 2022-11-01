
from timer import Timer

class Scheduler:
    listReadyProcess = []


    def __init__(self):


    def checkProcessReady(self, process):
        #see if int timer function
        #used to cmp with arrival time
        if process.arrival



    def divideQuantumTime(self, t):
        self.quantum = t
        #divide
        #verify that it divides with users first then process

    def readyProcess(self):
        #????

    def rearrangeQueues(self):
        #?????


    #threads

    def arrivalProcess(self):
        #change process state to ready

    def runProcess(self):
        #change state to running

    def pauseProcess(self):
        #change state to pause

    def resumeProcess(self):
        #change state to resume
        #then to running

    def terminateProcess(self):
        #terminate if process burst time is over
        #change state to finished