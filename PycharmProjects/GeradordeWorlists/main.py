import itertools

string = input("string a ser permutada: ")

resultado = itertools.permutations(string, len(string)) #o len pega o tamanho da string que for passad para ser permutada

#resultado = itertools.permutations('abcdef', 5) # o resultado recebe do ietertools o metodo permutatioon

for i in resultado: #para cada caracter no resultado
    print(''.join(i)) #imprime o caracter e faz um join