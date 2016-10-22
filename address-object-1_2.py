#!/usr/bin/env python

file = open('ipadd.txt')
#line = file.readlines()
line = file.read().splitlines()

i = 0

while i < len(line):
	print "address-object \"%s\"" % str(line[i])
	print "host %s" % str(line[i])
	print "zone WAN"
	print "end"
	i = i+1

file.close()
#https://github.com/ledzep84
