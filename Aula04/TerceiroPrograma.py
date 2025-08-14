# estudo de for e while loops

# for i in range(1, 11):
#     print(i)
# print("Fim do Loop")
# for y in range(10, 1, -1):
#     print(y)
# print("Fim do Loop")
# for i in range(1, 10, 1):
#     print(i)
# print("Fim do Loop")
# for x in range(10):
#     x+= 1
#     print(x)
# print("Fim do Loop")
# for x in range(10):
#     print(x + 1)

# for conta in range(100):
#     conta += 1
#     print(conta)
#     if conta == 50:
#         print("Chegou na metade!")
#     elif conta == 75:
#         print("Chegou nos 3/4 do caminho!")
#     elif conta == 100:
#         print("Chegou ao final!")

número = int(input("Digite um número: "))

if número % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")

número1 = int(input("Digite o primeiro número: "))
número2 = int(input("Digite o segundo número: "))
if número1 > número2:
    print(f"{número1} é maior que {número2}.")
elif número1 < número2:
    print(f"{número2} é maior que {número1}.")
else:
    print("Os números são iguais.")

idade = int(input("Digite sua idade: "))
if idade < 12:
    print("Você é uma criança.")
elif idade < 17:
    print("Você é um adolescente.")
elif idade < 64:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")

