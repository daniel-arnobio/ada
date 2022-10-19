string = 'ola mundo'
arquivo = open('ola_mundo.txt', 'w') ## cria arquivo para escrita
type(arquivo)
arquivo.write(string) ## o que eu quero passar pro arquivo txt

arquivo.close() ##SEMPRE FECHAR PARA CONSOLIDAR AS ALTERAÇÕES 


