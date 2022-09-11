import socket
import subprocess
import sys
import time

#Blank your screen
subprocess.call('clear', shell=True)

#Ask for input
remoteServer = input("Hello, Mel! Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

#Print a nice banner with information on which host we are about to scan
print ("Please wait, scanning remote host", remoteServerIP)

#Time start
start = time.time()

#Using the range function specifies ports
#Also, errors will be handled

try:
for port in range (1, 5000):
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((remoteServerIP, port))
if result == 0:
print ("Port {}:    Open".format(port))
sock.close()

except KeyboardInterrupt:
print ("Exiting...You Pressed Ctrl+C")
sys.exit()

except socket.gaierror:
print ("Exiting...Hostname could not be resolved. Exiting")
sys.exit()

except socket.error:
print ("Exiting...Couldn't connect to server")
sys.exit()


#Time difference
end = time.time()

#Print time elapsed on screen
print ("Scanning Completed in: ",end - start, "seconds")
