import hashlib

string = input("Digite  o texto a ser gerado:")

menu = int(input('''**** Menu - escolha o tipo de hash ***
             1) Md5
             2) SHA1
             3) SHA256
             4) SHA512
              Digite o numero do hash a ser gerado: '''))
if menu == 1:
    resultado = hashlib.md5(string.encode('utf - 8'))
    print("o Hash md5 da string eh: ", string, 'eh: ', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf - 8'))
    print("o Hash sha1 da string eh: ", string, 'eh: ', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf - 8'))
    print("o Hash sha256 da string eh:", string, 'eh: ', resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf - 8'))
    print("o Hash sha512 da string eh:", string, 'eh: ', resultado.hexdigest())
else:
    print('algo de certo deu errado')

#resultado = hashlib.md5(b'Phyton Security') #o  resulatdo recebe da biblioteca hashlib o tipo de hash md5 onde passamos uma string (python secu...) o b' converte a string em bytes
#resultado = hashlib.md5(string.encode('utf - 8'))
#print("o Hash da string eh:", resultado.hexdigest())