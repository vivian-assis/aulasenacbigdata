'''lista = ['joao', 16, 'japeri']

print(f'o aluno mora no bairro {lista[2]}')

lista.append('RJ')
print(f'o aluno mora no bairro {lista[2]} e na cidade {lista[3]}')

lista.insert(1, 'Masculino')
print(lista[1:4])

#opções de remoção
del lista[2]
lista.pop(2)
lista = ['joao', 'mateus', 'sofia', 'maria', 'sofia']

lista.remove('sofia')

num1 = 10 
y = 10,5
nome = 'gabe'
print(type(num1))
print(type(y))
print(type(nome))'''

'''
COPIE E COLE NO SEU NAVEGADOR 

https://teams.microsoft.com/l/meetup-join/19%3ameeting_MmY5MDFhOTYtNzNhMy00MjliLWE2NjYtMDMzMzExZTFkYjlj%40thread.v2/0?context=%7b%22Tid%22%3a%22c978a5cf-afa2-42a9-a3cf-a0d9518374a7%22%2c%22Oid%22%3a%221221c8fd-0367-432d-8e38-ad4bb36406e9%22%7d


DRIVE :
https://drive.google.com/drive/folders/1I6SiB6-WjDYg2hmCktlNC70SmWyXM045?usp=sharing 



BADGES:

https://github.com/iuricode/readme-template/tree/main/badges-shields'''

contador = 0
lista = []
while True:
    if contador <= 4:
        try :
            nome = input('Digite um nome\n').title()
            
            if not nome.replace(' ','').isalpha():
                raise ValueError('Digite um nome válido sem números')
            else:
                lista.append(nome)
                contador += 1
                            
        except ValueError as e:
            print('Digite um nome válido ')
    
    else:
        break

print(f'Nomes cadastrados:\n{lista}')

while True
    try
    remove=input('Escolha o nome que deseja remover da lista:\n')
    



