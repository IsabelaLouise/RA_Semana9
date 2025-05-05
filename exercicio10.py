# 10. Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos
# juntamente com o maior, o menor e a m  ́edia dos valores.
numero = [int(input("Digite um número: ")),
            int(input("Digite um número: ")), 
            int(input("Digite um número: ")), 
            int(input("Digite um número: ")), 
            int(input("Digite um número: "))]

maior = numero[0]
menor = numero[0]
media = (numero[0] + numero[1] + numero[2] + numero[3] + numero[4]) / 5

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

print(f"Valores: {numero} \nMenor: {menor} \nMaior: {maior} \nMédia: {media}")