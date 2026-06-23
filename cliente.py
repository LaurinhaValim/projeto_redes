import socket

HOST = '127.0.0.1'
PORT = 8080

def enviar_comando(comando):
    try:
        # Criando o socket TCP do cliente
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Conectando ao servidor
        cliente.connect((HOST, PORT))
        
        # Envia o comando escolhido pelo usuário
        cliente.sendall(comando.encode('utf-8'))
        
        # Recebe a resposta do servidor
        resposta = cliente.recv(1024).decode('utf-8')
        print(f"\n[SERVIDOR]: {resposta}\n")
        
        cliente.close()
    except ConnectionRefusedError:
        print("\n[ERRO]: Não foi possível conectar ao servidor. Ele está rodando?\n")

# Menu de interação
while True:
    print("--- MARKETPLACE VIA SOCKETS (PYTHON) ---")
    print("1. Listar Produtos Disponíveis")
    print("2. Comprar 1 Unidade de Notebook")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        enviar_comando("LISTAR")
    elif opcao == "2":
        enviar_comando("COMPRAR")
    elif opcao == "3":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!\n")