# 6. Faça um programa que receba do usu ́ario um vetor com 10 posic ̧  ̃oes. 
# Em seguida dever ́a ser impresso o maior e o menor elemento do vetor.
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
menor = numero[0]

if numero[1] > maior:
    maior = numero[1]
if numero[1] < menor:
    menor = numero[1]

if numero[2] > maior:
    maior = numero[2]
if numero[2] < menor:
    menor = numero[2]

if numero[3] > maior:
    maior = numero[3]
if numero[3] < menor:
    menor = numero[3]

if numero[4] > maior:
    maior = numero[4]
if numero[4] < menor:
    menor = numero[4]

if numero[5] > maior:
    maior = numero[5]
if numero[5] < menor:
    menor = numero[5]

if numero[6] > maior:
    maior = numero[6]
if numero[6] < menor:
    menor = numero[6]

if numero[7] > maior:
    maior = numero[7]
if numero[7] < menor:
    menor = numero[7]

if numero[8] > maior:
    maior = numero[8]
if numero[8] < menor:
    menor = numero[8]

if numero[9] > maior:
    maior = numero[9]
if numero[9] < menor:
    menor = numero[9]

print(f"Menor: {menor} \nMaior: {maior}")