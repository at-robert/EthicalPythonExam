#!/usr/bin/env  python

import scapy.all as scapy
import argparse

#----------------------------------------------------------------------
def get_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument ("-t", "--ipaddress", dest="ipaddress", help="IP Address")
    return parser.parse_args()

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

    # print("IP\t\t\tMAC Address\n-----------------------")
    client_list = []
    for element in answered:
        # print(element) # 2 element: send package , answer
        # print(element[1].show()) # To show data structure
        client_dict = {"ip":element[1].psrc,"mac":element[1].hwsrc}
        client_list.append(client_dict)
        # print(element[1].psrc + "\t\t" + element[1].hwsrc)
        # print("---------------------------------------")
    return client_list

def print_result(result_list):
    print("IP\t\t\tMAC Address\n-----------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])

#----------------------------------------------------------------------
if __name__ == "__main__":

    (options, arguments) = get_argument()
    ip_addr = options.ipaddress
    print(ip_addr)
    scan_result = scan(ip_addr)
    print_result(scan_result)