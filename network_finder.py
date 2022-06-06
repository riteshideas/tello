# A basic script to scan a local network for IP addresses to indentify Tello EDU drones


# Import modules
import ipaddress
from subprocess import Popen, PIPE



OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'


# Create the network
ip_net = ipaddress.ip_network(u'192.168.43.1/25', strict=False)

# Loop through the connected hosts
for val, ip in enumerate(ip_net.hosts()):

    # Convert the ip to a string so it can be used in the ping method
    ip = str(ip)
    
    # Let's ping the IP to see if it's online
    toping = Popen(['ping', '-c', '1', '-W', '50', ip], stdout=PIPE)
    output = toping.communicate()
    hostalive = toping.returncode
    
    print(f"{BOLD}[{val+1}/{ip_net.num_addresses}]{ENDC}", end=": ")
    # Print whether or not device is online
    if hostalive == 0:
        print(ip, f"{OKGREEN}is online{ENDC}")

    else:
        print(ip, f"{FAIL}is offline{ENDC}")
print(f"{BOLD}Completed!{ENDC}")
