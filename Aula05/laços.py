print("=" * 50)
print("ATIVIDADE 1 - Par ou Ímpar")
print("=" * 50)
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é ímpar")

print("\n" + "=" * 50)
print("ATIVIDADE 2 - Classificação de Nota")
print("=" * 50)
nota = float(input("Digite a nota do aluno (0-10): "))
if nota >= 7:
    print("Aprovado")
elif 5 <= nota < 7:
    print("Recuperação")
else:
    print("Reprovado")

print("\n" + "=" * 50)
print("ATIVIDADE 3 - Comparação de Números")
print("=" * 50)
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
if numero1 > numero2:
    print(f"O primeiro número ({numero1}) é maior")
elif numero2 > numero1:
    print(f"O segundo número ({numero2}) é maior")
else:
    print("Os números são iguais")

print("\n" + "=" * 50)
print("ATIVIDADE 4 - Classificação por Idade")
print("=" * 50)
idade = int(input("Digite sua idade: "))
if idade <= 12:
    print("Criança")
elif 13 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 64:
    print("Adulto")
else:
    print("Idoso")

print("\n" + "=" * 50)
print("ATIVIDADE 5 - Números de 1 a 10")
print("=" * 50)
print("Números de 1 a 10:")
for i in range(1, 11):
    print(i)

print("\n" + "=" * 50)
print("ATIVIDADE 6 - Tabuada")
print("=" * 50)
numero_tabuada = int(input("Digite um número para ver sua tabuada: "))
print(f"Tabuada do {numero_tabuada}:")
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")

print("\n" + "=" * 50)
print("ATIVIDADE 7 - Somar Números")
print("=" * 50)
soma = 0
print("Digite números para somar (0 para encerrar):")
while True:
    numero = float(input("Digite um número: "))
    
    if numero == 0:
        break
    
    soma += numero

print(f"A soma dos números digitados é: {soma}")