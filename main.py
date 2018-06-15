#!/usr/bin/python3
# William Zhang
import sys
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from lxml import etree


def main():
    if len(sys.argv) == 3:
        hostname = sys.argv[1]
        username = sys.argv[2]
    if len(sys.argv) == 2:
        hostname = sys.argv[1]
        username = "root"
    if len(sys.argv) == 1:
        hostname = input("Device hostname: ")
        username = input("Device username: ")

    password = getpass("Device password: ")
    dev = Device(host=hostname, user=username, passwd=password)

    try:
        dev.open()
    except ConnectError as err:
        print("Cannot connect to device: {0}".format(err))
        sys.exit(1)
    except Exception as err:
        print(err)
        sys.exit(1)

    output = dev.rpc.get_route_information()
    find = etree.XPath('//rt')
    matches = find(output)
    routes = []

    for m in matches:
        entry = dict()
        type_find = etree.XPath('rt-entry//protocol-name')
        entry['type'] = type_find(m)[0].text
        dest_find = etree.XPath('rt-destination')
        entry['dest'] = dest_find(m)[0].text
        int_find = etree.XPath('rt-entry//nh/via')
        int_res = int_find(m)
        entry['int'] = int_find(m)[0].text if len(int_res) > 0 else None
        routes.append(entry)

    print(routes)
    dev.close()


if __name__ == '__main__':
    main()
