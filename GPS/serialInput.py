import serial
GPS = serial.Serial('IOUSBDevice', 19200)
while(1):
        while GPS.inWaiting()==0:
                pass
        NMEA=GPS.readline()
        print (NMEA)