import time, datetime

time_list = [None]*16
deltatime_list = [None]*16
for i in range(0x10):
    input()
    time_list[i] = time.time()
    if i>=1: deltatime_list[i-1] = time_list[i]-time_list[i-1]
print(deltatime_list)