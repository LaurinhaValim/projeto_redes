import socket


HOST = '127.0.0.1' 
PORT = 8080       

estoque_notebook = 10
preco_notebook = 1500.00


servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()

print("=========================================")
print(f" Servidor Marketplace Ativo na Porta {PORT}")
print("=========================================")

while True:
    
    conexao, endereco = servidor.accept()
    print(f"[SERVIDOR] Conectado por {endereco}")
    
   
    requisicao = conexao.recv(1024).decode('utf-8')
    print(f"[SERVIDOR] Requisição recebida: {requisicao}")
    
   
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
        
   
    conexao.sendall(resposta.encode('utf-8'))
    
  
    conexao.close()