import os

import time

with open('hosts.txt') as file:    # vai abrir o arquivo hosts.txt
    dump = file.read()   #vai ler o arquivo

    #print(dump) #para ler o dump
    dump = dump.splitlines()  #eh para imprimir os ip's em linha recta

    for ip in dump:
        print('verificando o ip: ', ip)
        print('#' * 100)
        os.system('ping -n 2 {}'.format(ip)) #eh para ficar menos tempo a fazer o ping envia apenas dois pacotes
        print('#'*100)
        time.sleep(5) #determina o intervalo de tempo entre hosts no nosso caso sao 5s