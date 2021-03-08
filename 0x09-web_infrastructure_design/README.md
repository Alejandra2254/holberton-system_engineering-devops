# 0x09. Web infrastructure design

The general purpose of the project is that each student de able to draw a diagram covering the web stack you built with the sysadmin/devops track projects and then able to explain what each component is doing.

## Resources:books:
Read or watch:
* [What is a database](https://intranet.hbtn.io/rltoken/XLIOfzfuaxPQu39VQ0TLtw)
* [What’s the difference between a web server and an app server?](https://intranet.hbtn.io/rltoken/Nb8B47Y2D8SLqQMOKVoQyQ)
* [DNS record types](https://intranet.hbtn.io/rltoken/oAxMObOTX3Wx4KH_hCNw3g)
* [Single point of failure](https://intranet.hbtn.io/rltoken/wYpewVpIp9PSqqL27RPafg)
* [How to avoid downtime when deploying new code](https://intranet.hbtn.io/rltoken/Mlvynt0OgLQXrxjrC5Wlnw)
* [High availability cluster (active-active/active-passive)](https://intranet.hbtn.io/rltoken/POX3jE0S6TChQHSYQraYeQ)
* [What is HTTPS](https://intranet.hbtn.io/rltoken/N4BwU4wYDNW02kdzMiekFw)
* [What is a firewall](https://intranet.hbtn.io/rltoken/HrYI70d_nxUPZeufjUYzIw)


## 0. Simple web stack

Design a one server web infrastructure that hosts the website that is reachable via www.foobar.com.

### What is a server
In the computer world, a program that offers a series of services is called a server (answering a client's call), a computer on which all the programs work, technically a server delivers information or is used for another process.

* Web server: They store html files of a page and provide them to the client, transferring the files through the browser.

### What is the role of the domain name
* Hosting: A computer that is always on, is like a drawer in which the web page that is identified with the IP is located.
* Domain: A name example.com that can be configured to redirect and bring that name to a web page

### What is the role of the web server
Store html files of a page and provide them to the client, transferring the files through the browser.

### What is the role of the application server
An application server is a server specifically designed to run applications. The "server" includes both hardware and software that provide an environment for programs to run.
An application server serves dynamic content to the end users using different protocols including HTTP. It’s a software framework which provides all the facilities required to create and run both web based and enterprise based applications. it is best suited for serving dynamic content and transferring applications from one device to another.
* An application server provides the processing power and memory to run these applications in real time.
### What is the role of the database
Is the term used to refer to the back-end system of a database application using client/server architecture. Based on the client requirement the database server plans and their platform will change.

## 1. Distributed web infrastructure

Design a three server web infrastructure that hosts the website www.foobar.com.

### What distribution algorithm your load balancer is configured with and how it works
* Load Balancer:  acts as the "Transit Officer" in front of its servers and routes client requests across all servers to satisfy those requests in a way that maximizes speed and capacity to ensure that no server is overloaded, as saturation could affect performance.
* Round Robin - Requests are distributed across the pool sequentially.
* Least Connections - A new request is sent to the server based on the number of current connections from clients. The capacity of each server is taken into account to determine the number of connections.
* IP Hash - The client's IP address is used to determine which server receives the request.

### How a database Primary-Replica (Master-Slave) cluster works
Master-slave replication enables data from one database server (the master) to be replicated to one or more other database servers (the slaves). The master logs the updates, which then ripple through to the slaves. 

## 2. Secured and monitored web infrastructure

Design a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.

### What are firewalls for
Computer program that controls the access of a computer to the network and of elements of the network to the computer, for security reasons.
### What monitoring is used for
a program that observes and regulates and controls or verifies the operations of a data-processing system

## Author
* **Alejandra Higuera** - [Alejandra2254](https://github.com/Alejandra2254/)
