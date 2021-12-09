from threading import Thread
import time

def carro(velicidade, piloto): #definimos a funcao carro1 e passamos o arqgumeto veloc
    trajecto = 0 #estamos dizendo que ele inicia no kilimentro 0
    while trajecto <= 100:
        #print('carro:', piloto, trajecto)  #imprime de forma desorganizada
        trajecto+=velicidade #fazemos o incremoento  do trajecto com a velocidade que foi passado
        time.sleep(0.5)
        print('Piloto: {} km: {} \n'.format(piloto, trajecto)) # correm jubtos depois de um tempo um python perdi, e o edson corre sozinho


#carro1(10) # chamamos a funcao carro com a velocidade de 10 k/h
#carro2(20) # chamamos a funcao carro com a velocidade d


t_carro1 = Thread(target=carro, args=[1, 'Edson']) #vai pertencer a classe tread, para qu funcione passamos terget que eh o alvo para que funcione, arqumentos dessa funcao sao a velocidade

t_carro2 = Thread(target=carro, args=[2, 'Phyton'])

t_carro1.start()
t_carro2.start()