#!/usr/bin/env  python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    print(arp_request.summary())
    # scapy.ls(scapy.ARP())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether())
    print(broadcast.summary())
    arp_request_broadcast = broadcast/arp_request
    arp_request_broadcast.show()

    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    # print(answered.summary())

    print("IP\t\t\tMAC Address\n-----------------------")
    for element in answered:
        # print(element) # 2 element: send package , answer
        # print(element[1].show()) # To show data structure
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
        print("---------------------------------------")


scan("10.0.1.1/24")
