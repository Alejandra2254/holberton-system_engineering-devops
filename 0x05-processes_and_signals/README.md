# 0x05. Processes and signals

## General

### What is a PID?
(process identification number) is a number that is automatically assigned to each process when it is created on a Unix.

*the PID, is always a positive integer.
*init, is the only process that will have always the same PID on any session and on any system, and is 1, beacuse is the first process on the system and the ancestor of all other processes.
*A very large PID does not necessarily mean that there are anywhere near that many processes on a system. This is because such numbers are often a result of the fact that PIDs are not immediately reused, in order to prevent possible errors.
could be exist 32,767 processes simultaneously on a system.

### What is a process?
A process is an executing (running) instance of a program.

### How to find a process’ PID?
Using the ps command or the pstree command.

### How to kill a process
There are various commands to kill a process ( kill, killall, pkill, top )

* killall: If you know the exact name of a process, and you know that it’s not running as another user and it is not in the Z or D states, then you can use this command directly.
* pkill: Sometimes, you only know part of a program’s name. Just like pgrep, pkill allows you to kill processes based on partial matches. For example, if you want to kill all processes containing the name apache in the name
* kill: Using the kill command is straightforward. Once you have found out the PID of the process that you want to kill, you can terminate it using the kill command.

### What is a signal
Signals are software interrupts. A robust program need to handle signals. This is because signals are a way to deliver asynchronous events to the application.

A user hitting ctrl+c, a process sending a signal to kill another process etc are all such cases where a process needs to do signal handling.

### What are the 2 signals that cannot be ignored
SIGKILL and SIGSTOP cannot be ignored. This is because these two signals provide a way for root user or the kernel to kill or stop any process in any situation .The default action of these signals is to terminate the process. Neither these signals can be caught nor can be ignored