"""
Escopo de Variáveis

Dois casos de escopo:

1 Variáveis globais:

- Variaveis globais são reconhecidas, ou seja, seu escopopo compreende todo o programa.

2 Variáveis locais:

- Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo esta limitado ao bloco onde foi declarada

Para declarar variáveis em Python fazemos:

nome da variavel = valor da variavel

Python é uma linguagem de tipagem dinamica. Isso significa que ao declararmos
uma variavel, nos não colocamos o tipo de dado dela

Este tipo é inferido ao atribuirmos o valor a mesma.

Exemplo em C: int numero = 42;

"""

numero = 42 # Exemplo de variavel global
print(numero)
print(type(numero))


#novo = 0

if numero > 10:
    novo = numero + 10 # A variavel 'novo' está declarada localmente dentro do bloco if, portanto é local.
    print(novo)

print(novo)