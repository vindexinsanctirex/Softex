# print(type('22'))
# print(type(22))
# print(type(22.0))
# print(type(True))
# print(type(None))
# print(str(22))
# print(float(22))
# print(int(22.0))
# print(bool(-2))
# print(bool(None))

# def bmi(weight, height):
#     index = weight / (height * height)
#     return index

# p6 = bmi(79, 1.73)
# p7 = bmi(102, 1.89)
# print(p6 < 18.5)
# print(p6 >= 18.5 and p6 < 25)
# print(p6)
# print(p7 < 18.5)
# print(p7 >= 18.5 and p7 < 25)
# print(p7)


# nome = "Caio"
# idade = 37
# curso = "Python pela Softex"

# print("Olá meu nome é " + nome + ", tenho " + str(idade) + " anos e estou aprendendo " + curso + " por um período de 6 meses.")
# print("Olá meu nome é ", nome, ", tenho ", idade, " anos e estou aprendendo ", curso, " por um período de ", 2 + 4, " meses.", sep='')
# print(f'Olá meu nome é {nome}, tenho {idade} anos e estou aprendendo {curso} por um período de {2 + 4} meses.')


resposta = input("Sim, Não ou Talvez: ")

if resposta == "Sim" or resposta == "sim":
    print("Resposta Certa!")

elif resposta == "Não" or resposta == "não":
    print("Resposta Errada!")

elif resposta == 'Talvez' or resposta == 'talvez':
    print("Responda Novamente!")

else:
    print("Resposta Inválida!")
