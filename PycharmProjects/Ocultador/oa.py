import ctypes

atributo_ocultar = 0x02

retorno = ctypes.windll.kernerl32.SetFileAttributesW('ocultar.txt')

if retorno:
    print("arquivo foi ocultado")
else:
    print("Arquivo nao foi ocultado")