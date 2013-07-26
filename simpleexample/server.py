# Server program: Decoder
import random
import numpy
from decimal import *

def StringDecodedToListof4(astring):
	Decodedlist = []	
	c = astring.replace("], [", ', ')
	d = c.replace("[[", '[')
	e = d.replace("]]", ']').replace("]], [[", ',')
	f = e.replace(", ", ',')
	print f
	f = e.split(',')
	for x in f:
		y = x.strip('][ ')
		z = float(y)
		Decodedlist.append(z)
	listOfEqns = split(4, Decodedlist)
	return listOfEqns

def ConcatListElements(alist):
	p = ''	
	for x in alist:
		p += x
	return p
def split(n, iter, fill=None):
    return [iter[i:i+n] + [fill] * (i + n - len(iter))
            for i in xrange(0, len(iter), n)]

def ListOfIntToListOfString(alist):
	iList = []
	for x in alist:
		iList.append(chr(x))	
	return iList

#Decodes using Gauss elimination method
def DecodeAtReceiver(listOfVector):
	a = numpy.array(listOfVector)
	rows=a.shape[0]
	columns=a.shape[1]
	print(a)
	answer = numpy.zeros(rows)
	# Eliminating variables
	for i in numpy.arange(0,columns): #variable to eliminate
	   for j in numpy.arange(i+1,rows): #rows to eliminate said variable from
	     tmp=a[i]*(-a[j][i]/a[i][i]) #multiply row
	     a[j]=tmp+a[j] #add
	# Back substitute
	for i in (numpy.arange(rows).shape[0]-numpy.arange(rows)-1):
	   if(i<columns-2):
	     a[i][columns-1]=a[i][columns-1]-(sum(a[i])-a[i][i]-a[i][columns-1])
	 
	   #calculate ith variable
	   answer[i]=a[i][columns-1]/(a[i][i])
	   #substitute variable by
	   #multiply rows starting with i-1, column i by answer[i]
	   for j in numpy.arange(0,i):
	     a[j][i]=a[j][i]*answer[i]
	return answer

from socket import *

# Set the socket parameters
host = "localhost"
port = 21567
buf = 300000
addr = (host,port)

# Create socket and bind to address
UDPSock = socket(AF_INET,SOCK_DGRAM)
UDPSock.bind(addr)

# Encoded message got from network 
encodedstringreceived = ''

# Receive messages
while 1:
	data,addr = UDPSock.recvfrom(buf)
	if not data:
		print "Client has exited!"
		break
	else:
		print "\nReceived message '", data,"'"
		encodedstringreceived = data
		break

# Close socket
UDPSock.close()
print encodedstringreceived

# Decoding Part
#################################################################
decodeddatalist1 = []
decodeddatalist2 = []
decodeddatalist3 = []
decodeddatalist4 = []

# list containing decoded packets
encoded_list = StringDecodedToListof4(encodedstringreceived)
print 'encoded list'
print encoded_list

listt = split(3, encoded_list)
print listt
listAns =[]
for listOfVector in listt:
	decoded = DecodeAtReceiver(listOfVector)
	print decoded

	y = []
	for x in decoded: 
		y.append(int(round(x, 0)))
	print y
	listAns.append(y)
print listAns

for ix in listAns:
	#print ix
	# decodeddata1 list
	decodeddatalist1.append(ix[0])
	# decodeddata2 list
	decodeddatalist2.append(ix[1])
	# decodeddata3 list
	decodeddatalist3.append(ix[2])

print ''
print 'Decoded data: '
print 'Data from source A'
# Data in decimal value
print decodeddatalist1
abc1 =  ListOfIntToListOfString(decodeddatalist1)
print abc1
decodeddata1 = ConcatListElements(abc1)
print decodeddata1

print 'Data from source B'
print decodeddatalist2
abc2 = ListOfIntToListOfString(decodeddatalist2)
print abc2
decodeddata2 = ConcatListElements(abc2)
print decodeddata2

print 'Data from source C'
print decodeddatalist3
abc3 = ListOfIntToListOfString(decodeddatalist3)
print abc3
decodeddata3 = ConcatListElements(abc3)
print decodeddata3










