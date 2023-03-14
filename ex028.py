#Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos


num = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

somaQuadrados = (num*num) + (num2*num2) + (num3*num3)
print(f'A soma dos quadradosé {somaQuadrados}')
