# Calculadora
numA = input ('Digite o primeiro número: ')
numB = input ('Digite o segundo número: ')

soma = float(numA) + float(numB)
subtracao = float (numA) - float(numB)
divisao = float(numA) / float(numB)
multiplicacao = float(numA) * float(numB)

menu = print ('\nEscolha 1 para somar\n\nEscolha 2 para subtrair\n\nEscolha 3 para dividir\n\nEscolha 4 para multiplicar\n')

operacao = input ('Escolha a sua operação: ')

if operacao == ('1'):
  print (soma)

if operacao == ('2'):
  print (subtracao)

if operacao == ('3'):
  print (divisao)
  
if operacao == ('4'):
  print (multiplicacao)
