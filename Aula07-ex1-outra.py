produto= {'nome':'Mouse', 'preco' : 49.90 , 'estoque': 25}

for chave,valor in produto.items():
    print(f'Chave: {chave} , Valor: {valor}')

consulta=input('Digite a chave que deseja consultar: ').lower()
print(produto.get(consulta,'Essa informação não está disponível'))
        
dados_novos={'categoria':'Informática','preco':59.90}
produto.update(dados_novos)
del produto['estoque']

print(f'\n--Dados atualizados--\n')

for chave,valor in produto.items():
    print(f'{chave} : {valor}')