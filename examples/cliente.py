# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 18:45:08 2020

@author: Antonio Fernández Ares (antares@ugr.es)

Ejemplo Sockets: Cliente
"""

import socket

host = socket.gethostname()
port = 12345

BUFFER_SIZE = 1024
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
	while(True):
		socket_tcp.connect((host,port))
		while(True):
			print("Introduzca los datos a mandar")
			MESSAGE = input() #Esto es lo que vamos a envia
			socket_tcp.send(MESSAGE.encode("utf-8"))
			data = socket_tcp.recv(BUFFER_SIZE)
			print(data.decode("utf-8"))