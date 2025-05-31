while True:
    try:
        n1 = float(input('Digite o primeiro número:  '))
        break
    except ValueError:
        print('Dado inválido')

while True:
    try:        
        operacao = input('\nDigite a operação desejada (+, -, *, /):\n')
        if operacao in ['+', '-', '*', '/']:
            break
        else:
            print('Opção inválida, digite +, -, * ou /')         
    except ValueError:
        print('Opção inválida')

while True:
    try:
        n2 = float(input('\nDigite o segundo número:  '))
        if operacao == '/' and n2==0:
            raise ValueError('Não é possível dividir por zero.')
        break
    except ValueError as e:
        print(f'Erro: {e}')

if operacao == '+':
    resultado = n1+n2
    print(f'O resultado da soma é {resultado}')

elif operacao == '-':
    resultado = n1-n2
    print(f'O resultado da subtração é {resultado}')

elif operacao == '+':
    resultado = n1*n2
    print(f'O resultado da multiplicação é {resultado}')

elif operacao == '/':
    resultado = n1/n2
    print(f'O resultado da divisão é {resultado}\n')
