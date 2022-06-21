nome = 'Dani'
idade = 30
altura= 1.70
peso = 84
nasc = 1991
imc = peso / altura ** 2
print(nome, 'tem', idade, 'de idade e seu imc é', imc)


print('{n} tem {i} anos, {a} de altura e pesa {p}kg. O IMC de {n} é {im}e seu imc é {im}.{n} nasceu em {nasc}'.format(n=nome, i=idade, a=altura, im=imc, p=peso, nasc=nasc))
print(f'{nome} tem {idade} anos  e {altura} de altura.')
print(f'{nome} pesa {peso}kg e seu imc é {imc:.2f}.')
print(f'{nome} nasceu em  {nasc}.')