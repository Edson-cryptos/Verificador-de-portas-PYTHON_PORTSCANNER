import nmap

verificador = nmap.PortScanner()

print('<->' * 40)

host = input("Digite um host valido: ")
print("O host digitado eh: ", host)

print("1 <-> Verificar as portas Udp")
print("2 <-> Verificar as portas Syn")
print("3 <-> Verificar as portas C")
print("")
opcoes = int(input("Escolha uma opcao: "))

if opcoes == 1:
    print("A versao do nmap", verificador.nmap_version())
    verificador.scan("host", '1-1924', '-v -sU')
    print("status di host:", verificador[host].state())
    print(verificador[host].all_protocols())
    print("Portas abertas:", verificador[host]['tcp'].keys())
elif opcoes == 1:
    print("A versao do nmap", verificador.nmap_version())
    verificador.scan("host", '1-1924', '-v -sU')
    print("status di host:", verificador[host].state())
    print(verificador[host].all_protocols())
    print("Portas abertas:", verificador[host]['tcp'].keys())
elif opcoes == 3:
    print("A versao do nmap", verificador.nmap_version())
    verificador.scan("host", '1-1924', '-v -sU')
    print("status di host:", verificador[host].state())
    print(verificador[host].all_protocols())
    print("Portas abertas:", verificador[host]['tcp'].keys())
else:

    while (opcoes >= 4):
        opcoes = int(input("Escolha uma opcao Valida no intervalo de 1 - 3: "))
        print("1 <-> Verificar as portas Udp")
        print("2 <-> Verificar as portas Syn")
        print("3 <-> Verificar as portas C")
        print("")
        print("A opcao esclolhida foi:", opcoes , "Por favor reinicie o programa e volte a introduzir a opcao..!")

