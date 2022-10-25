from pyrsistent import v
import csv

with open('projeto_LP_tweets_2022.csv', 'r') as file:
    file_csv = csv.reader(file, delimiter='')
    for line in  file_csv:
        dict tweets


def menu():
    print('Boas vindas ao nosso sistema:')
    print('1 - Buscar tweets por data')
    print('2 - Buscar tweets por termo')
    print('3 - Buscar tweets por assunto')
    print('4 - Salvar resultado da busca')
    print('5 - Sair')

menu()
option = int(input('Escreva sua opção: '))

while option != 5:
    if option == 1:
        option1()
    
    elif option == 2:
    
    elif option ==3:

    elif option == 4:

    elif option == 1:
    
    else:
        print('Opção Inválida. Tente Novamente.')

    print()
    menu()
    option = int(input('Escreva sua opção: '))

print('Obrigado por usar nosso programa. Até a próxima!')