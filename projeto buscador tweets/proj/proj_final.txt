
import json, csv

### Lendo o arquivo csv
arquivo = open("C:\projeto_LP_tweets_2022.csv", 'r',  encoding="utf-8")
planilha = csv.reader( arquivo, delimiter = ',', lineterminator = '\n')

lista_tweets = list(planilha)
arquivo.close()

#funcao para buscar tweets por data
def buscar_data(data):
        datas = []
        conteudo = []
        assunto_ = []
        print('data | conteúdo | assunto')
        ## um for para varrer todas as datas da lista_tweets e comparar com a data inputada
        for linha in range(len(lista_tweets)):
                data2 = lista_tweets[linha][0][0:10]                                         
                if data[0:2] == data2[8:11] and \
                    data[3:5] == data2[5:7] and \
                    data[6:12] == data2[0:4]:
                        datas.append(lista_tweets[linha][0])
                        conteudo.append(lista_tweets[linha][3])
                        assunto_.append(lista_tweets[linha][4])
                        print(f'{lista_tweets[linha][0][0:10][8:11]}/{lista_tweets[linha][0][0:10][5:7]}/{lista_tweets[linha][0][0:10][0:4]} | {lista_tweets[linha][3]} | {lista_tweets[linha][4]}')

        dic = {'data': datas, 'conteudo': conteudo, 'assunto': assunto_}
        return dic

#funcao para buscar termo no tweet
def buscar_termo(termo):
    datas = []
    conteudo = []
    assunto_ = []
    print('data | conteúdo | assunto')
    ## um for para varrer todas as datas da lista_tweets e comparar com a data inputada
    for linha in range(len(lista_tweets)):
        if termo in lista_tweets[linha][3]:
            datas.append(lista_tweets[linha][0])
            conteudo.append(lista_tweets[linha][3])
            assunto_.append(lista_tweets[linha][4])
            print(f'{lista_tweets[linha][0][0:10][8:11]}/{lista_tweets[linha][0][0:10][5:7]}/{lista_tweets[linha][0][0:10][0:4]} | {lista_tweets[linha][3]} | {lista_tweets[linha][4]}')

    dic = {'data': datas, 'conteudo': conteudo, 'assunto': assunto_}
    return dic

#funcao para buscar assunto no tweet
def buscar_assunto(assunto):
    print('data | conteúdo | assunto')
    datas = []
    conteudo = []
    assunto_ = []
    ## um for para varrer todas as datas da lista_tweets e comparar com o assunto
    for linha in range(len(lista_tweets)):
        if assunto ==  lista_tweets[linha][4]:
            datas.append(lista_tweets[linha][0])
            conteudo.append(lista_tweets[linha][3])
            assunto_.append(lista_tweets[linha][4])
            print(f'{lista_tweets[linha][0][0:10][8:11]}/{lista_tweets[linha][0][0:10][5:7]}/{lista_tweets[linha][0][0:10][0:4]} | {lista_tweets[linha][3]} | {lista_tweets[linha][4]}')

    dic = {'data': datas, 'conteudo': conteudo, 'assunto': assunto_}
    return dic

#funcao que salva em arquivo json
def salvar_busca(dic):
    json_object = json.dumps(dic) 
    with open('./Busca_json.json', "w") as outfile: 
        outfile.write(json_object)

def data_valida(data):
    try:
        dia, mes, ano = map(int, data.split('/'))
        if mes < 1 or mes > 12 or ano <= 0:
            return False

        if mes in (1, 3, 5, 7, 8, 10, 12):
            ultimo_dia = 31
        elif mes == 2:
            if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
                ultimo_dia = 29
            else:
                ultimo_dia = 28
        else:
            ultimo_dia = 30

        if dia < 1 or dia > ultimo_dia:
            return False

        return True
    except ValueError:
        return False

def menu():
    print('Boas vindas ao nosso sistema:')
    print('1 - Buscar tweets por data')
    print('2 - Buscar tweets por termo')
    print('3 - Buscar tweets por assunto')
    print('4 - Salvar resultado da busca')
    print('5 - Sair')

menu()
option = input('Escreva sua opção: ')
print()

while option != 5:
    if option == 1: 
        data = input('Digite uma data no formato dd/mm/aaaa: ')
        if data_valida(data):
            dic = buscar_data(data)
        else:
            print('Atenção!! Formato da data não é válida, seguir o padrão dd/mm/aaaa')
    elif option == 2:
        termo = input('Digite um termo: ')
        dic = buscar_termo(termo)
    elif option == 3:
        assunto = input('Digite um assunto: ')
        dic = buscar_assunto(assunto)
    elif option == 4:
        salvar_busca(dic)
    else:
        print('Opção Inválida. Tente Novamente.')
        
    print()
    menu()
    option = int(input('Escreva sua opção: '))

print('Obrigado por usar nosso programa. Até a próxima!')




