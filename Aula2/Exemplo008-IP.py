import socket # Se necessário, usar pip install socket

hostname = socket.gethostname()
ip_local = socket.gethostbyaddr(hostname)

print(f"Nome do Host: {hostname}")
print(f"Endereço do host: {ip_local}")