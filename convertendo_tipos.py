# Converter Float para Int
print(int(1.5))

# Converter Int para Float
print(float(1))

# Converter String para Int
print(int("1"))

# Converter String para Float
try:
    print(float("1.5"))
except ValueError:
    print("Não é possível converter a string para float")

# Mas caso a string não seja um numero?
try:
    print(float("Barreira"))
except ValueError:
    print("Não é possível converter a string para float")

# Descobrindo o tipo da variavel
valor = 10
valor_str = str(valor)
print(type(valor))
print(type(valor_str))

# Como converter usando divisão
print(100 / 2)
print(100 // 2)