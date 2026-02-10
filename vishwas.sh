#!bin/bash
echo " Parent PID:$$"
sleep 20 & 
ps -o pid
ps -o ppid
ps -o cmd
