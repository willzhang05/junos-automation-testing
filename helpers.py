#!/usr/bin/python3
# William Zhang
import os, sys
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from lxml import etree


def main():
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        print("No file specified.")
        return 1

    if not os.path.isfile(filepath):
        print("Invalid filepath.")
        return 1
    tree = etree.parse(filepath)
    '''
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
    '''
    print(etree.tostring(tree.getroot()))
    return 0


if __name__ == '__main__':
    main()
