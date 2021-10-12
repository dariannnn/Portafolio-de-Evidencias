#!/bin/bash

#Irvin Martínez González
#Darian Michelle Orona Aguilar

echo 'Ingrese la API key:'
read -rs APIKEY

API-Request() {
#API key: cfccfca8a55b497f9f3c5b22a9cd132a
while read i; do 
    printf "Correo: $i\n"
    curl -H "hibp-api-key:$APIKEY" -H "user-agent: Studies" -isS "https://haveibeenpwned.com/api/v3/breachedaccount/$i" > test.txt

    if grep -q "HTTP/2 404" test.txt; then
        echo "Tu cuenta no ha sido vulnerada."
    #elif grep -q "HTTP/2 401" test.txt; then
    #    echo "Ha ocurrido un error con el request hacía la API."
    else 
        echo "Tu cuenta ha sido vulnerada en los siguientes servicios: "
        grep "Name" test.txt
    fi

    printf "\n";
done < correos.txt
}

API-Request
rm test.txt

