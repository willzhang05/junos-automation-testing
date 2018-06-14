#!/usr/bin/python3
# William Zhang
import sys
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from lxml import etree


def main():
    hostname = input("Device hostname: ")
    username = input("Device username: ")
    password = getpass("Device password: ")
    dev = Device(host=hostname, user=username, passwd=password)
    try:
        dev.open()
    except ConnectError as err:
        print ("Cannot connect to device: {0}".format(err))
        sys.exit(1)
    except Exception as err:
        print (err)
        sys.exit(1)
    #output = dev.display_xml_rpc('show isis adjacency')
    output = dev.rpc.get_config()
    print(etree.tostring(output, encoding='unicode'))

    dev.close()

if __name__ == '__main__':
    main()
