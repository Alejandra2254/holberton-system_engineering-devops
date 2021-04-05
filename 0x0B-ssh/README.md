# 0x0B. SSH

General
## What is a server

A server is a piece of computer hardware or software (computer program) that provides functionality for other programs or devices, called "clients". This architecture is called the client–server model. Servers can provide various functionalities, often called "services", such as sharing data or resources among multiple clients, or performing computation for a client. 

## Where servers usually live

A Data Center is, as the name implies, a "data center" or "Data Processing Center" (CPD). This definition encompasses dependencies and associated systems through which:

The data are stored, processed and distributed to the personnel or processes authorized to consult and/ or modify them.
Servers on which this data is hosted are maintained in an optimal operating environment.

## What is SSH

SSH is a secure protocol used as the primary means of connecting to Linux servers remotely. It provides a text-based interface by spawning a remote shell. After connecting, all commands you type in your local terminal are sent to the remote server and executed there.

## How to create an SSH RSA key pair

To generate an RSA key pair on your local computer, type:

```
$ssh-keygen
```
```
Output
Generating public/private rsa key pair.
Enter file in which to save the key (/home/demo/.ssh/id_rsa):
```
This prompt allows you to choose the location to store your RSA private key. Press ENTER to leave this as the default, which will store them in the .ssh hidden directory in your user’s home directory. Leaving the default location selected will allow your SSH client to find the keys automatically.
```
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
```
The next prompt allows you to enter a passphrase of an arbitrary length to secure your private key. By default, you will have to enter any passphrase you set here every time you use the private key, as an additional security measure. Feel free to press ENTER to leave this blank if you do not want a passphrase. Keep in mind though that this will allow anyone who gains control of your private key to login to your servers.

If you choose to enter a passphrase, nothing will be displayed as you type. This is a security precaution.
```
Output
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
The key fingerprint is:
8c:e9:7c:fa:bf:c4:e5:9c:c9:b8:60:1f:fe:1c:d3:8a root@here
The key's randomart image is:
+--[ RSA 2048]----+
|                 |
|                 |
|                 |
|       +         |
|      o S   .    |
|     o   . * +   |
|      o + = O .  |
|       + = = +   |
|      ....Eo+    |
+-----------------+
```
This procedure has generated an RSA SSH key pair, located in the .ssh hidden directory within your user’s home directory. These files are:

~/.ssh/id_rsa: The private key. DO NOT SHARE THIS FILE!
~/.ssh/id_rsa.pub: The associated public key. This can be shared freely without consequence.

## How to connect to a remote host using an SSH RSA key pair

To connect to a remote server and open a shell session there, you can use the command.ssh

The simplest form assumes that your username on your local machine is the same as that on the remote server. If this is true, you can connect using:
```
$ssh remote_host
``` 
If your username is different on the remoter server, you need to pass the remote user’s name like this:
```
$ssh username@remote_host
```
Your first time connecting to a new host, you will see a message that looks like this:
```
The authenticity of host '111.111.11.111 (111.111.11.111)' can't be established.
ECDSA key fingerprint is fd:fd:d4:f9:77:fe:73:84:e1:55:00:ad:d6:6d:22:fe.
Are you sure you want to continue connecting (yes/no)? yes
Type to accept the authenticity of the remote host.yes
```
If you are using password authentication, you will be prompted for the password for the remote account here. If you are using SSH keys, you will be prompted for your private key’s passphrase if one is set, otherwise you will be logged in automatically.

## The advantage of using #!/usr/bin/env bash instead of /bin/bash

The use of /usr/bin/env is a clever hack used to search the command in the PATH