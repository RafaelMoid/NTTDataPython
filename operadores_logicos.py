# AND = para ser True tudo deve ser True. 
# OR = para ser True um deve ser True.

print("Testes com AND e OR")
print(f"Usando AND com True e True: {True and True}")
print(f"Usando AND com True e False: {True and False}")
print(f"Usando AND com False e False: {False and False}")
print(f"Usando OR com True e True: {True or True}")
print(f"Usando OR com True e False: {True or False}")
print(f"Usando OR com False e False: {False or False}")

saldo = 1000
saque = 200
limite = 100

# Operador E ou And - checa todas as condições
# print(saldo >= saque and saque <= limite)

# Operador Ou ou Or - checa todas as condições
# print(saldo >= saque or saque <= limite)

# Operador Não ou Not - checa todas as condições
# print(not saldo >= saque)

# nos casos abaixos usando o Not para checar se existe conteudo dentro das variaveis e strings
contatos_emergencia = []
# print(not contatos_emergencia)

# print(not "sheoldred")

# print(not "")

# Parenteses
saldo = 1000
saque = 250
limite = 200
conta_especial = True

# exp = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
# print(exp)