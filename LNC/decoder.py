import numpy
from encoder import encode, fullencode, code1, linearCode, xorCode, SelfTest

DEBUG=False

#Decodes using Gauss elimination method
def GaussEliminationLinear(listOfVector):
	a = numpy.array(listOfVector)
	rows=a.shape[0]
	columns=a.shape[1]
	if DEBUG: print '---------------'
	if DEBUG: print a
	
	answer = numpy.zeros(rows)
	
	# Eliminating variables
	if DEBUG: print '- eliminate'
	for i in numpy.arange(0,columns): #variable to eliminate
		for j in numpy.arange(i+1,rows): #rows to eliminate said variable from
			tmp=a[i]*(-a[j][i]/a[i][i]) #multiply row
			a[j]=tmp+a[j] #add
			if DEBUG: print a, i, j, tmp
	
	# Back substitute
	if DEBUG: print '- backsub'
	for i in (numpy.arange(rows).shape[0]-numpy.arange(rows)-1):
		answer[i]=a[i][columns-1]/(a[i][i])
		if DEBUG: print '***', i, '=', answer[i]
		for j in numpy.arange(0,i):
			a[j][columns-1]-=a[j][i]*answer[i]
			a[j][i]=0
			if DEBUG: print a, i, j

	if DEBUG: print a, answer
	return answer

def GaussEliminationXor(listOfVector):
	l = [ [ int(x) for x in y] for y in listOfVector ]
	a = numpy.array(l)
	rows=a.shape[0]
	columns=a.shape[1]
	if DEBUG: print '---------------'
	if DEBUG: print a
	
	answer = [0]*rows
	
	# Eliminating variables
	if DEBUG: print '- eliminate'
	for i in numpy.arange(0,columns): #variable to eliminate
		for j in numpy.arange(i+1,rows): #rows to eliminate said variable from
			if a[j][i]==0: continue
			tmp=a[i]
			a[j]=tmp ^ a[j] #add
			if DEBUG: print a, i, j, tmp
	
	# Back substitute
	if DEBUG: print '- backsub'
	for i in (numpy.arange(rows).shape[0]-numpy.arange(rows)-1):
		answer[i]=a[i][columns-1] #/(a[i][i])
		if DEBUG: print '***', i, '=', answer[i]
		for j in numpy.arange(0,i):
			a[j][columns-1] ^= a[j][i]*answer[i]
			a[j][i]=0
			if DEBUG: print a, i, j

	if DEBUG: print a, answer
	return answer

if code1==linearCode:
	print 'NOTE: Using linear code'
	decode1=GaussEliminationLinear
else:
	print 'NOTE: Using GF(2) code'
	decode1=GaussEliminationXor

# Decoding Part
#################################################################
def decode(encoded):
	listt = encoded
	numAns = len(listt[0])
	listAns =[]
	for listOfVector in listt:
		y=[int(x) for x in decode1(listOfVector)]
		listAns.append(y)
	#print 'listAns', listAns

	decodeddata=[ [ix[n] for ix in listAns] for n in range(numAns) ]

	return decodeddata

def fullreconstruct(coeffs, encoded):
	pass
	
if __name__=='__main__':
	# Encoded message got from network
	encodedstringreceived = SelfTest.gold

	listt = eval(encodedstringreceived)
	decodeddata=decode(listt)
	decodeddatalist1, decodeddatalist2, decodeddatalist3=decodeddata

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
