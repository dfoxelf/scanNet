#!/usr/bin/env python2.7
# _*_ coding: utf-8 _*_


"""
scanNet.py 1.0.0 by cb0n3y ()
Licence: BSD, GPL3, GNU

Description: This script was designed to be 
			 executed on your own network and 
			 thus know which hosts are turned 
			 on and their respective hostnames.

Usage: Just run it like every python program

Advice: This script is for private use only on 
		your own network. I am not responsible 
		for any misuse you may give to the 
		content of this script. Please be smart 
		and don't break the law.
"""


__author__ = 'cb0n3y'
__version__ = '1.0.0'
__copyright__ = 'Copyright (c) 2018-2019 cb0n3y'



import socket


def hostNameDiscover():
	ip_addrs = []
	ip_prefix = '10.10.20.'	# Please change this ip address to the tree first octet your own network.
	
	for i in range(1, 256):
		ip_addrs.append(str(ip_prefix) + str(i))

	for ips in ip_addrs:
		try:
			print("[+] IP Addrerss: {} ==> Host Name: {}".format(ips, socket.gethostbyaddr(ips)[0]))
		except socket.error as e:
			print("[-] Error ==> {}".format(e))
			continue

	
	
if __name__ == '__main__':
	hostNameDiscover()


