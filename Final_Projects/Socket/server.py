import socket                                         

# Create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Get local machine name
host = socket.gethostbyname('localhost')

try:
    port = 9993   
except OSError:
    print("Address Error")                                   
else:
    # Bind to the port
    serversocket.bind((host, port))                                  

    # Listen
    serversocket.listen(5)                                           

    # Connect
    while True:
        clientsocket,addr = serversocket.accept()      

        print("Got a connection from %s" % str(addr))
            
        msg = 'Thank you for connecting'+ "\n"
        clientsocket.send(msg.encode('utf-8'))
        clientsocket.close()
        
        text = clientsocket.recv(1024)
        print (text.decode('utf-8'))
        
serversocket.close()