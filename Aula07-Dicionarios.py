aluno = {"nome":"Ana", "idade":16,"nota":9.0}

print(aluno.keys())
print(aluno.values())
print(aluno.items())


#adicionar ou alterar valores
aluno['nota'] = 9.5
aluno['turma'] = '3A'

# remover itens
del aluno['idade']

# verificar chave existente
if 'nome' in aluno:
    print(len(aluno))

# tamanho do dicionario
print(len(aluno))

# obter apenas chaves, valores ou ambos
print(aluno.keys())
print(aluno.values())
print(aluno.items())

# iterar
for chave, valor in aluno.items():
    print(f'{chave}: {valor}')

#Copiar um dicionário
copia = aluno.copy()


