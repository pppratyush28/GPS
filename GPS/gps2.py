import serial
from time import sleep
ser=serial.Serial('/dev/tty.0x100003eaf',19200)

while True:

    while ser.inWaiting()==0:
        pass
    print("ATLASLINK INITIALIZED")
    ser.flushInput()
    arr=ser.readline()
    arr2=arr.split(',')

    if arr2[0] == "$GPGGA":
        time = arr2[1][:-8]+':'+arr2[1][-8:-6]+':'+arr2[1][-6:-4]
        lat = arr2[2][:-7]
        latmin = arr2[2][-7:]
        latdir = arr2[3]
        lon = arr2[4][-7]
        lonmin = arr2[4][-7:]
        londir = arr2[5]
        sats = arr2[7]
        alt = arr2[9]
        print ('Universal Time: '),time
        print ('You are Tracking: '),sats,' satellites'
        print ('My Latitude: '),lat, 'Degrees ', latmin,' minutes ', latdir
        print ('My Longitude: '),lon, 'Degrees ', lonmin,' minutes ', londir
        print ('My Altitude: '),alt

    elif arr2[0] == "$GPGNS":
        time = arr2[1][:-8]+':'+arr2[1][-8:-6]+':'+arr2[1][-6:-4]
        lat = arr2[2][:-7]
        latmin = arr2[2][-7:]
        latdir = arr2[3]
        lon = arr2[4][-7]
        lonmin = arr2[4][-7:]
        londir = arr2[5]
        sats = arr2[7]
        alt = arr2[9]
        print ('Universal Time: '),time
        print ('You are Tracking: '),sats,' satellites'
        print ('My Latitude: '),lat, 'Degrees ', latmin,' minutes ', latdir
        print ('My Longitude: '),lon, 'Degrees ', lonmin,' minutes ', londir
        print ('My Altitude: '),alt

    elif arr2[0] == "$GPGSA":
        mode = arr[2]
        if mode == 1:
            print ("fix not available")
        elif mode == 2:
            print ("2D fix")
        else:
            print ("3D fix")
    
    elif arr2[0] == "$GPGST":
        time = arr2[1][:-8]+':'+arr2[1][-8:-6]+':'+arr2[1][-6:-4]
        rmserr = arr2[2]
        print ('Universal Time: '),time
        print ('RMS error: '),rmserr

    elif arr2[0] == "$GPGSV":
        sats = arr2[3]
        print ('You are Tracking: '),sats,' satellites'

    elif arr2[0] == "$GPZDA":
        time = arr2[1][:-8]+':'+arr2[1][-8:-6]+':'+arr2[1][-6:-4]
        day = arr2[2]
        month = arr2[3]
        year = arr2[4]
        print ('Universal Time: '),time
        print ('day: '),day
        print ('month: '),month
        print ('year: '),year
    
    else:
        pass

    time.sleep(1)

        
    




