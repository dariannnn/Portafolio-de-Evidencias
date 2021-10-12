import argparse
import socket
from cryptography.fernet import Fernet

# Arumentos
description = """ Modo de uso:
    ClienteTCP.py -msj [ mensaje a enviar ] """

parser = argparse.ArgumentParser(description='Port Scanning',
                                epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-msj", metavar='MSJ', dest="msj", 
                    help="mensaje a enviar", required=True)
params = parser.parse_args()

# Cifrado
clave = Fernet.generate_key()
cipher_suite = Fernet(clave)

# Almacenamiento de la clave
with open('clave.key', 'wb') as file:
    file.write(clave)

# Convertir argumento en bytes
msj = params.msj
msj_byte = msj.encode()

#Ciframos el mensaje
crypt_msj = cipher_suite.encrypt(msj_byte)
print("Mensaje enviado:\n", msj)

#Datos de conexion
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048

#Establecimiento de la conexion
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.connect((TCP_IP, TCP_PORT))
skt.send(crypt_msj)
res = skt.recv(BUFFER_SIZE).decode()
skt.close()

print("Respuesta recibida: ", res)
