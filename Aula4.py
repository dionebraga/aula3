# Programa para calcular a média aritmética de 4 notas

# Solicita o nome do usuário
nome = input("Digite seu nome ")

# Solicita as quatro notas, uma por vez
nota1 = float(input("Por favor, insira a primeira nota: "))
nota2 = float(input("Por favor, insira a segunda nota: "))
nota3 = float(input("Por favor, insira a terceira nota: "))
nota4 = float(input("Por favor, insira a quarta nota: "))

# Calcula a média aritmética das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

# Exibe a média com uma mensagem personalizada
print(f"Olá, {nome}! Sua média é: {media:.2f} pontos")

