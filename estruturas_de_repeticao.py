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

