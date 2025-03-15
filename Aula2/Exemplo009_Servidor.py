# Servidor

import socket
from datetime import datetime

def fibonacci(N):
    if N == 1 | N == 2:
        return 1
    else:
        return fibonacci(N - 1) + fibonacci(N - 2)
    

def iniciar_servidor():
    # Configuração do servidor
    HOST = '127.0.0.1' # Endereço local
    PORT = 65432       # Porta para comunicação

    # Criando o socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT)) # Associa o socket ao endereço e porta
        s.listen()           # Habilita o servidor para aceitar conexões

        print(f"Servidor executando em {HOST}:{PORT}")

        while True:
            # Aguarda uma conexão
            conn, addr = s.accept()

            with conn:
                print(f"Conectado por {addr}")
                while True:
                    # Recebe dados do cliente
                    data = conn.recv(1024)

                    if not data:
                        break

                    # Verifica se o cliente pediu a data e hora
                    if data.decode().strip().lower() == "data e hora":
                        # Obtém data e hora atuais
                        agora = datetime.now().strftime("%Y - %m - %d  %H:%M:%S")
                        resposta = f"Data e hora: {agora}"
                        conn.sendall(resposta.encode())

                    elif data.decode().strip().lower() == "bom dia":
                        resposta = f"Olá, {addr}. Bom dia para você também!!!"
                        conn.sendall(resposta.encode())

                    # Cálculo Fatorial
                    elif data.decode().strip().lower() == "fatorial":
                        resposta = "numero"
                        conn.sendall(resposta.encode())
                        data = conn.recv(1024)
                        N = int(data.decode())
                        Fatorial = 1
                        for x in range(N):
                            Fatorial = Fatorial * (x + 1)
                        resposta = f"O fatorial de {N} é {Fatorial}."
                        conn.sendall(resposta.encode())

                    # Cálculo Fiboncci
                    elif data.decode().strip().lower() == "fibonacci":
                        resposta = "numero"
                        conn.sendall(resposta.encode())
                        data = conn.recv(1024)
                        N = int(data.decode())
                        F = fibonacci(N)
                        resposta = f"O {N}* termo da serie de fibonacci é {F}."
                        conn.sendall(resposta.encode())

                    else:
                        resposta = "Mensagem inválida!"
                        conn.sendall(resposta.encode())
                    
if __name__ == "__main__":
    iniciar_servidor()