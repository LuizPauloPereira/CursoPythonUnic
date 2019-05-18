nome = input("Digite seu nome: ")
print("Olá {}".format(nome))

valor = float(input("Digite sua media: "))

if valor >= 7:
    resultado = "aprovado"
else:
    resultado = "reprovado"

print("{} está {} com média {}".format(nome, resultado, valor))