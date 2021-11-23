import time

class Clock:
    def __init__(self,hours,minutes,seconds,c_type = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.type = c_type

    def __str__(self):
        if self.type == 0:
            print('{:02}:{:02}:{:02}'.format(self.hours,self.minutes,self.seconds))
        if self.type == 1:
            if self.hours < 13:
                print('{:02}:{:02}:{:02} am'.format(self.hours,self.minutes,self.seconds))
            if self.hours > 12:
                print('{:02}:{:02}:{:02} pm'.format(self.hours,self.minutes,self.seconds))
    
    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
            if self.minutes == 60:
                self.hours += 1
                self.minutes = 0
                if self.hours == 25:
                    self.hours = 1
        return self.seconds,self.minutes,self.hours

hours = int(input('What is the current hour ==> '))
minutes = int(input('What is the current minute ==> '))
seconds = int(input('What is the current second ==> '))
clock = Clock(hours,minutes,seconds)
while True:
    clock.__str__()
    clock.tick()
    time.sleep(1)