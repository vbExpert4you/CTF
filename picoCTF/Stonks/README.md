#   Stonks

##  Description
I decided to try something no one else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! [vuln.c](nc mercury.picoctf.net 6989)

##  Hint
1.  Okay, maybe I'd believe you if you find my API key.

I found a writeup [here](https://dmfrsecurity.com/2021/04/07/picoctf-2021-stonks-writeup/)
He suspected a vulnerability in line 93 and used %p as an input to verify.  It prints the pointer location.
The explanation of %p is found [here](https://www.tutorialspoint.com/what-is-the-use-of-p-in-printf-in-c)

Running it and choosing to buy stonks and using %p as a token I get: 0x825c430

He had a bash script but running it on my machine runs it a few iterations and then says it's dumped the core.
Found this [Stack Overflow page](https://stackoverflow.com/questions/52952965/the-monitored-command-dumped-core)

I was looking at the weird output I was getting, which was different than what was on the writeup, and figured it might be the encoding my terminal is using. I ran $LANG at the prompt and it showed I was using UTF-8. Looking around on the web, I found [this article](https://github.com/microsoft/Terminal/issues/306) about problems with encoding in WSL.
