def calcularMedia(notas):
    soma = 0
    for nota in notas:
        print("Nota: {}".format(nota))
        soma += nota
        
    return soma/4

nome = input("Digite seu nome: ")

notas = []

contador = 0

while contador < 4:
    nota = float(input("Digite a nota {}: ".format(contador)))
    notas.append(nota)
    contador+=1

media = calcularMedia(notas)

if (media>=7):
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

print("A média do {} é: {}, e está {}".format(nome, media, resultado))