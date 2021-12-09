import re
import json
from urllib.request import urlopen

url = 'https://dio.me'

resposta = urlopen(url)

dados = json.load(resposta) #o json carrega todo o java scrip e joga para o dados

ip = dados['ip'] # ip guarda dados da seccao ip
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']

print('Detalhes do Ip externo\n')
print('Ip : {4}\nRegiao: {1}\nPasis: {2}\nCidade: {3}\nOrg.: {0}'.format(org,regiao,pais,cid,ip))