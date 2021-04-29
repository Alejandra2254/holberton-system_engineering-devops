# 0x12. Web stack debugging #2

The power of debugging is is only acquired with experience but there are some tricks to help. For example:
Ask questions until you find the issue :confused:.

1. For web server:
    * If you installed a web server
    * is the web serve started?
    * On what port should it listen?
    * Is it actually listening on this port?
    * It is listening on the correct server IP? 
    * Is there a firewall enabled?
    * Can I connect to the HTTP port from the location I am browsing from? 

2. For the machine level:
    * Does the server have free disk space?
    * Is the server able to keep up with CPU load? 
    * Does the server have available memory?
    * Are the server disk(s) able to keep up with read/write IO? 

3. For netwotk issue:
    * Does the server have the expected network interfaces and IPs up and running?
    * Does the server listen on the sockets that it is supposed to? 
    * Can you connect from the location you want to connect from, to the socket you want to connect to?
    * Does the server have the correct firewall rules? 

4. For the software:
    * Is the software started?
    * Is the software process running?
    * Is there anything interesting in the logs? 

Debugging is fun :confused: