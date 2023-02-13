#leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus celsius

temp_f= float(input('Qual a temperatura em Fahrenheit: '))
temp_c= (5*(temp_f-32)/9)
print(f'A temperatura em Celsius é de : {temp_c}')