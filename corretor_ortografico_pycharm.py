import nltk
'''
Foi usado 'pip install nltk' para fazer a instalação da biblioteca NLTK no terminal
O import foi realizado no código: 'import nltk'
'''

#____________________________CARREGANDO ARQUIVOS____________________________
with open("dados/artigos.txt", "r", encoding="utf8") as f:
    artigos = f.read()
'''
    Abrindo um arquivo usando python: função 'open()' que recebe dois parametros
  1 - caminho do arquivo e o nome com extensão
  2 - o tipo de atividade que será executada; r:ler, w:escreve, x:cria_escreve, a:abre_escreve_append
    Como queremos o texto, devemos usar o comando 'with' e ao final 'as f' significa 'como file'
ficando da seguinte forma: COM A FUNÇÃO OPEN NO ARQUIVO X NO MODO DE LEITURA COMO UM FILE
    E então podemos passar as ações que serão feitas nesse aquivo, que nesse caso, salvamos dentro de uma variável seu conteúdo,
usando a função '.read()' 
'''

#____________________________TRATAMENTO DO CORPUS TEXTUAL____________________________

def separa_palavras(corpus_textual):
    lista_tokens = nltk.tokenize.word_tokenize(artigos)
    lista_palavras = []
    for token in lista_tokens:
        if token.isalpha():
            lista_palavras.append(token.lower())
    return lista_palavras
'''
NLTK - Conjunto de ferramentas que implementa diversos metodos e algoritmos para análise textual.
Tokens são strings que contém textos e sinais, são feitos com palavras separadas e pode-se usar o metodo split para extrair
Necessário para descobrir a quantidade de palavras no CorpusTextual

    A função 'separa_palavras()' recebe o CorpusTextual, usa a biblioteca 'nltk' e a funçãoo '.word_tokenize()' para criar
# uma lista de tokens.
    O 'for' percorre toda a lista de tokens e questiona se o token é um caracter alphanumerico, se for verdade, ele é adcionado
na lista de palavras
    A função também aplica um lowerCase na palavra, normalizando sua saida.
No 'return' da função, é feito com o método 'set()', para retornar elementos distintos

Para tratar uma corpusTextual, só precisamos inicializa-lo em uma variável e passar como parametro da função 'separa_palavra'
'''
lista_palavras = separa_palavras(artigos)


def gerador_palavras(palavra):
    fatias = []
    for index in range(len(palavra)+1):
        fatias.append((palavra[:index], palavra[index:]))
    palavras_geradas = insere_letras(fatias)
    palavras_geradas += deletando_caracteres(fatias)
    palavras_geradas += troca_caracteres(fatias)
    palavras_geradas += inverte_caracteres(fatias)
    return palavras_geradas
'''    
    A função 'gerador_palavras' usa algoritmos que criam todas as possiveis formas de fatiamento de uma string, passeando
pelo index de acordo com o 'len'
    Assim, qualquer palavra que for escrita e for passada como parâmetro da função 'gerador_palavras()', passará pelas
funções de algoritmo, gerando todas as possiveis correções, limitadas ao algoritmo.
'''


#____________________________FUNÇÕES DO ALGORITMO DE CORREÇÃO____________________________

def insere_letras(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D)
    return novas_palavras
'''
    A função 'insere_letras' recebe como parametro as possiveis formas de fatiamento de uma string, como recebem em forma de 
tupla com indice (0,1), dividimos em E(querdo) e D(ireito)
    As possiveis inserções estão dentro da variável 'letras', o 'for' pegará letra por letra e vai adcionar a string fatiada
    O retorno dessa função, é uma lista com as possiveis inserções nas possiveis formas de fatiamento
'''

def inverte_caracteres(fatias):
    novas_palavras = []
    for E, D in fatias:
        if len(D) > 1:
            novas_palavras.append(E + D[1] + D[0] + D[2:])
    return novas_palavras
