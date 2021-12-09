import itertools    #importando a biblioteca itertools

entrada = input("Introduza o texto que deve ser transformado: ")

saida = itertools.permutations('abcd', 4)       # Estamos atribuindo a variavel saida o construtor itertools que implementa
                                                 # o metodo permutation que permuta o texto introduzido na variavel entrada,o 4 define a quantidade das combinações a serem feitas, utilizando os caracteres abcd.

# print(saida)
for i in saida:   # Percorendo cada caracter do resultado saida
    print(''.join(i))  # imprimindo o caracter e juntando ao outro, até que formem 4 caracteres