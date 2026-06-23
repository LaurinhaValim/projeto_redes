import socket

# Configurações do servidor
HOST = '127.0.0.1'  # Endereço IP local (localhost)
PORT = 8080        # Porta que o servidor vai escutar

# Simulação do banco de dados do marketplace
estoque_notebook = 10
preco_notebook = 1500.00

# Criando o socket TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()

print("=========================================")
print(f" Servidor Marketplace Ativo na Porta {PORT}")
print("=========================================")

while True:
    # Aguarda e aceita uma conexão do cliente
    conexao, endereco = servidor.accept()
    print(f"[SERVIDOR] Conectado por {endereco}")
    
    # Recebe a requisição do cliente (máximo 1024 bytes) e decodifica para texto
    requisicao = conexao.recv(1024).decode('utf-8')
    print(f"[SERVIDOR] Requisição recebida: {requisicao}")
    
    # Processa as regras de negócio
    if requisicao == "LISTAR":
        resposta = f"Produto: Notebook | Estoque: {estoque_notebook} | Preço: R$ {preco_notebook:.2f}"
    elif requisicao == "COMPRAR":
        if estoque_notebook > 0:
            estoque_notebook -= 1
            resposta = f"Compra realizada com sucesso! Estoque atual: {estoque_notebook}"
        else:
            resposta = "Erro: Produto esgotado!"
    else:
        resposta = "Comando inválido."
        
    # Envia a resposta de volta para o cliente (convertida em bytes)
    conexao.sendall(resposta.encode('utf-8'))
    
    # Fecha a conexão atual
    conexao.close()