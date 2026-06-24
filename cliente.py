import socket

HOST = '127.0.0.1'
PORT = 8080

def enviar_comando(comando):
    try:
        
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
       
        cliente.connect((HOST, PORT))
        
    
        cliente.sendall(comando.encode('utf-8'))
        
   
        resposta = cliente.recv(1024).decode('utf-8')
        print(f"\n[SERVIDOR]: {resposta}\n")
        
        cliente.close()
    except ConnectionRefusedError:
        print("\n[ERRO]: Não foi possível conectar ao servidor. Ele está rodando?\n")


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