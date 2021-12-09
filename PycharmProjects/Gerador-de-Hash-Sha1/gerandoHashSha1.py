import hashlib

senha = input("Digite a senha: ")

saida = hashlib.sha1(senha.encode('utf - 8'))
print("O hash sha1 da senha e: ", senha, 'e: ', saida.hexdigest())
