# Criação da tupla com 5 dados
tupla = (1, 2, 3, 4, 5)

# Alteração da tupla para uma lista
lista = list(tupla)

# Inserção de 2 dados extras na lista
lista.append(6)
lista.append(7)

# Remoção do primeiro dado da lista
lista.pop(0)

# Remoção do último dado da lista
lista.pop()

# Print do primeiro dado da lista
print("Primeiro dado da lista:", lista[0])

# Print da quantidade de dados da lista
print("Quantidade de dados na lista:", len(lista))

# Criação de um dicionário com Nome, Idade, Profissão
dicionario = {
    "Nome": "João",
    "Idade": 30,
    "Profissão": "Engenheiro"
}

# Impressão do valor contido na chave Nome do dicionário
print("Nome no dicionário:", dicionario["Nome"])