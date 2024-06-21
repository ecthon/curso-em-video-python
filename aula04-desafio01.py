
# Desafio 1
# Crie um script Python que leia o nome de uma pessoa e mostre uma messagem de boas-vindas de acordo
# com o valor digitado.

nome = input("Qual é seu nome? ")

# Modo 1 - Utilizando F-strings (Python 3.6+)
# Neste exemplo, o f antes das aspas indica que é uma f-string, 
# que permite inserir expressões Python dentro da string, incluindo variáveis entre chaves {}.
print(f"Olá {nome}! Seja bem-vindo.")

# Modo 2 - Utilizando o método `.format()`
# Neste caso, `{}` dentro da string é substituído pelo valor de `nome` passado como
# argumento para o método `format()`.
print('Olá {}! Seja bem-vindo.'.format(nome))

# Modo 3 - Concatenando strings manualmente
# Neste método, você concatena strings usando o operador +. No entanto, em Python,
# a formatação de string com f-strings ou .format() é geralmente considerada mais legível e pythonica.
print('Olá ' + nome + '! Seja bem-vindo.')