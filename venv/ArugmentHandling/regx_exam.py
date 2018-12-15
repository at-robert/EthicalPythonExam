#!/usr/bin/env  python
import subprocess
import optparse
import re

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

    res = subprocess.check_output(["ls","-la"])
    print(" Output = {}".format(res))

    reg_res = re.search(r"total [0-9]*",res.decode("utf-8"))
    print(" Regx Output = {}".format(reg_res.group(0)))
