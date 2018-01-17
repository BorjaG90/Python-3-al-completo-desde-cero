import time
import os
import datetime

while(True):
    actual = datetime.datetime.now()
    print("{}:{}:{}".format(actual.hour, actual.minute, actual.second))
    time.sleep(1)
    os.system('cls')