from labjack import ljm
import time
import threading

handle = ljm.openS("ANY", "ANY", "ANY")
info = ljm.getHandleInfo(handle)
print("Opened a LabJack with Device type: %i, Connection type: %i,\n"
      "Serial number: %i, IP address: %s, Port: %i,\nMax bytes per MB: %i" %
      (info[0], info[1], info[2], ljm.numberToIP(info[3]), info[4], info[5]))

countA1 = 0
countA2 = 0

def analogRead1():
    global countA1
    global handle
    name = "AIN0"
    result = ljm.eReadName(handle, name)
    countA1 += 1
    time.sleep(15)
    print(result)

def analogRead2():
        global countA2
        global handle
        name = "AIN1"
        result = ljm.eReadName(handle, name)
        countA2 += 1
        print(result)

t1=time.time()
t2=time.time()

#while True:

    global t1
    global t2

    while t2 - t1 < 10:
        a1 = threading.Thread(target=analogRead1)
        a2 = threading.Thread(target=analogRead2)
        a1.start()
        a2.start()
        t2 = time.time()

ljm.close(handle)