#!/usr/bin/python3
# William Zhang
import os, sys
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from lxml import etree

def route_advert_bgp(tree, addr, table=None):
    if table is None:
        rt_tab_find = etree.XPath('//route-table/table-name/..')
    else:
        rt_tab_find = etree.XPath('//route-table/*[table-name=' + table + ']/..')

    rt_table = rt_tab_find(tree)

    print(rt_table)
    print(etree.tostring(rt_table[0]))


    return

def route_recv_bgp():

    return


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
    route_advert_bgp(tree, "140.222.238.201", table="inet.0")

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
    return 0


if __name__ == '__main__':
    main()
