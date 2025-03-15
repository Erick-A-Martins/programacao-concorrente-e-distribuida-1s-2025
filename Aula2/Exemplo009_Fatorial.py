# Cliente 

import socket

def iniciar_Cliente():
    # Configuração do cliente
    HOST = '127.0.0.1'
    PORT = 65432

    # Criando o socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as S:
        S.connect((HOST, PORT))
        
        S.sendall(b"fatorial")
        data = S.recv(1024)
        if data.decode() == "numero":
            S.sendall(b"7")
            data = S.recv(1024)
            print(f"Resposta: {data.decode()}")
        

if __name__ == "__main__":
    iniciar_Cliente()