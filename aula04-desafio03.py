
# Desafio 3
# Crie um script Python que leia dois números
# e tente mostrar a soma entre eles.

numero1 = int(input("Primeiro número: "))
numero2 = int(input("Segundo número: "))
soma = numero1 + numero2

# Modo 1 - Utilizando F-strings (Python 3.6+)
# Neste exemplo, o f antes das aspas indica que é uma f-string, 
# que permite inserir expressões Python dentro da string, incluindo variáveis entre chaves {}.
print(f"A soma de {numero1} + {numero2} é {numero1+numero2}.")

# Modo 2 - Utilizando o método `.format()`
# Neste caso, `{}` dentro da string é substituído pelo valor de `nome` passado como
# argumento para o método `format()`.
print('A soma de {} + {} é {}.'.format(numero1,numero2,soma))

# Modo 3 - Concatenando strings manualmente
# Neste método, você concatena strings usando o operador +. No entanto, em Python,
# a formatação de string com f-strings ou .format() é geralmente considerada mais legível e pythonica.
print('A soma de ' +str(numero1)+ ' + ' +str(numero2)+ ' é ' +str(soma)+'.')