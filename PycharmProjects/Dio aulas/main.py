lista = [1, 3, 7, 5]
lista_animal = ['cachoro', 'gato', 'elefante']

if 'lobo' in lista_animal:
    print('existe um lobo na lista')
else:
    print('nao existe um lobo na lista')
    lista_animal.append('lobo')
    print(lista_animal)

# lista_animal.pop(1)
# print(lista_animal)

lista_animal.sort()
lista.sort()
print(lista_animal)
print(lista)

lista_animal[0] = 'gaviao'
print(lista_animal)

tupla = (1,2,3,45,56)
print(tupla)
print(len(lista_animal))

lista_numerica = tuple(lista_animal)
print(type(lista_numerica))

