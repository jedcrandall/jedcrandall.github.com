#!/usr/bin/env python

from scapy.all import *
import sys
import random

MULTIPLIER = 44
TIMES8 = (44 * 8)

pastids = []
def uniqid():
    id = random.randint(0,2**16-1)
    while id in pastids:
        id = random.randint(0,2**16-1)
    pastids.append(id)
    return id

def makefragmentssillyway(pkt):
    lst = []
    bla = pkt.copy()
    del(bla[IP].payload)
    del(bla[IP].chksum)
    del(bla[IP].len)
    one = bla.copy()
    two = bla.copy()
    three = bla.copy()
    four = bla.copy()
    five = bla.copy()
    six = bla.copy()
    one[IP].flags |= 1
    two[IP].flags |= 1
    three[IP].flags |= 1
    four[IP].flags |= 1
    five[IP].flags |= 1
    one[IP].frag = 0
    two[IP].frag = 4 * MULTIPLIER
    three[IP].frag = 6 * MULTIPLIER 
    four[IP].frag = 1 * MULTIPLIER
    five[IP].frag = 6 * MULTIPLIER
    six[IP].frag = 9 * MULTIPLIER
    s = raw(pkt[IP].payload)
    r_one_bytes = s[0:TIMES8]
    r_one_bytes += bytes('1' * (TIMES8 * 2), 'ascii')
    r_one = conf.raw_layer(load=r_one_bytes)
    r_two = conf.raw_layer(load='2' * (TIMES8 * 2))
    r_three = conf.raw_layer(load='3' * (TIMES8 * 3))
    r_four = conf.raw_layer(load='4' * (TIMES8 * 4))
    r_five = conf.raw_layer(load='5' * (TIMES8 * 3))
    r_six = conf.raw_layer(load='6' * (TIMES8 * 3))
    r_one.overload_fields = pkt[IP].payload.overload_fields.copy()
    r_two.overload_fields = pkt[IP].payload.overload_fields.copy()
    r_three.overload_fields = pkt[IP].payload.overload_fields.copy()
    r_four.overload_fields = pkt[IP].payload.overload_fields.copy()
    r_five.overload_fields = pkt[IP].payload.overload_fields.copy()
    r_six.overload_fields = pkt[IP].payload.overload_fields.copy()
    one.add_payload(r_one)
    lst.append(one)
    two.add_payload(r_two)
    lst.append(two)
    three.add_payload(r_three)
    lst.append(three)
    four.add_payload(r_four)
    lst.append(four)
    five.add_payload(r_five)
    lst.append(five)
    six.add_payload(r_six)
    lst.append(six)
    return lst


# 16 is 8 bytes of ICMP header and 8 bytes of name of the probe
if 1:
    firststr = 'FIRST111' + '1' * ((TIMES8 * 3) - 16) + '4' * (TIMES8) + '2' * (TIMES8 * 2) + '3' * (TIMES8 * 3) + '6' * (TIMES8 * 3)  
    laststr = 'LAST1111' + '1' * ((TIMES8) - 16) + '4' * (TIMES8 * 4) + '2' * (TIMES8) + '5' * (TIMES8 * 3) + '6' * (TIMES8 * 3)  
    linuxstr = 'LINUX111' + '1' * ((TIMES8 * 3) - 16) + '4' * (TIMES8 * 2) + '2' * (TIMES8) + '5' * (TIMES8 * 3) + '6' * (TIMES8 * 3)  
    bsdstr = 'BSD11111' + '1' * ((TIMES8 * 3) - 16) + '4' * (TIMES8 * 2) + '2' * (TIMES8) + '3' * (TIMES8 * 3) + '6' * (TIMES8 * 3)  
    bsdrightstr = 'BSDRIGHT' + '1' * ((TIMES8) - 16) + '4' * (TIMES8 * 3) + '2' * (TIMES8 * 2) + '5' * (TIMES8 * 3) + '6' * (TIMES8 * 3)  

    random.seed()

    dapackets = []
    firstpacket = IP(dst=sys.argv[1],id=uniqid())/ICMP(type=8,id=uniqid())/firststr
    dapackets.append(firstpacket)
    lastpacket = IP(dst=sys.argv[1],id=uniqid())/ICMP(type=8,id=uniqid())/laststr
    dapackets.append(lastpacket)
    linuxpacket = IP(dst=sys.argv[1],id=uniqid())/ICMP(type=8,id=uniqid())/linuxstr
    dapackets.append(linuxpacket)
    bsdpacket = IP(dst=sys.argv[1],id=uniqid())/ICMP(type=8,id=uniqid())/bsdstr
    dapackets.append(bsdpacket)
    bsdrightpacket = IP(dst=sys.argv[1],id=uniqid())/ICMP(type=8,id=uniqid())/bsdrightstr
    dapackets.append(bsdrightpacket)

    for packet in dapackets:
        sillyfrags = makefragmentssillyway(packet)
        for f in sillyfrags:
            send(f)

