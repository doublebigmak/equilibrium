# alarm
# alarm
# AUTHOR: Maln
# TIME: 04/03/2017
#alarm ??
import time

usertime = input("Input Time > ")
struct_time = time.strptime(usertime,"%H:%M:%S")
#calculate difference between input time and current time

user_hour = struct_time[3]
user_min = struct_time[4]

trigger = 1
while(trigger):
    current_time = list(time.localtime())
    hour = current_time[3]
    minute = current_time[4]
    if user_hour == hour and user_min == minute:
        print("Ding Ding, Alarm triggered!")
        trigger = 0
    else:
        time.sleep(1)
        print("Tick")


    #do function