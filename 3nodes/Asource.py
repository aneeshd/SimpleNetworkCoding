# Source A send the data to node B
# Client program when souce node A sends data to intermediate nodes

import binascii
import base64
from socket import *

ibinarylist1 = []
ibinarylist2 = []

def byte_to_binary(n):
    return ''.join(str((n & (1 << i)) and 1) for i in reversed(range(8)))

def hex_to_binary(h):
    return ''.join(byte_to_binary(ord(b)) for b in binascii.unhexlify(h))

def ByteToHex( byteStr ):
    return ' '.join( [ "%02X" % ord( x ) for x in byteStr ] )
	
# convert the decimal value into the binary value
def bin(s):
    return str(s) if s<=1 else bin(s>>1) + str(s&1)

def dec2hex(n):
    """return the hexadecimal string representation of integer n"""
    return "%X" % n

def hex2dec(s):
    """return the integer value of a hexadecimal string s"""
    return int(s, 16)

def StringToBinaryList(astring):
	ibinarylist = []
	Valueinbits = ''
	for x in astring: 
		#print x
		if x:
			hexValue = ByteToHex(x)
			binValue = hex_to_binary(hexValue)
			print x + ' equivalent binary value ' + binValue
			if binValue == '1010':
				#print '1010: end of file'
				ibinarylist.append(binValue)
				Valueinbits += binValue
			else:
				ibinarylist.append(binValue)
				Valueinbits += binValue
	return ibinarylist

def stringToInteger(astring):
	listOfinteger = []
	for c in astring[0:len(astring)]:
		p = int(c)
		listOfinteger.append(p)
	return listOfinteger


def IntegerToString(aint):
	listOfStr = []
	for c in aint[0:len(aint)]:
		p = str(c)
		listOfStr.append(p)
	return listOfStr

# Performs XOR operations for two bits 
# Returns: integer or bit after XOR operations
def XOROperation(a, b):
	return a ^ b 

# Use Network coding and performs Encoding of data bits from two sources 
# Returns: list of integers (bits) after XOR operationsnd performs Encoding of data bits from two sources 
def EnodeDatabits(p, q):
	c_data = []
	len1 = len(p)
	len2 = len(q)
	i = 0
	if len1 == len2:
		#print	'Both data contain equal bits'
		for x in p:
  			xor_res = XOROperation(x, q[i]) 
			c_data.append(xor_res)
			i = i + 1
	elif len1 > len2:
		print ''
	elif len2 > len1:
		print '' 
	return c_data


# Performs decoding of data bits to separate the data from two sources 
# Returns: list of integers (bits) 
def DecodeData(c, s):
	d_data = []
	len1 = len(c)
	len2 = len(s)
	i = 0
	if len1 == len2:
		#print	'Both data contain equal bits'
		for x in c:
  			xor_res = XOROperation(x, s[i]) 
			d_data.append(xor_res)
			i = i + 1
	elif len1 > len2:
		print ''
	elif len2 > len1:
		print '' 
	return d_data

def ListOfCharToListofString(alist):
	Integerlist = []	
	for x in alist:
		p = stringToInteger(x)
		Integerlist.append(p)
	return Integerlist

def ListOfStringToListofChar(alist):
	Charlist = []	
	for x in alist:
		p = IntegerToString(x)
		string = ''
		for y in p:
			string += str(y) 
		Charlist.append(string)
	return Charlist


def ListAfterXOREncode(lis1, lis2):
	Integerlist1 = []
	Integerlist2 = []
	xorIntegerlist = [] 
	# Initially coded_data is empty.
	coded_data = []
	listOfCodedData = []
	i = 0
	for x in lis1:
		p = stringToInteger(x)
		Integerlist1.append(p)
	for x in lis2:
		p = stringToInteger(x)
		Integerlist2.append(p)
	print 'Network Coding started: Performing XOR operations on bits...'
	for x in Integerlist1:
		data1 = x
		data2 = Integerlist2[i]
		i = i + 1
		coded_data = EnodeDatabits(data1, data2)
		listOfCodedData.append(coded_data)
	print 'End on Encoding'	
	return listOfCodedData

def ListDecode(lis1, lis2):
	Decoded_list = []
	i = 0
	for x in lis1:
		ilist = []
		data1 = stringToInteger(x)
		data2 = stringToInteger(lis2[i])
		i = i + 1
		ilist = EnodeDatabits(data1, data2)
		Decoded_list.append(ilist)
	return Decoded_list

