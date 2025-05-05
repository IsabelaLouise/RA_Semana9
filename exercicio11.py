# 11. Fazer um programa para ler 5 valores e, em seguida, mostrar a posic ̧ ̃ao onde se encon-
# tram o maior e o menor valor.
numero = [int(input("Digite um número: ")),
            int(input("Digite um número: ")), 
            int(input("Digite um número: ")), 
            int(input("Digite um número: ")), 
            int(input("Digite um número: "))]

maior = numero[0]
menor = numero[0]
indiceMaior = 0
indiceMenor = 0

if numero[1] > maior:
    maior = numero[1]
    indiceMaior = 1
if numero[1] < menor:
    menor = numero[1]
    indiceMenor = 1

if numero[2] > maior:
    maior = numero[2]
    indiceMaior = 2
if numero[2] < menor:
    menor = numero[2]
    indiceMenor = 2

if numero[3] > maior:
    maior = numero[3]
    indiceMaior = 3
if numero[3] < menor:
    menor = numero[3]
    indiceMenor = 3

if numero[4] > maior:
    maior = numero[4]
    indiceMaior = 4
if numero[4] < menor:
    menor = numero[4]
    indiceMenor = 4

print(f"Menor: {menor} \nPosição do menor: {indiceMenor} \nMaior: {maior} \nPosição do maior: {indiceMaior}")