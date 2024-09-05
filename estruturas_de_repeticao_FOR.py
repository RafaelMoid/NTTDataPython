# Hoje vamos falar de estruturas de repetição

# For
texto = input("Informe um Commander: ")
VOGAIS = "AEIOU"
vogais_do_commander = ""

for letra in texto:
    if letra.upper() in VOGAIS:
        vogais_do_commander =  vogais_do_commander + letra
    else:
        print()
        print("Não tem letras no nome do Commander")
        break
        
print() #Adiciona quebra de linha

print(f"As vogais do seu Commander são: {vogais_do_commander}")

Range + For
for numero in range(1,11):
    print(numero, end="")
    
#Exibindo a tabuada de 5 com For e Range
for numero in range (0, 11):
    print(f"{numero} x 5 = {numero * 5}")
    
print() #Adiciona quebra de linha
    
    # Outra forma de fazer
for numero2 in range (0, 51, 5): #O terceiro parametro/argumento determina de quanto em quanto o range vai retornar itens
    print(numero2, end=" ")
