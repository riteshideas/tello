# This example script demonstrates how to send/receive commands to/from Tello
# This script is part of our course on Tello drone programming
# https://learn.droneblocks.io/p/tello-drone-programming-with-python/

# Import the built-in socket and time modules
import socket
import time
from collections import deque

#tello_address_info = deque(maxlen=
tello_address_info = []
for i in range(int(input("How mant tellos? "))):
	tello_address_info.append((input("Ip address: "), int(input("Port: "))))

for val, address in enumerate(tello_address_info):
	print(f"Tello Drone {val+1} : \033[1m{address[0]}\033[0m  ->  \033[1m{address[1]}\033[0m")

# IP and port of Tello
#tello_address = ('192.168.10.1', 8889)

# Create a UDP connection that we'll send the command to
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Let's be explicit and bind to a local port on our machine where Tello can send messages
sock.bind(('', 6969))

# Function to send messages to Tello
def send(message, printOut_, address):
    try:
        sock.sendto(message.encode(), address)
        if printOut_: print("Sending message: " + message)
    except Exception as e:
        print("Error sending: " + str(e))

# Function that listens for messages from Tello and prints them to the screen
def receive():
	try:
		response, ip_address = sock.recvfrom(128)
		return response.replace("\n", "").decode(encoding = 'utf-8'), str(ip_address)
	except Exception as e:
		print("Error receiving: " + str(e))


def send_command(command, tello_ip,reading=False, sleep_time=3, printOut=True):
	send(command, printOut, tello_ip)
	output = receive()
	if printOut : print("Received message: " + output[0] + " from Tello with IP: " + str(output[1]) + "\n")
	if not reading: time.sleep(sleep_time)
	else: pass
	return output


with open("command.txt", "r") as f:
	commands = f.read()
commands = commands.split("\n")


for command in commands:
	command = command.strip(" -> ")
	send_command(command, tello_address_info[int(command[1]) - 1])
#send_command("command")
#send_command("battery?", True)
#send_command("takeoff")
#send_command("land")


# Important!
sock.close()

