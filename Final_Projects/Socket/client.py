import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Get local machine name
host = socket.gethostbyname('localhost')                          

# Set the port
port = 9993

# Connect to hostname on the port.
s.connect((host, port))                               

# Receive no more than 1024 bytes
msg = s.recv(1024)                                     
print (msg.decode('utf-8'))

text = 'It is a great day'
s.send(text.encode('utf-8'))

# Close the connection
s.close()