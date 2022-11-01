
from timer import Timer
from process import Process, UserGroup
from scheduler import Scheduler
from threading import Thread





if __name__ == '__main__':

    time_quan = 4
    dict = {"A":2, "B":1}
    arrival_arr = [4, 1, 5]
    burst_arr = [3, 5, 6]

    # t1 = Timer()
    # t1.resume(3)
    # print(t1.time)
    # t1.resume(5)
    # print(t1.time)

    p0 = Process(0, arrival_arr[0], burst_arr[0])
    p1 = Process(1, arrival_arr[1], burst_arr[1])
    u1 = UserGroup("A", 2)
    u1.appendProcesses(p0)
    u1.appendProcesses(p1)


    p3 = Process(0, arrival_arr[2], burst_arr[2])
    u2 = UserGroup("B", 1)
    u2.appendProcesses(p3)

    t1 = Thread(target=Timer, args=(1,))
    t1.start()
    t1.join()   #when done join



    scheduler = Scheduler()







    #u2 = UserGroup(dict.keys()[1], dict.values()[1])










