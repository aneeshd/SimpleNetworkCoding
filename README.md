SimpleNetworkCoding
===================
There are three simple example to demonstrate network coding principles:

[1] "3nodes" shows simple example to perform XOR operations betweens bits from source A and bits from source B at the intermediate node C.

[2] "LNC" is simple example to show how to perform linear network coding.

[3] "simpleexample" shows how to perform encoding and decoding in simple way.

Limitations
Some of the limitations of the test performed are as follows: 

[1] This tests are only limited to the sharing of a message string but not for the file. 

[2] The source nodes send message string to intermediate node which assumes that the obtained strings are equal in size in order to perform network coding. 

[3] Sometimes in LNC, coefficients for encoding vectors might be same which creates problem in solving Matrix using Gauss Elimination method. 
