import obd
import time

connection = obd.OBD("COM11",fast=False) 

while True:  
    if connection.status() == "Car Connected":
        #print("Car Connected")
        cmd = obd.commands.RPM # select an OBD command (sensor)
        response = connection.query(cmd) # send the command, and parse the response
        cmd = obd.commands.SPEED # select an OBD command (sensor)
        response2 = connection.query(cmd)

        if not response.is_null():
            print(response.value) 
            print(response2.value)