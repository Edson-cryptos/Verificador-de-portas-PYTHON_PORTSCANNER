import ipaddress #para nos permitir trabalhar com ip's

#ip
#ip = '127.0.0.0'  #com a biblioteca ipaddress conseguimos transformar uma string em ip
#endereco = ipaddress.ip_address(ip) # para imprimir em formato de ip, recebe da biblioteca ip address o metodo ip_address
#print(endereco + 256) #para chegar a .1, estamos imprimindo e ao mesmo tempo adicionando + 256

#rede
ip = '192.168.0.0/0'  #com a biblioteca ipaddress conseguimos transformar uma string em ip
rede = ipaddress.ip_network(ip, strict=False) # Com strict=false validamos um ip, se corremos uma rede nao reconhecida nao sera corrida

for ip in rede:  #vai imprimir todos enderecos de ip do endereco 24* a rede que nos colocarmos
    print(rede)
