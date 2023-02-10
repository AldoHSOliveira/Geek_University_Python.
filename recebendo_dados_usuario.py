"""
Recebendo dados do usuario

input() -> Todo dado recebido via input é do tipo String

Em Python String é tudo que estiver entre:

- Aspas simples: 'Aldo'
- Aspas Duplas: "Aldo"
- Aspas Simples triplas:'''Aldo'''

"""
# - Aspas duplas Triplas: """Aldo"""



# Entrada de dados

#print("Qual é seu nome ? ")
#nome = input() #input = entrada


nome = input('Qual é seu nome? ')

# Processamento


# Saida de dados

#Exemplo de print Antigo

#print('Seja bem vindo[a] %s' % nome)

#Exemplo de print Moderno
#print('Seja bem vinda(a) {0}'.format(nome))

#Exemplo de print atual
print(f'Seja bem vindo {nome}')

# Entrada de dados

#print('Qual sua idade? ')
#idade = input()

#int para converter para inteiro
idade = int(input('Qual é sua idade ? '))


# Processamento

#Saida de dados

#Exemplo de print Antigo
#print('Você %s tem %s anos' % (nome, idade))

#Exemplo de print Moderno
#print('Você {0} tem {1} anos '.format(nome,idade))

#Exemplo de print atual
print(f'Você {nome} tem {idade} anos')

"""
# int(idade) >> cast

Cast é a 'conversação' de um tipo de dado para outro

"""