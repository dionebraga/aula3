# Solicita o valor da compra ao cliente
valor_compra = float(input(" Olá, Bem vindos a FashionStyle! Digite o valor total da sua compra: R$ "))

# Verifica os critérios de desconto e imprime as mensagens correspondentes
if valor_compra > 500:
    print("PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%")
elif valor_compra >= 250:
    print("PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00")
else:
    print("POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.")