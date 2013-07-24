SimpleNetworkCoding
===================
[A] Test Assumptions
		For network coding using XOR: 
		• Sources send string as message in wireless network.
		• Both the source data contains equal number of bits.
		• Encoding is done at intermediate node i.e. C 
		• Decoding is performed at both the source nodes A and B. 
		For network coding using RLNC: 
		• Both the source data contains equal number of bits.
		• Data is converted into a message of string before sending to other computer or node via sockets. 

[B] Test Environment: 
		The test was performed in a three laptops using both XOR and RLNC. Another tests need to be performed on a real butterfly network using network coding. The result of performing network coding using XOR is given as follow: 
		1. Source node A and source node B send the string "Network Coding is complex and hard" and "Performing experiments in Interlab" respectively to intermediate node C. 
		2. Node C performs XOR operations betweens bits from source A and source B and then broadcasts the coded message. 
		3. Nodes A and B decode the message from received coded data and data it contains. 
		4. Node A decodes message "Performing experiments in Interlab" from source node B and node B decodes message "Network Coding is complex and hard" from source node A.

[C] Result: 
		The result of performing network coding using RLNC is given as follow: 
		[1] Source node S collects three equal string messages from nodes A, B and C. 
		[2] Strings are converted into its equivalent ASCII value and then S performs network coding and creates three equations using random linear coding. 
		[3] The values of the coefficients of equation (encoding vectors) along with summation value (encoded data) are stored on a list and that list is converted to coded strings. 
		[4] The coded strings are sent to the decoding node via socket. 
		[5] Decoding node receives the coded message via socket and converts the string message into list of integer values and performs Gauss Elimination method to get ASCII values of messages of all the nodes. 
		[6] Converts ASCII values to its equivalent characters and append them to get the required message string from all the source nodes. 

[D] Limitations
		Some of the limitations of the test performed are as follows: 
		[1] This test is only limited to the sharing of a message string but not for the file. 
		[2] The source nodes send message string to intermediate node which assumes that the obtained strings are equal in size in order to perform network coding. 
		[3] Sometimes, coefficients for encoding vectors might be same which creates problem in solving Matrix using Gauss Elimination method. 
