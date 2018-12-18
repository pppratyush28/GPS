from socketIO_client_nexus import SocketIO,LoggingNameSpace
import logging
import time
 
i = 0
with SocketIO('localhost', 4000, LoggingNameSpace) as socketio:
    while True:
        data = i
        socketIO.emit('arduino',{'arduino':data})
        time.sleep(0.1)
        i=i+1