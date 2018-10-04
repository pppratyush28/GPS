from labjack import ljm
import time
#import threading
handle = ljm.openS("ANY", "ANY", "ANY")
info = ljm.getHandleInfo(handle)
print("Opened a LabJack with Device type: %i, Connection type: %i,\n"
      "Serial number: %i, IP address: %s, Port: %i,\nMax bytes per MB: %i" %
      (info[0], info[1], info[2], ljm.numberToIP(info[3]), info[4], info[5]))
#f = open ('sampleWrLP.csv','w+')
t1=time.time()
t2=time.time()
count=0

while t2-t1<10 :

      name = "AIN0"
      result = ljm.eReadName(handle, name)
      print("\n%s reading : %f V" % (name, result))

      name = "AIN1"
      result = ljm.eReadName(handle, name)
      print("\n%s reading : %f V" % (name, result))

      name = "AIN2"
      result = ljm.eReadName(handle, name)
      print("\n%s reading : %f V" % (name, result))

      name = "AIN3"
      result = ljm.eReadName(handle, name)
      print("\n%s reading : %f V" % (name, result))

      name = "AIN4"
      result2 = ljm.eReadName(handle, name)
      print("\n%s reading : %f V" % (name, result2))

      # name = "MIO0"
      # result = ljm.eReadName(handle, name)
      # print("\n%s reading : %f V" % (name, result))
      #
      # name = "MIO1"
      # result = ljm.eReadName(handle, name)
      # print("\n%s reading : %f V" % (name, result))
      #
      # name = "MIO2"
      # result = ljm.eReadName(handle, name)
      # print("\n%s reading : %f V" % (name, result))
      #
      # name = "FIO6"
      # result = ljm.eReadName(handle, name)
      # print("\n%s reading : %f V" % (name, result))
      #
      # name = "FIO7"
      # result = ljm.eReadName(handle, name)
      # print("\n%s reading : %f V" % (name, result))

      #time.sleep(5)

      t2=time.time()
      #resultant=result2*2
      #f.write("%f\n" %resultant)
      count+=1


# Close handle
#f.close()
print("count",count/10)
ljm.close(handle)
