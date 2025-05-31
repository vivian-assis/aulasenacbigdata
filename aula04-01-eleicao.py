print('BEM VINDO AO SISTEMA DE VOTAÇÃO\n\nPara iniciar o processo de votação é necessario que você se identifique\n')
v1 = 0
v2 = 0
v3 = 0
qv = 0
while True:
    try:
        nome = input('Digite seu nome:  ')
        if not nome.isalpha():
            raise ValueError('Digite um nome válido')
        else:
            break
    except ValueError as e:
        print(e)   

while True:
    try:
        idade = int(input('Digite a sua idade:   '))
        if idade>=14:
            break
        elif idade<14:
            print('Você não tem idade para votar ainda') 
    except ValueError:
        print('Dado inválido')
print('\nEsses são os candidatos à representante da turma\n 1. Goku \n 2. Naruto \n 3. Luffy \n')        
while True:
    try:
        voto= int(input('Digite o número do candidato que deseja votar:  '))
        
        match voto:
            case 1:
                v1 += 1
                qv +=1
            case 2:
                v2 += 1
                qv +=1
            case 3:
                v3 += 1
                qv +=1
            case _:
                print('Digite um candidato válido')

        maisvoto = input('Voto computado, deseja registrar outro voto (s/n)?\n').lower()
        if maisvoto == 'n':
            break
        elif maisvoto == 's':
            print('Então vote novamente')
        else:
            print('opção inválida')
        
                
    except ValueError:
        print('Dado inválido')

print(f'\n{nome}, você votou {qv} vezes\n')
print('O resultado da votação foi:')  


r1=(f'{v1} - Goku')
r2=(f'{v2} - Naruto')
r3=(f'{v3} - Luffy')
votos=[r1,r2,r3]
resultado=sorted(votos, reverse=True)
print(resultado)
eleito=(resultado)[0]

'''print(f'O candidato eleito foi: {eleito}')
'''
if v1>v2 and v1>v3:
    print(f'Goku foi eleito com {v1} votos!\n')
elif v2>v1 and v2>v3:
    print(f'Naruto foi eleito com {v2} votos!\n')
elif v3>v1 and v3>v2:
    print(f'Luffy foi eleito com {v3} votos!\n')
#elif v1==v2 or v1==v3 or v2==v3:
    #print(f'Houve um empate')
else:
    print('Houve um empate, novas eleições')

