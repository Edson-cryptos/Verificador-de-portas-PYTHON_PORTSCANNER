import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket Criado com Sucesso')

host = 'localhost' # criamos uma variavel host para armazenar o host
port = 5432 #criamos uma variavel port para armazenar a porta

s.bind((host, port))  #faz a ligacao entre o cliente servidor atraves do host, e da porta
mensagem = '\nServidor: Olaaaa cliente e tudo bem?'

while 1:  # enquanto isso for 1
    dados, end = s.recvfrom(4096) # vai receber 4096 bytes atraves do objecto de conexao e vai guardar dentro do endereco e dentro de dados byte e e end

    if dados:   # Se o dados tiver alguma coisa vai printar, vai imprimir a mensagem
        print('Servidor enviando mensagem....')
        s.sendto(dados + (mensagem.encode()), end) # vai enviar dados e a mensagem e 4096 bytes