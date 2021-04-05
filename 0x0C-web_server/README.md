# 0x0C. Web server

### General
## What is the main role of a web server

The main job of a web server is to display website content through storing, processing and delivering webpages to users. Besides HTTP, web servers also support SMTP (Simple Mail Transfer Protocol) and FTP (File Transfer Protocol), used for email, file transfer and storage.

## What is a child process

A child process is a process created by another process. The creator process is properly called the “parent process”. The benefit of a child process is that it can start or stop at will without affecting the parent process. The child process is, however, is typically dependent on the parent process. If the parent process dies, the child process becomes an orphan process.

## Why web servers usually have a parent process and child processes

Apache creates child processes (or children, if you prefer) whenever the number of requests (web page accesses from users) exceeds the maximum allowed number of requests. When the maximum number of child process requests is exceeded, another child process spawns.

## What are the main HTTP requests

A GET request retrieves data from a web server by specifying parameters in the URL portion of the request. This is the main method used for document retrieval.

### DNS

## What DNS stands for

DNS is, in simple words, the technology that translates human-adapted, text-based domain names to machine-adapted, numerical-based IP