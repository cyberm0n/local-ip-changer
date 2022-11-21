from pyroute2 import IPRoute
import sys

if len(sys.argv) < 3:
  print('true usage : python ip-changer.py <ip-adress> <interface>')
else:
  ip = IPRoute()
  index = ip.link_lookup(ifname=sys.argv[2])[0]
  ip.addr('add', index, address=sys.argv[1], mask=24)
  ip.close()
