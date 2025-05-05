# 5. Leia um vetor de 10 posic ̧ ̃oes. Contar e escrever quantos valores pares ele possui.
pares = 0
numeros = [int(input("Digite um número: ")),
            int(input("Digite um número: ")), 
            int(input("Digite um número: ")), 
            int(input("Digite um número: ")), 
            int(input("Digite um número: ")), 
            int(input("Digite um número: ")), 
            int(input("Digite um número: ")), 
            int(input("Digite um número: ")),
            int(input("Digite um número: ")),
            int(input("Digite um número: "))]
if numeros[0] % 2 == 0:
    pares += 1
if numeros[1] % 2 == 0:
    pares += 1
if numeros[2] % 2 == 0:
    pares += 1
if numeros[3] % 2 == 0:
    pares += 1
if numeros[4] % 2 == 0:
    pares += 1
if numeros[5] % 2 == 0:
    pares += 1
if numeros[6] % 2 == 0:
    pares += 1
if numeros[7] % 2 == 0:
    pares += 1
if numeros[8] % 2 == 0:
    pares += 1
if numeros[9] % 2 == 0:
    pares += 1
print(f"Possui {pares} valor(es) par(es)")