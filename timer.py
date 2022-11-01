
import time
#not needed. We can make our own timer

class Timer:
    timer=0;

    while(True):
        time.sleep(1)
        timer+=1

        print(timer)


    #properties func for setter?
    def getTime(self):
        return timer




