import os

ip_ou_host = input("Digite o Ip ou host a ser verificado: ")

os.system('ping -n 6 {}'.__format__(ip_ou_host)) ##tras ao sistema que podem ser usados