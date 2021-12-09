import hashlib # Importada a biblioteca hashlib

arquivo1 = 'a.txt' #para que esse projecto funcione precisamos desse arquivo
arquivo2 = 'b.txt' #E deste arquivo

hash1 = hashlib.new('ripemd160')   # hash1 recebe um construtor da hashlib.new que recebe uma string que define algoritimo que iremos usar definimos o algoritmo que sera usado pelo hash1, o nome do algoritmo eh ripemd160, que foi passado pelo new"qu eh o construtor"

hash1.update(open(arquivo1, 'rb').read())  # o update faz a compraracao, dentro dele encotimos a frase, ou o que sera passadado para ser comparado,o 'rb' eh para abrir o arquivo e ler dentro do hash, e usamos o metodo rb, que eh um metodo de leitura do binario

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read()) # update 2 gera para nos o hash 2

if hash1.digest() != hash2.digest() :#digest resume os dados passados pelo metodo update
    print(f' O arquivo: {arquivo1}  eh do arquivo: {arquivo2} ') #f' eh abreviacao do format
    print('O hash do arquivo a a.txt eh : ', hash1.hexdigest()) #imprimindo os respetivos hash's hezdigest que resume o hash hexadecimal e nos mostra o respetivo hash em hexa
    print('O hash do arquivo a b.txt eh', hash2.hexdigest())

else:
    print(f' O arquivo: {arquivo1}  eh do arquivo: {arquivo2}')
