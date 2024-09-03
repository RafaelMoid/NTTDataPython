# ESTRUTURAS COM IF, ELSE E ELIF

MAIOR_IDADE = 18
CASADO = False
# CASADO = True

idade = int(input("informe sua idade: "))

# Usando IF com redundancia
if idade >= MAIOR_IDADE:
    print("ta liberado para tomar uma cervejinha")
    
if idade < MAIOR_IDADE:
    print("ta liberado para tomar um água")


# Usando IF e ELSE
if idade >= MAIOR_IDADE:
    print("e pegar o deck de 2k")
    
else:
    print("e jogar com deck budget")


# Usando IF e ELSE
if idade >= MAIOR_IDADE and CASADO == False:
    print("gaste quanto quiser com papelão, é seu lazer")
elif idade >= MAIOR_IDADE and CASADO == True:
    print("porém cuidado para não gastar muito e não dar rolê com a esposa")    
else:
    print("aproveite para procurar emprego e conseguir comprar papelão")
    
# ESTRUTURAS COM IF, ELSE E ELIF