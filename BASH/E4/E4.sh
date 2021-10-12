#!/bin/bash 

echo "Empieza script"

if type -t wevtutil &> /dev/null 

then 

    OS=MSWin 

elif type -t scutil &> /dev/null 

then 

    OS=macOS 

else 

    OS=Linux 

fi 

echo $OS>>ScriptE4Texto.txt



function is_alive_ping() { 

  ping -c 1 $1 > /dev/null 2>&1 

  [ $? -eq 0 ] && echo "Node with IP: $i is up.">>ScriptE4Texto.txt  

} 

for i in 192.168.100.{1..255}

do
    is_alive_ping $i & disown
    
    
    host=$i 
    firstport=10 
    lastport=500

    function portscan { 

    for ((counter=$firstport; counter<=$lastport; counter++)) 

    do 

        (echo >/dev/tcp/$host/$counter) > /dev/null 2>&1 && echo "$counter open">>ScriptE4Texto.txt
    done 

    } 

    portscan
    
done 

echo "Termina Script"
