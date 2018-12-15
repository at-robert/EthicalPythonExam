#!/usr/bin/env  python
import subprocess
import optparse

#----------------------------------------------------------------------
def get_argument():
    parser = optparse.OptionParser()
    parser.add_option ("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m","--mac", dest="new_mac", help="New MAC address")

    return parser.parse_args()

#----------------------------------------------------------------------
if __name__ == "__main__":

    (options, arguments) = get_argument()

    interface = options.interface
    new_mac = options.new_mac

    # print(" {} , {}".format(type(interface), type(new_mac)))

    if(isinstance(interface, str) & isinstance(new_mac, str)):
        print("[+] Changing MAC address for " + interface + " to " + new_mac)
    else:
        print("Not input Argument properly yet !!")