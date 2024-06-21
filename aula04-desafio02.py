
# Desafio 2
# Crie um script Python que leia o dia o mês e o ano de nascimento de uma pessoa
# e mostre uma mensagem  com a data formatada.

dia = input("Dia: ")
mes = input("Mês: ")
ano = input("Ano: ")

# Modo 1 - Utilizando F-strings (Python 3.6+)
# Neste exemplo, o f antes das aspas indica que é uma f-string, 
# que permite inserir expressões Python dentro da string, incluindo variáveis entre chaves {}.
print(f"Você nasceu no dia {dia} de {mes} de {ano}. Correto?")

# Modo 2 - Utilizando o método `.format()`
# Neste caso, `{}` dentro da string é substituído pelo valor de `nome` passado como
# argumento para o método `format()`.
print('Você nasceu no dia {} de {} de {}. Correto?'.format(dia,mes,ano))

# Modo 3 - Concatenando strings manualmente
# Neste método, você concatena strings usando o operador +. No entanto, em Python,
# a formatação de string com f-strings ou .format() é geralmente considerada mais legível e pythonica.
print('Você nasceu no dia ' + dia + ' de ' + mes+ ' de ' + ano +'. Correto?')