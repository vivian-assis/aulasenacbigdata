'''Estruturas de Decisão'''
idade = int(input('Qual a sua idade: '))
ingresso = input('Você comprou o seu ingresso? S/N ').upper()
nome = input('Qual o seu nome? ').title()

if idade >= 18 and ingresso == 'S':
    print(f'{nome}, seu acesso está liberado! Beba com moderação')
elif idade >= 18 and ingresso != 'S':
    print(f'{nome}, vá até a bilheteria e compre um ingresso' )
else: 
    print('Acesso negado')

