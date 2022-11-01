
class Process:
    def __init__(self, id, arrival, burst):
        self.id = id
        self.arrival = arrival
        self.burst = burst
        self.state = "waiting"
        #current state of process

    #setters??

    #getters??


class UserGroup:
    def __init__(self, name, num):
        self.name = name
        self.num = num
        self.processList = []


    def appendProcesses(self, id, arrival, burst):
        self.processList.append(Process(id, arrival, burst))


    def appendProcesses(self, process):
        self.processList.append(process)

