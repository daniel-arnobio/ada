
import json, csv

### Lendo o arquivo csv
arquivo = open('C:\projeto_LP_tweets_2022.csv', 'r',  encoding="utf-8")
planilha = csv.reader(
    arquivo, 
    delimiter = ',', 
    lineterminator = '\n')

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
                        #dia                    #mes                       #ano
                if data[0:2]==data2[8:11] and data[3:5]==data2[5:7] and data[6:12]==data2[0:4]:
                        #data           #conteudo                #assunto
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
    with open(r"C:\Users\Jorge Lira\Downloads\colab\Aula 2\projeto\busca.json", "w") as outfile: 
        outfile.write(json_object)


def menu():
    print('Boas vindas ao nosso sistema:')
    print('1 - Buscar tweets por data')
    print('2 - Buscar tweets por termo')
    print('3 - Buscar tweets por assunto')
    print('4 - Salvar resultado da busca')
    print('5 - Sair')

menu()
option = int(input('Escreva sua opção: '))
print()

while option != 5:
    if option == 1: 
        data = input('Digite uma data no formato dd/mm/aaaa: ')
        dic = buscar_data(data)
    elif option == 2:
        termo = input('Digite um termo: ')
        dic = buscar_termo(termo)
    elif option ==3:
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


























