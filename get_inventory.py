#!/usr/bin/env python

from pycimc import *
import config
from pprint import pprint
import cveLogger

import sys
cveLogger.initlogging(sys.argv)

wildcard = '0.0.0.0'
for address in config.SERVERS:
    if config.CREDS.get(address):
        USERNAME = config.CREDS[address].get('username')
        PASSWORD = config.CREDS[address].get('password')
    else:
        USERNAME = config.CREDS[wildcard].get('username')
        PASSWORD = config.CREDS[wildcard].get('password')

    with UcsServer(address, USERNAME, PASSWORD) as server:
        out_string = server.ipaddress
        if server.get_interface_inventory():
            for int in server.inventory['adaptor']:
                out_string += ',SLOT-'+int['pciSlot']
                for port in int['port']:
                    out_string += ',port-'+str(port['portId'])+','+port['adminSpeed']+','+port['linkState']
                    for vnic in port['vnic']:
                        out_string += ','+str(vnic['name'])+','+str(vnic['mac'])
                pprint(out_string)
        else:
            pprint('get_interface_inventory() returned False')
