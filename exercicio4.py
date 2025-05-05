# 4. Faça um programa que leia um vetor de 8 posições e, em seguida, 
# leia tamb ́em dois valores X e Y quaisquer correspondentes a duas posic ̧ ̃oes no vetor. 
# Ao final seu programa devera ́ escrever a soma dos valores encontrados nas respectivas posic ̧ ̃oes X e Y .
numeros = [int(input("Digite um número: ")),
            int(input("Digite um número: ")), 
            int(input("Digite um número: ")), 
            int(input("Digite um número: ")), 
            int(input("Digite um número: ")), 
            int(input("Digite um número: ")), 
            int(input("Digite um número: ")), 
            int(input("Digite um número: "))]

x = int(input("Digite a posição x (0 a 7): "))
y = int(input("Digite a posição y (0 a 7): "))

soma = numeros[x] + numeros[y]

print(f"A soma entre {numeros[x]} e {numeros[y]} é de {soma}")