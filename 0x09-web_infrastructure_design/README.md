# 0x09. Web infrastructure design

The general purpose of the project is that each student de able to draw a diagram covering the web stack you built with the sysadmin/devops track projects and then able to explain what each component is doing.

## 0. Simple web stack

Design a one server web infrastructure that hosts the website that is reachable via www.foobar.com.

### What is a server

In the computer world, a program that offers a series of services is called a server (answering a client's call), a computer on which all the programs work, technically a server delivers information or is used for another process.

* Web server: They store html files of a page and provide them to the client, transferring the files through the browser.

### What is the role of the domain name
* Hosting: A computer that is always on, is like a drawer in which the web page that is identified with the IP is located.
* Domain: A name example.com that can be configured to redirect and bring that name to a web page
### What type of DNS record www is in www.foobar.com
* DNS: is a server is a table relate between a domain and an IP
records A and AAAA
### What is the role of the web server
Store html files of a page and provide them to the client, transferring the files through the browser.
### What is the role of the application server
An application server is a server specifically designed to run applications. The "server" includes both hardware and software that provide an environment for programs to run.
An application server serves dynamic content to the end users using different protocols including HTTP. It’s a software framework which provides all the facilities required to create and run both web based and enterprise based applications. it is best suited for serving dynamic content and transferring applications from one device to another.
* An application server provides the processing power and memory to run these applications in real time.
### What is the role of the database
Is the term used to refer to the back-end system of a database application using client/server architecture. Based on the client requirement the database server plans and their platform will change.
### What is the server using to communicate with the computer of the user requesting the website
Web browser

## Distributed web infrastructure

Design a three server web infrastructure that hosts the website www.foobar.com.

### For every additional element, why you are adding it
### What distribution algorithm your load balancer is configured with and how it works
### Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
### How a database Primary-Replica (Master-Slave) cluster works
### What is the difference between the Primary node and the Replica node in regard to the application