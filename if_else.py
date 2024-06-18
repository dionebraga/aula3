# Solicita a idade do usuário
idade = int(input("Digite a sua idade: "))

# Verifica a idade do usuário e imprime as mensagens correspondentes
if idade > 18:
    print("Indivíduo possui idade mínima para dirigir")
elif idade == 17 or idade == 18:
    print("Indivíduo tem entre 17 e 18 anos e ainda NÃO está apto para dirigir")
else:
    print("Indivíduo NÃO possui idade mínima para dirigir")