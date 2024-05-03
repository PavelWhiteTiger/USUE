import datetime, time

for i in range(5):
    print(time.strftime('%H:%M:%S', time.localtime()))
    time.sleep(1)