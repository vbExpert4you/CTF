#   Stonks

##  Description
I decided to try something no one else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! [vuln.c](nc mercury.picoctf.net 6989)

##  Hint
1.  Okay, maybe I'd believe you if you find my API key.

I found a writeup [here](https://dmfrsecurity.com/2021/04/07/picoctf-2021-stonks-writeup/)
He suspected a vulnerability in line 93 and used %p as an input to verify.  It prints the pointer location.
The explanation of %p is found [here](https://www.tutorialspoint.com/what-is-the-use-of-p-in-printf-in-c)

