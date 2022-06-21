#dpcumentação

#isnumeric
#isdigit
#isdecimal

num1 = input('Digite um numero:')
num2 =  input('Digite ouro número')
# print(num1.isnumeric())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Não consgeui converter')