'''
    A função 'inverte_caracteres' recebe como parametro as possiveis formas de fatiamento de uma string, 
como recebem em forma de tupla com indice (0,1), dividimos em E(querdo) e D(ireito)
    Dentro de um 'for', percorre-se todas as fatias, trocando a letra de indice[0] pela letra de indice[1], sempre que o tamanho
do lado D(ireito) seja maior que 1, para que possa ocorrer a troca e o erro 'out_of_range' não ocorrer
    Dessa forma, a função retorna todas as possiveis inversões
'''

def deletando_caracteres(fatias):
    novas_palavras = []
    for E, D in fatias:
        novas_palavras.append(E + D[1:])
    return novas_palavras
'''  
    A função 'deletando_caracteres' recebe como parametro as possiveis formas de fatiamento de uma string, 
como recebem em forma de tupla com indice (0,1), dividimos em E(querdo) e D(ireito)
    Dentro de um 'for', percorre-se todas as fatias concatenando o lado E(querdo) completo e o D(ireito) fatiado a partir do 
primeiro caracter, fazendo com que a cada loop, uma palavra é gerada excluindo possiveis caracteres escritos a mais.
    O retorno dessa função, é uma lista com as possiveis exclusões nas possiveis formas de fatiamento 
  '''

def troca_caracteres(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D[1:])
    return novas_palavras
'''    
    A função 'troca_caractere' recebe como parametro as possiveis formas de fatiamento de uma string, 
como recebem em forma de tupla com indice (0,1), dividimos em E(querdo) e D(ireito)
    Dentro de um 'for', percorre-se todas as fatias concatenando o lado E(querdo) completo e o D(ireito) fatiado a partir do 
primeiro caracter e adicionando uma letra no lugar da primeira letra do lado direito, que foi deletada
    Dessa forma fazemos uma troca de todas as formas possiveis e salvamos numa lista.
O retorno dessa função, é uma lista com as possiveis trocas nas possiveis formas de fatiamento 
'''


#____________________________FUNÇÃO DO CORRETOR____________________________
frequencia = nltk.FreqDist(lista_palavras)
def probabilidade(palavra_gerada):
    total_palavras = len(lista_palavras)
    return frequencia[palavra_gerada]/total_palavras
'''
    Para calcular a frequencia das palavras, usamos uma função da biblioteca nltk, 'nltk.FreqDist, que calcula
a distribuição de frequencia das palavras, recebe como parametro a lista de palavras do corpusTextual
    É importante que a variavel 'frequencia' esteja fora da função 'probabilidade', isso diminui o tempo de execução
do programa enquanto estiver no looping, mas não resolve o tempo de execução do carregamento e tratamento dos dados
'''

def corretor(palavra):
    palavras_geradas = gerador_palavras(palavra)
    palavra_correta = max(palavras_geradas, key=probabilidade)
    return palavra_correta
'''
    A função 'corretor', vai chamar a função 'gerador_palavras' dentro de uma variável 'palavras_geradas', 
vai criar uma variável 'palavra_correta' que recebe uma built-in chamada 'max', que retorna a probabilidade 
de cada uma das palavras geradas ser a palavra correta
    São passados dois parametros para a função 'max'
  1 - 'palavras_geradas': Variável criada que recebe o retorno da função 'gerador_palavras()'
  2 - 'key=probabildiade': Função que calcula a probabilidade da palavra correta 
'''



#____________________________FUNÇÃO EXCLUSIVA DO PYCHARM PARA TESTAR O CORRETOR____________________________
while True:
    palavra = input('Palavra: ')
    if corretor == '0':
        break
    else:
        resultado = corretor(palavra)
        print(resultado)
'''
    O tempo de execução da leitura e tokeninzação do arquivo de corpusTextual é alto, principalmente no PyCharm
    O loop criado no final (while True) permite testar a função 'corretor' pulando a parte de carregar e tratar os dados
    Para sair, basta digitar '0' e apertar 'Enter', o programa será encerrado
'''
