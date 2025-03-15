# Cliente 

import socket

def iniciar_Cliente():
    # Configuração do cliente
    HOST = '127.0.0.1'
    PORT = 65432

    # Criando o socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as S:
        S.connect((HOST, PORT))
        
        S.sendall(b"bom dia")
        data = S.recv(1024)
        print(f"Resposta do servidor: {data.decode()}")

        # Envia a solicitação ao servidor
        S.sendall(b"data e hora")
        # Recebe a resposta do servidor
        data = S.recv(1024)
        # Exibe a resposta
        print(f"Resposta do servidor: {data.decode()}")

if __name__ == "__main__":
    iniciar_Cliente()