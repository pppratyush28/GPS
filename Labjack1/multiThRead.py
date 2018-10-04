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
countA3 = 0
countA4 = 0
countA5 = 0

def analogRead1():
    global countA1
    global handle
    name = "AIN0"
    result = ljm.eReadName(handle, name)
    countA1 += 1
    print("1",countA1)


def analogRead2():
    global countA2
    global handle
    name = "AIN1"
    result = ljm.eReadName(handle, name)
    countA2 += 1
    print("2",countA2)


def analogRead3():
    global countA3
    global handle
    name = "AIN2"
    result = ljm.eReadName(handle, name)
    countA3 += 1
    tx=time.time()
    ty=time.time()
    while(ty-tx<5):
        ty=time.time()
    print("3",countA3)


def analogRead4():
    global countA4
    global handle
    name = "AIN3"
    result = ljm.eReadName(handle, name)
    countA4 += 1
    print("4",countA4)


def analogRead5():
    global countA5
    global handle
    name = "AIN4"
    result = ljm.eReadName(handle, name)
    countA5 += 1
    tx = time.time()
    ty = time.time()
    while (ty - tx < 5):
        ty = time.time()
    print("5",countA5)



t1=time.time()
t2=time.time()

while True:

    global t1
    global t2

    while t2 - t1 < 10:
        a1 = threading.Thread(target=analogRead1)
        a2 = threading.Thread(target=analogRead2)
        a3 = threading.Thread(target=analogRead3)
        a4 = threading.Thread(target=analogRead4)
        a5 = threading.Thread(target=analogRead5)
        a1.start()
        a2.start()
        a3.start()
        a4.start()
        a5.start()
        t2 = time.time()

    # print("result1", countA1)
    # print("result2", countA2)
    # print("result3", countA3)
    # print("result4", countA4)
    # print("result5", countA5)

ljm.close(handle)