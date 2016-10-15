#!/usr/bin/env python

file = open('ipadd.txt')
#line = file.readlines()
line = file.read().splitlines()
group = raw_input("Enter Address Group Name: ")
i = 0
print "address-group \"%s\"" % (group)
while i < len(line):
        print "address-object \"%s\"" % str(line[i])
        i = i+1

file.close()
