#!/bin/bash
for ((i = 1; i <= 5; i++ ))
do
rm log$i.txt
done
./darkhttpd 1 --port 8081 --addr 127.0.0.1 --log log1.txt & 
./darkhttpd 2 --port 8082 --addr 127.0.0.1 --log log2.txt & 
./darkhttpd 3 --port 8083 --addr 127.0.0.1 --log log3.txt & 
./darkhttpd 4 --port 8084 --addr 127.0.0.1 --log log4.txt &
./darkhttpd 5 --port 8085 --addr 127.0.0.1 --log log5.txt
