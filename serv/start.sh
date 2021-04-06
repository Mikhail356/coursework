#!/bin/bash

for ((i = 1; i <= 5; i++ ))
do
rm log$i.txt
./darkhttpd $i --port 808$i --addr 127.0.0.1 --log log$i.txt &
done
wait
