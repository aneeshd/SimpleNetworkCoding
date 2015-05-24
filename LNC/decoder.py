#import random
import numpy
#from decimal import *

#Decodes using Gauss elimination method
def DecodeAtReceiver(listOfVector):
	a = numpy.array(listOfVector)
	rows=a.shape[0]
	columns=a.shape[1]
	#print a
	
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

# Decoding Part
#################################################################
def decode(encoded):
	listt = encoded
	numAns = len(listt[0])
	listAns =[]
	for listOfVector in listt:
		y=[int(x) for x in DecodeAtReceiver(listOfVector)]
		listAns.append(y)
	#print 'listAns', listAns

	decodeddata=[ [ix[n] for ix in listAns] for n in range(numAns) ]

	return decodeddata

from encoder import encode, SelfTest

if __name__=='__main__':
	# Encoded message got from network
	encodedstringreceived = SelfTest.gold

	listt = eval(encodedstringreceived)
	decodeddata=decode(listt)
	decodeddatalist1, decodeddatalist2, decodeddatalist3=decodeddata

	print ''
	print 'Decoded data: '
	print 'Data from source A'
	# Data in decimal value
	#print decodeddatalist1
	abc1 =  [chr(x) for x in decodeddatalist1]
	#print abc1
	decodeddata1 = ''.join(abc1)
	print decodeddata1
	assert decodeddata1==SelfTest.a

	print 'Data from source B'
	#print decodeddatalist2
	abc2 =  [chr(x) for x in decodeddatalist2]
	#print abc2
	decodeddata2 = ''.join(abc2)
	print decodeddata2
	assert decodeddata2==SelfTest.b

	print 'Data from source C'
	#print decodeddatalist3
	abc3 =  [chr(x) for x in decodeddatalist3]
	#print abc3
	decodeddata3 = ''.join(abc3)
	print decodeddata3
	assert decodeddata3==SelfTest.c
