# Usando WHILE
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar\n[2] Exibir extrato\n[3] Sair\n"))
    
    if opcao == 1:
        print("Sacando")
    elif opcao == 3:
        print("Saindo")
        break
    else:
        print("Exibindo extrado")