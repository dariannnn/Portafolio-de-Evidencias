import argparse
import socket
from cryptography.fernet import Fernet

#Datos de conexion
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048

#Establecimiento de la conexion
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.bind((TCP_IP, TCP_PORT))
skt.listen(1)
(conn, addr) = skt.accept()
print('Dirección de conexión: ', addr)
while True:
    crypt_msj = conn.recv(BUFFER_SIZE)
    conn.send(b"Enterado. Bye!")
    break
conn.close()

#Cifrado
with open('clave.key', 'rb') as file:
    clave = file.read()
cipher_suite = Fernet(clave)

msjByte = cipher_suite.decrypt(crypt_msj, None)
msj = msjByte.decode()
print("Mensaje recibido:\n", msj)
