nome = input("Digite seu nome: ")

notas = []

contador = 0

while contador < 4:
    valor= input("Digite a nota {}:".format(contador))
    nota = float(valor)
    notas.append(nota)
    contador+=1