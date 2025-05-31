'''Você está desenvolvendo um sistema de controle de despesa'''
'''O sistema deve solicitar que o usuário informe o limeite do cartão de crédito e valor da compra que deseja realizar'''
'''Após isso, o sistema deve retornar uma mensagem dizendo se a compra poderá ser realizada ou não'''

print('\nBem vindo ao sistema de controle de despesas!\n')
nome = input('\nDigite seu nome: \n').title()
limite = float(input('\nDigite o valor do limite do seu cartão: \n'))
compra = float(input('\nDigite o valor da compra desejada: \n'))

if compra<limite:
    print(f'Parabéns {nome}, você pode realizar a compra desejada!\nAinda restará {limite-compra} de limite no seu cartão ;)\n')
elif compra==limite:
    print(f'{nome}, você pode realizar a compra, mas ficará sem nenhum limite\n')
else:
    print(f'{nome}, infelizmente você não tem limite suficiente :(\nFalta {compra-limite} de limite para que você possa realizar a compra\n')
