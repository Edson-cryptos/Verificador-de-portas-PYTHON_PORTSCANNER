import webbrowser
from tkinter import *
from tkinter import Tk, Button

root = Tk( ) # root vai reprenstar o tkinter, quando colocamos espaco signifia'none' que nao tem nome da tela,

root.title('Abrir Browser') # O titulo do a interface grafica
root.geometry('300x200') # o tamanho do sistema que vai abrir o programa

def google():  # a funcao Para que possa abrir o google
    webbrowser.open('www.google.com')

mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20) #Objecto mygoogle, que recebe o botao do tkinte, e esse botao pertence ao root, e o seu text eh' ', e o command eh abrir o navegador google o parametro pack passa a posiicao do botao que eh 20
root.mainloop()

