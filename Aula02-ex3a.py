'''Você está desenvolvendo um sistema de pagamento para o mercadinho do seu Zé
Seu Zé sempre dá um desconto de:
2,70% aos clientes que pagam em dinheiro
'1,95% aos clientes que pagam em PIX
Acréscismo de 4,85% aos clientes que pagam em cartão
O sistema deve coletar o valor total da compra. Perguntar o tipo de pagamento, apalicar as regras do seu Zé e informar o valor final da compra'''

print('BEM VINDO AO MERCADINHO DO SEU ZÉ\nO MELHOR DO BAIRRO\n')


valor_total = float(input("Digite o valor total da compra: "))
metodo_pagamento = input("Digite o método de pagamento (dinheiro, pix, cartao): ").lower()

if metodo_pagamento == "dinheiro":
    valor_total  = valor_total - (valor_total*0.027)
    print(valor_total)
elif metodo_pagamento == "pix":
    valor_total = valor_total - (valor_total*0.0195)
    print(valor_total)
elif metodo_pagamento == "cartao":
    valor_total = valor_total + (valor_total*0.0485)
    print(valor_total)
else:
    print("Método de pagamento inválido.")

