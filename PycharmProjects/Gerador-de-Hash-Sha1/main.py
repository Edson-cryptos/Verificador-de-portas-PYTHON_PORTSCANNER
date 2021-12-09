import hashlib

senha = input("Digite a senha: ")

saida = hashlib.sha1(senha.encode('utf - 8'))
print("A senha normal é: ", senha, '\nE em hash sha1 é: ', saida.hexdigest())
