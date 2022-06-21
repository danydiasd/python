nome = 'Dani'
print(nome)
idade = 30
altura= 1.70
peso = 84
maioridade = idade>18
print("Nome: ", nome)
print("altura: ", altura)
print("idade", idade)
imc = peso / altura ** 2
print(nome, 'tem', idade, 'de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos e seu imc é {}'.format(nome, idade, imc))
print('{n} tem {i} anos e seu imc é {im}'.format(n=nome, i=idade, im=imc))

