'''Você está desenvolvendo um sistema de pagamento para o mercadinho do seu Zé'''
'''Seu Zé sempre dá um desconto de:'''
'''2,70% aos clientes que pagam em dinheiro'''
''''1,95% aos clientes que pagam em PIX'''
'''Acréscismo de 4,85% aos clientes que pagam em cartão'''
'''O sistema deve coletar o valor total da compra. Perguntar o tipo de pagamento, apalicar as regras do seu Zé e informar o valor final da compra'''

print('Bem vindo Seu Zé!')

compra = float(input('Digite o valor da compra: '))
pag = int(input('Qual a forma de pagamento?\n1 - Dinheiro\n2 - PIX\n3 - Cartão\nDigite uma opção: '))

match pag:
    case 1:
        print(f'Valor a pagar  {compra-(compra*0.027)}\n')
    case 2:
        print(f'Valor a pagar  {compra-(compra*0.0195)}\n')
    case 3:
        print(f'Valor a pagar  {compra+(compra*0.0485)}\n')
    case _:
        print('Opção inválida!\n')
