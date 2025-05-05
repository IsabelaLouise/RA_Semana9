# 9. Fac ̧a um programa que preencha um vetor com 10 n  ́umeros reais, calcule e mostre a
# quantidade de n  ́umeros negativos e a soma dos n  ́umeros positivos desse vetor.
negativos = 0
somaPositivo = 0
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

if numero[0] < 0:
    negativos += 1
elif numero[0] > 0:
    somaPositivo += numero[0]

if numero[1] < 0:
    negativos += 1
elif numero[1] > 0:
    somaPositivo += numero[1]

if numero[2] < 0:
    negativos += 1
elif numero[2] > 0:
    somaPositivo += numero[2]

if numero[3] < 0:
    negativos += 1
elif numero[3] > 0:
    somaPositivo += numero[3]

if numero[4] < 0:
    negativos += 1
elif numero[4] > 0:
    somaPositivo += numero[4]

if numero[5] < 0:
    negativos += 1
elif numero[5] > 0:
    somaPositivo += numero[5]

if numero[6] < 0:
    negativos += 1
elif numero[6] > 0:
    somaPositivo += numero[6]

if numero[7] < 0:
    negativos += 1
elif numero[7] > 0:
    somaPositivo += numero[7]

if numero[8] < 0:
    negativos += 1
elif numero[8] > 0:
    somaPositivo += numero[8]

if numero[9] < 0:
    negativos += 1
elif numero[9] > 0:
    somaPositivo += numero[9]

print(f"Quantidade números negativos: {negativos} \nSoma dos números positivos: {somaPositivo}")