'''Match Case'''
print('\nBEM VINDO AO SENAC\n')

curso = int(input('Qual curso você deseja fazer conosco:\n1- Análise de Dados\n2- Power BI\n3- Desenvolvimento de Banco de Dados\n4- Outro\nDigite sua opção '))

match curso:
    case 1:
        print('Parabéns por escolher Análise de Dados\n')
    case 2:
        print('Parabéns por escolher Power BI\n')
    case 3:
        print('Parabéns por escolher Desenvolvimento de Banco de Dados\n')
    case 4:
        print('Acesse nosso site e veja outras opções\n')
    case _:
        print('Opção inválida\n')
    