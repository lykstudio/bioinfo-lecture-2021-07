#! /usr/bin/env python

file_name = "read_sample.txt"


#1
# with open(file_name, "r") as handle:
#    for line in handle:
#       print(line)

#2
# with open(file_name, "r") as handle:
#    lines = handle.readlines()
#    for line in lines:
#        print(line.strip())


#3
#handle = open(file_name, 'r')
#for line in handle:
#    print(line.strip())
#handle.close()

#4
handle = open(file_name, 'r')
lines = handle.readlines()
for line in lines:
    print(line.strip())
handle.close()