def ListOfCharToListOfBinary(alist):
	p = []
	for x in alist:
		c = int(x)
		p.append(c)
	return p


def ListOfBinaryToListOfHex(alist):
	p = []
	for x in alist:
		c = int(x, 2)
		z = hex(c)
		p.append(z)
	return p

def ListOfHexToListOfDecimal(alist):
	p = []
	for x in alist:
		integer = int(x, 16)
		p.append(integer)
	return p

def ListOfDeciamlToListOfChar(alist):
	p = []
	for x in alist:
		char = chr(x)
		p.append(char)
	return p

def ListOfBinaryToListOfChar(alist):
	p = []
	for x in alist:
		c = int(x, 2)
		z = hex(c)
		integer = int(z, 16)
		char = chr(integer)
		p.append(char)
	#print p
	return p

# Convert the binary list to its equivalent Hex String
def BinarylistToHexString(bl):
	bytesin =''
	for x in bl:
		bytesin += x 
	#print bytesin
	dd = bytesin.replace('0x', '\\x')
	return dd

	
def Result(source, aDecodedata):
	print ''
	print 'Decode data from source node: ' + source
	decoded_1 =  ListOfStringToListofChar(aDecodedata)
	print 'List of string decoded:'
	print decoded_1

	print 'Converting it into binary value'
	binarylist =  ListOfCharToListOfBinary(decoded_1)
	print binarylist

	print 'Converting binary value to hex value'
	hexlist = ListOfBinaryToListOfHex(decoded_1)
	print hexlist

	print 'Converting to data'
	data = ListOfBinaryToListOfChar(decoded_1)
	return data

def BackToString(alist):
	decoded_1 =  ListOfStringToListofChar(alist)
	
	print 'List of string decoded:'
	print decoded_1

	print 'Converting it into binary value'
	binarylist =  ListOfCharToListOfBinary(decoded_1)
	print binarylist

	print 'Converting binary value to hex value'
	hexlist = ListOfBinaryToListOfHex(decoded_1)
	print hexlist
	
	print 'Converting to data'
	dataq = ListOfBinaryToListOfChar(decoded_1)
	print dataq
	print StringToBinaryList(dataq)
	print 'done'
	return dataq




def ConcatListElements(alist):
	p = ''	
	for x in alist:
		p += x
	return p

# Set the socket parameters
host1 = "localhost"
port1 = 21578
buf = 2048
addr1 = (host1, port1)
data1 = ''
# Create socket
UDPSock = socket(AF_INET,SOCK_DGRAM)

def_msg = "Enter message to send to intermediate node C";
print "\n",def_msg
data1list = []
# Send messages
while (1):
	data1 = raw_input('>> ')
	data1list = StringToBinaryList(data1)
	if not data1:
		break
	else:
		if(UDPSock.sendto(data1, addr1)):
			print "Sending message '",data1,"'....."
			
		# Now hear the packet receive from the intermediate node
		# Set the socket parameters
		host2 = '' # Bind to all interfaces or use 0.0.0.0 to bind to all interfaces
    		s = socket(AF_INET, SOCK_DGRAM)
    		s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    		s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    		s.bind((host2,8881))
		
		message = ''
    		print 'Listening the broadcasted message: ...'
		while True :
			# This port should be different for all the nodes
			message , address = s.recvfrom(8192)
			print 'Message from %s' % (address[0])
			print 'Message Broadcasted: '+ str(message)
			break		

		print "\nReceived message from intermediate node'", message,"'"
		# Decoding part
		# Decode the data from first file or source
		listOfCodedData1 = StringToBinaryList(message)
		listOfCodedData = ListOfCharToListofString(listOfCodedData1) 
				
		print ''			
		print 'Coded data got from intermediate node:'
		print listOfCodedData
				
		data11 = ListOfCharToListofString(data1list)
		print ''
		print 'Self Data:'
		print data11
				
		# Decode the message				
		DecodeFirst = ListDecode(listOfCodedData1, data11)

		print "Decode Data from node B"
		print DecodeFirst
		decodedlist1 = Result('B', DecodeFirst)
		print decodedlist1
				
		# The real decoded_data 
		a = ConcatListElements(decodedlist1)
		print 'The real data from source node B:'				
		print a
		break
		s.close()
# Close socket
UDPSock.close()


