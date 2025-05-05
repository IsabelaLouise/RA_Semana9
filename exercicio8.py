# 8. Fac ̧a um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule
# e imprima a m  ́edia geral.
notas = [float(input("Digite a primeira nota: ")),
         float(input("Digite a segunda nota: ")),
         float(input("Digite a terceira nota: ")),
         float(input("Digite a quarta nota: ")),
         float(input("Digite a quinta nota: ")),
         float(input("Digite a sexta nota: ")),
         float(input("Digite a sétima nota: ")),
         float(input("Digite a oitava nota: ")),
         float(input("Digite a nona nota: ")),
         float(input("Digite a décima nota: ")),
         float(input("Digite a décima primeira nota: ")),
         float(input("Digite a décima segunda nota: ")),
         float(input("Digite a décima terceira nota: ")),
         float(input("Digite a décima quarta nota: ")),
         float(input("Digite a décima quinta nota: ")),]

media = (notas[0] + notas[1] + notas[2] + notas[3] + notas[4] + notas[5] + notas[6] + notas[7] + notas[8] + notas[9] + notas[10] + notas[11] + notas[12] + notas[13] + notas[14]) / 15 
print(f"A média de todas as notas foi de {media}")