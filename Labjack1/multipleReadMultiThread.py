from labjack import ljm
import time
import threading
handle = ljm.openS("ANY", "ANY", "ANY")
info = ljm.getHandleInfo(handle)
print("Opened a LabJack with Device type: %i, Connection type: %i,\n"
      "Serial number: %i, IP address: %s, Port: %i,\nMax bytes per MB: %i" %
      (info[0], info[1], info[2], ljm.numberToIP(info[3]), info[4], info[5]))
#f = open ('sampleWrLP.csv','w+')
countA1=0
countA2=0
#countA3=0
#countA4=0
# countA5=0
# countD1=0
# countD2=0
# countD3=0
# countD4=0
# countD5=0

def analogRead1():
     global countA1
     global handle
     name = "AIN0"
     result = ljm.eReadName(handle, name)
     # print("\n%s reading : %f V" % (name, result))
     countA1 += 1

def analogRead2():
     global countA2
     global handle
     name = "AIN1"
     result = ljm.eReadName(handle, name)
     # print("\n%s reading : %f V" % (name, result))
     countA2 += 1

#def analogRead3():
#      global countA3
#      global handle
#     name = "AIN2"
 #     result = ljm.eReadName(handle, name)
 #     #print("\n%s reading : %f V" % (name, result))
  #    countA3 += 1
#
# def analogRead4():
#       global countA4
#       global handle
#       name = "AIN3"
#       result = ljm.eReadName(handle, name)
#       print("\n%s reading : %f V" % (name, result))
#       countA4 += 1

# def analogRead5():
#       global countA5
#       global handle
#       name = "AIN5"
#       result = ljm.eReadName(handle, name)
#       print("\n%s reading : %f V" % (name, result))
#       countA5 += 1

# def digitalRead1():
#       global countD1
#       global handle
#       name = "MIO0"
#       result = ljm.eReadName(handle, name)
#       print("\n%s reading : %f V" % (name, result))
#       countD1 += 1
#
# def digitalRead2():
#       global countD2
#       global handle
#       name = "MIO1"
#       result = ljm.eReadName(handle, name)
#       print("\n%s reading : %f V" % (name, result))
#       countD2 += 1
#
# def digitalRead3():
#       global countD3
#       global handle
#       name = "MIO2"
#       result = ljm.eReadName(handle, name)
#       print("\n%s reading : %f V" % (name, result))
#       countD3 += 1
#
# def digitalRead4():
#       global countD4
#       global handle
#       name = "FIO6"
#       result = ljm.eReadName(handle, name)
#       print("\n%s reading : %f V" % (name, result))
#       countD4 += 1
#
# def digitalRead5():
#       global countD5
#       global handle
#       name = "FIO7"
#       result = ljm.eReadName(handle, name)
#       print("\n%s reading : %f V" % (name, result))
#       countD5 += 1


# a3=threading.Thread(target=analogRead3)
# a4=threading.Thread(target=analogRead4)
# a5=threading.Thread(target=analogRead5)
# d1=threading.Thread(target=digitalRead1)
# d2=threading.Thread(target=digitalRead2)
# d3=threading.Thread(target=digitalRead3)
# d4=threading.Thread(target=digitalRead4)
# d5=threading.Thread(target=digitalRead5)

t1=time.time()
t2=time.time()
#count=0
while t2-t1<10 :
      a1 = threading.Thread(target=analogRead1)
      a2 = threading.Thread(target=analogRead2)
      #time.sleep(5)
      a1.start()
      a2.start()
      # a3.start()
      # a4.start()
      # a5.start()
      # d1.start()
      # d2.start()
      # d3.start()
      # d4.start()
      # d5.start()

      t2=time.time()
      #resultant=result2*2
      #f.write("%f\n" %resultant)
      #count+=1


# Close handle
#f.close()
print(countA1)
print(countA2)
# print("countA3",countA3)
# print("countA4",countA4)
# print("countA5",countA5)
# print("countD1",countD1)
# print("countD2",countD2)
# print("countD3",countD3)
# print("countD4",countD4)
# print("countD5",countD5)

ljm.close(handle)
