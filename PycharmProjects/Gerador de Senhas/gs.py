import random

import string

tamanho = int(input('digite o tamanho de senhas que voce deseja'))

#tamanho = 16 # vai receber o tamanho da senha que vou criar, em boas praticas de SI optamos por 16 careters
chars = string.ascii_letters + string.digits + ' cc!@#$%'# asci.letters nos permite ter letras maisculasa e menusculas, recebe a estrutura da senha que sera criada

rnd = random.SystemRandom() #os. gera senhas aleatorias atraves das senhas que o so forneceu

print(''.join(rnd.choice(chars) for i in range (tamanho))) #fazemos a juncao do rnd.choice(chars)'retorna uma lista com os caracteres randomico' e pega cada caracter randomico gerado pelo 'chars' que passa um caracter randomico, para cada i no range tamanho vai gerar um novo caraceter aleatorio, conforme vai gerando, deve gerar ate 16 caracteres
