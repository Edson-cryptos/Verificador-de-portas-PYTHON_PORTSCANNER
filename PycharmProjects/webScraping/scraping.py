from bs4 import BeautifulSoup  # Precisa ser instalado para
import requests #importanto a biblioteca requests

#objecto site recebendo o conteudo da requisicao http do site.....
site = requests.get("https://www.climatempo.com.br/").content # .content eh para pegar todo conteudo do site

# Objecto souo esta baixando do site o html desse site
soup = BeautifulSoup(site, 'html.parser')
print(soup.prettify())

temperatura = soup.find("li", class_="item")
print(temperatura.string)
print(soup.title.string )
#Transforma html em string e o print vai exibir o html
