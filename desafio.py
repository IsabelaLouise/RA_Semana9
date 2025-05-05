#Desafio
# Implemente um programa em Python para verificar quantos números
# uma aposta acertou na Mega Sena. O programa deve ler do teclado
# os 6 números apostados e comparar com os 6 números sorteados.
# Ao final, o programa deve exibir os números sorteados, números
# jogados e quantidade de acertos
from random import sample
acertos = 0
numerosMega = [range(1,60), 6]
numeroDigitado = [int(input("Digite o número para aposta: ")), int(input("Digite o número para aposta: ")), int(input("Digite o número para aposta: ")), int(input("Digite o número para aposta: ")), int(input("Digite o número para aposta: ")), int(input("Digite o número para aposta: "))]

if numerosMega[0] == numeroDigitado[0] or numerosMega[0] == numeroDigitado[1] or numerosMega[0] == numeroDigitado[2] or numerosMega[0] == numeroDigitado[3] or numerosMega[0] == numeroDigitado[4] or numerosMega[0] == numeroDigitado[5]:
    acertos += 1
if numerosMega[1] == numeroDigitado[0] or numerosMega[1] == numeroDigitado[1] or numerosMega[1] == numeroDigitado[2] or numerosMega[1] == numeroDigitado[3] or numerosMega[1] == numeroDigitado[4] or numerosMega[1] == numeroDigitado[5]:
    acertos += 1
if numerosMega[2] == numeroDigitado[0] or numerosMega[2] == numeroDigitado[1] or numerosMega[2] == numeroDigitado[2] or numerosMega[2] == numeroDigitado[3] or numerosMega[2] == numeroDigitado[4] or numerosMega[2] == numeroDigitado[5]:
    acertos += 1
if numerosMega[3] == numeroDigitado[0] or numerosMega[3] == numeroDigitado[1] or numerosMega[3] == numeroDigitado[2] or numerosMega[3] == numeroDigitado[3] or numerosMega[3] == numeroDigitado[4] or numerosMega[3] == numeroDigitado[5]:
    acertos += 1
if numerosMega[4] == numeroDigitado[0] or numerosMega[4] == numeroDigitado[1] or numerosMega[4] == numeroDigitado[2] or numerosMega[4] == numeroDigitado[3] or numerosMega[4] == numeroDigitado[4] or numerosMega[4] == numeroDigitado[5]:
    acertos += 1
if numerosMega[5] == numeroDigitado[0] or numerosMega[5] == numeroDigitado[1] or numerosMega[5] == numeroDigitado[2] or numerosMega[5] == numeroDigitado[3] or numerosMega[5] == numeroDigitado[4] or numerosMega[5] == numeroDigitado[5]:
    acertos += 1

print(f"Números sorteados: {numerosMega} \nNúmeros jogados: {numeroDigitado} \nAcertos: {acertos}")