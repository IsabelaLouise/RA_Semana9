# 7. Escreva um programa que leia 10 n  ́umeros inteiros e os armazene em um vetor. Imprima
# o vetor, o maior elemento e a posic ̧ ̃ao que ele se encontra.
numero = [int(input("Digite um número: ")),
            int(input("Digite um número: ")), 
            int(input("Digite um número: ")), 
            int(input("Digite um número: ")), 
            int(input("Digite um número: ")), 
            int(input("Digite um número: ")), 
            int(input("Digite um número: ")), 
            int(input("Digite um número: ")),
            int(input("Digite um número: ")),
            int(input("Digite um número: "))]

maior = numero[0]
indice = 0

if numero[1] > maior:
    maior = numero[1]
    indice = 1
if numero[2] > maior:
    maior = numero[2]
    indice = 2
if numero[3] > maior:
    maior = numero[3]
    indice = 3
if numero[4] > maior:
    maior = numero[4]
    indice = 4
if numero[5] > maior:
    maior = numero[5]
    indice = 5
if numero[6] > maior:
    maior = numero[6]
    indice = 6
if numero[7] > maior:
    maior = numero[7]
    indice = 7
if numero[8] > maior:
    maior = numero[8]
    indice = 8
if numero[9] > maior:
    maior = numero[9]
    indice = 9
print(f"Maior elemento: {maior} \nPosição: {indice}")