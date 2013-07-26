# Client program: Encoder
# By Kishoj Bajracharya
import random
import numpy
from decimal import *

# Initial data from the three different source nodes
# Say data from node A
a = ['H', 'e', 'l', 'l', 'o', 'a', 'b', 'c', 'd', 'e', 'A', 'p', 'p', 'l', 'e', 'A', 'p', 'p', 'l', 'e', 'H', 'e', 'l', 'l', 'o', 'a', 'b', 'c', 'd', 'e', 'H', 'e', 'l', 'l', 'o', 'a', 'b', 'c', 'd', 'e', 'A', 'p', 'p', 'l', 'e', 'A', 'p', 'p', 'l', 'e', 'H', 'e', 'l', 'l', 'o', 'a', 'b', 'c', 'd', 'e', 'H', 'e', 'l', 'l', 'o', 'a', 'b', 'c', 'd', 'e', 'A', 'p', 'p', 'l', 'e', 'A', 'p', 'p', 'l', 'e', 'H', 'e', 'l', 'l', 'o', 'a', 'b', 'c', 'd', 'e', 'H', 'e', 'l', 'l', 'o', 'a', 'b', 'c', 'd', 'e', 'A', 'p', 'p', 'l', 'e', 'A', 'p', 'p', 'l', 'e', 'H', 'e', 'l', 'l', 'o', 'a', 'b', 'c', 'd', 'e', 'H', 'e', 'l', 'l', 'o', 'a', 'b', 'c', 'd', 'e', 'A', 'p', 'p', 'l', 'e', 'A', 'p', 'p', 'l', 'e', 'H', 'e', 'l', 'l', 'o', 'a', 'b', 'c', 'd', 'e']
# Say data from node B
b = ['a', 'b', 'c', 'd', 'e', 'A', 'p', 'p', 'l', 'e', 'H', 'e', 'l', 'l', 'o', 'H', 'e', 'l', 'l', 'o', 'a', 'b', 'c', 'd', 'e', 'A', 'p', 'p', 'l', 'e', 'a', 'b', 'c', 'd', 'e', 'A', 'p', 'p', 'l', 'e', 'H', 'e', 'l', 'l', 'o', 'H', 'e', 'l', 'l', 'o', 'a', 'b', 'c', 'd', 'e', 'A', 'p', 'p', 'l', 'e', 'a', 'b', 'c', 'd', 'e', 'A', 'p', 'p', 'l', 'e', 'H', 'e', 'l', 'l', 'o', 'H', 'e', 'l', 'l', 'o', 'a', 'b', 'c', 'd', 'e', 'A', 'p', 'p', 'l', 'e', 'a', 'b', 'c', 'd', 'e', 'A', 'p', 'p', 'l', 'e', 'H', 'e', 'l', 'l', 'o', 'H', 'e', 'l', 'l', 'o', 'a', 'b', 'c', 'd', 'e', 'A', 'p', 'p', 'l', 'e', 'a', 'b', 'c', 'd', 'e', 'A', 'p', 'p', 'l', 'e', 'H', 'e', 'l', 'l', 'o', 'H', 'e', 'l', 'l', 'o', 'a', 'b', 'c', 'd', 'e', 'A', 'p', 'p', 'l', 'e']
# Say data from node C
c = ['A', 'p', 'p', 'l', 'e', 'H', 'e', 'l', 'l', 'o', 'a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e', 'A', 'p', 'p', 'l', 'e', 'H', 'e', 'l', 'l', 'o', 'A', 'p', 'p', 'l', 'e', 'H', 'e', 'l', 'l', 'o', 'a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e', 'A', 'p', 'p', 'l', 'e', 'H', 'e', 'l', 'l', 'o', 'A', 'p', 'p', 'l', 'e', 'H', 'e', 'l', 'l', 'o', 'a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e', 'A', 'p', 'p', 'l', 'e', 'H', 'e', 'l', 'l', 'o', 'A', 'p', 'p', 'l', 'e', 'H', 'e', 'l', 'l', 'o', 'a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e', 'A', 'p', 'p', 'l', 'e', 'H', 'e', 'l', 'l', 'o', 'A', 'p', 'p', 'l', 'e', 'H', 'e', 'l', 'l', 'o', 'a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e', 'A', 'p', 'p', 'l', 'e', 'H', 'e', 'l', 'l', 'o']

# Code for random linear coding
def linearCode(x, y, z):
	ilist = []
	a = 1*x + 1*y + 1*z
	b = 2*x + 1*y + 1*z
	c = 1*x + 2*y + 1*z
	ilist.append(numpy.float64(1))
	ilist.append(numpy.float64(1))
	ilist.append(numpy.float64(1))
	ilist.append(numpy.float64(a))

	ilist.append(numpy.float64(2))
	ilist.append(numpy.float64(1))
	ilist.append(numpy.float64(1))
	ilist.append(numpy.float64(b))

	ilist.append(numpy.float64(1))
	ilist.append(numpy.float64(2))
	ilist.append(numpy.float64(1))
	ilist.append(numpy.float64(c))
	return ilist

def encode(x, y, z):
	li = linearCode(x, y, z) 
	#for a in li: 
	#	print a
	listOfEqns = split(4, li)
	return listOfEqns

def split(n, iter, fill=None):
    return [iter[i:i+n] + [fill] * (i + n - len(iter))
            for i in xrange(0, len(iter), n)]

def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)
    return reduce(lambda x,y:x+y, lst)

def ListOfCharToListOfInt(alist):
	iList = []
	for x in alist:
		# char to hex
		q = toHex(x)
		#print q 
		#p = int('0x48', 16)
		# Hex to int		
		p = int(q, 16)
		#print p
		iList.append(p)
	return iList

# Packets whose values are conveted into the decimal values
p = ListOfCharToListOfInt(a)
#print p
q = ListOfCharToListOfInt(b)
#print q
r = ListOfCharToListOfInt(c)
#print r
i = 0

# list containing decoded packets
listAns = []

# Perform an encoding operation using Random Linear Coding
encodedlist = []

for x in p:
	# Mix the packets from the list of 3 packets
	listOfVector = encode(x, q[i], r[i])
	i = i + 1	
	#print 'List of Encoded data'
	print listOfVector
	encodedlist.append(listOfVector)

#print encodedlist
encoded_mess = str(encodedlist)
print 'Encoded Message'
#print encoded_mess

from socket import *

# Set the socket parameters
host = "localhost"
port = 21567
buf = 300000
addr = (host,port)

# Create socket
UDPSock = socket(AF_INET,SOCK_DGRAM)

def_msg = "===Enter message to send to server===";
print "\n",def_msg

# Send messages
while (1):
	#data = raw_input('>> ')
	data = encoded_mess
	if(UDPSock.sendto(data,addr)):
		print "Sending message '",data,"'....."
		break

# Close socket
UDPSock.close()

