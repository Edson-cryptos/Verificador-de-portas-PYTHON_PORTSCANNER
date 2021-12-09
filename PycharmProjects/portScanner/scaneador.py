import nmap



scaneador = nmap.PortScanner #jogamos todos os atribitos do portscanner da bibliooteca nmap na variavel scanner[ prorpriedade scanner do nmap e jogamos na varievel scanner

#print("Seja bem vindo ao DIOScanner")
print("#" * 30)

ip = input("DIgite o ip a ser varrodo:")
print("O ip digitado foi:", ip)
type(ip)

menu = input("""\n escolha o tipo de varedura a ser realizada
                1 -> Varredura do tipo SYN
                2 -> Varredura do tipo UDP
                3 -> Varreura do tipo Intensa
                Digite a opcao escolhida: """)
print("A opcao escolhida foi:", menu)

if menu == "1":
    print("Versao do Nmap: ", scaneador.nmap_version())
    scaneador.scan(ip, '1-1024', '-v -sS') #ip eh o ip a ser varido, 1-1024 sao as portas que ele vai varer,-v verbose para mostrar na tela sobre como esta sendo feita a veredura, s de scan e S de sync)
    print(scaneador.scaninfo()) # Para mostrar as informacoes do scan
    print("Starus do IP: ", scaneador[ip].state()) # para printar o status do ip
    print(scaneador[ip].all_protocols()) # Para imprimir todos os protoculos que passam dentro do ip
    print("")
    print("Portas Abertas: ", scaneador[ip]['tcp'].keys()) # PAra imprimir as portas abertas, do lado do [ip] vem a requisicao que ele precisa fazer que eh requisacao do tipo tcp e pegue as keys da mesmas

elif menu == "2":
    print("versao do Nmap: ", scaneador.nmap_version())
    scaneador.scan(ip, '1-1024', '-v -sU')
    print(scaneador.scaninfo())
    print("status do IP: ", scaneador[ip].state())
    print(scaneador[ip].all_protcols())
    print("")
    print("Portas Abertas: ", scaneador[ip]['udp'].keys())
elif menu == "3":
    print("versao do Nmap: ", scaneador.nmap_version())
 #  scanner.scam(ip, '1-1024', '-v -sU