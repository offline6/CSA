import scapy.all as scapy
from socket import* 
import sys
import ipaddress
import argparse
import subprocess

class result: 
    def __init__(self, ip, mac): 
        self.ip = ip 
        self.mac = mac

def inputIp():
	return ipaddress.ip_network(sys.argv[1], False).hosts()
    
def scan(targets):
	pass

def print_results(results):
	print("IP" + "\t\t" + "MAC")
	for el in results:
		print(el.ip, el.mac)
def containsAny(str, set):
    return 1 in [c in str for c in set]

# Main 
parser = argparse.ArgumentParser(description='Scan IP Range for MAC')
parser.add_argument('iprange', help='Single IP or Range')
parser.add_argument('-a', '--arp', help='Use arp system process for scanning (Default: disabled)', action='store_true', dest="arp")
parser.add_argument('-v', '--verbose', help='Enable verbosity (Default: disabled)', action='store_true', dest="verbose")
args = parser.parse_args()



if args.verbose:
	sys.stderr = sys.__stderr__
else:
	sys.stderr = None 

try:
	targets = inputIp()
except:
	print("Invalid ip range provided")
	exit()


if args.arp:
	subprocess.run(['arp-scan' if containsAny(sys.argv[1], '/-') else 'arp', sys.argv[1]])
else:
	results = []

	for ip in targets:
		mac = getmacbyip(str(ip)) 
		if(str(mac) != 'None'):
			results.append(result(ip, mac))
	if not results:
		print("Could not scan any of the input ip addresses")
	else:
		print_results(results)