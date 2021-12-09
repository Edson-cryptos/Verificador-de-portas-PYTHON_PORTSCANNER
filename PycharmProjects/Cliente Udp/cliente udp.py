import socket #importando socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #crie um objecto s

print('Cliente Socket Criado com Sucesso!!')  #mandei imprimir a mensagem de criado com sucesso

host = 'localhost'  #disse que o host sera local host
porta = 5433 #disse que a porta do cliente eh 5433
mensagem = 'Ola servidor, na boa' # mandei a mensagem para p servidor

try:  # tentado enviar e receber a mensagem
    print('Cliente:' + mensagem) #
    s.sendto(mensagem.encode(), (host, 5432)) # empacota a mensagem e envia para o host que o localhost na porta 5432, que sera a porta que o servidor estara ouvindo

    dados, servidor = s.recvfrom(4096) #o recebe tanto dados como servidor vao receber do servidor uma resposta de 4096 bytes
    dados = dados.decode() #desempacota os dados mandados pelo servidor
    print("Cliente: " + dados) # imprime os dados desempacoctados
finally:
    print('Cliente: Fechando a conexao')
    s.close() #fecha a conexao para que a mesma nao fique em loop