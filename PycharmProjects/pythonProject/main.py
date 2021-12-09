import os #Importa a biblioteca os (integra os programas e recursos do S.O

print('#' * 60)  #Imprimindo o # 60 x

ip_ou_host = input("Digite o Ip ou host a ser verificado: ") #criamos uma variavel que vai receber do usuario um ip

print('-' * 60)

os.system('ping -n 6 {}'.format(ip_ou_host)) ##tras ao sistema que podem ser usados, {} chama o atributo format, estamos o modolo system da biblioteca os, e estamos chamando um comando ping - n -num de pacotes que serao 6 {}

print('-' * 60)
