import nltk
'''
Foi usado 'pip install nltk' para fazer a instalação da biblioteca NLTK no terminal
O import foi realizado no código: 'import nltk'
'''

#____________________________CARREGANDO ARQUIVOS____________________________
with open("dados/baseDados.txt", "r", encoding="utf8") as f:
    dados = f.read()
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
    lista_tokens = nltk.tokenize.word_tokenize(dados)
    lista_palavras = []
    for token in lista_tokens:
        if token.isalpha():
            lista_palavras.append(token.lower())
    return lista_palavras
lista_normalizada = separa_palavras(dados)
vocabulario = set(lista_normalizada)
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


def gerador_palavras(palavra):
    fatias = []
    for index in range(len(palavra)+1):
        fatias.append((palavra[:index],palavra[index:]))
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


def aumenta_escopo(palavras_geradas):
    novas_palavras = []
    for palavra in palavras_geradas:
        novas_palavras += gerador_palavras(palavra)
    return novas_palavras
'''
A função 'aumenta_escopo()' recebe como parametro as 'palavras_geradas' no primeiro gerador, que chama mais uma vez a 
função 'gerador_palavras()' fazendo com que a palavra seja verificada duas vezes, aumentando o tamanho do escopo em que
o usuário pode cometer erros ortográficos
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
frequencia = nltk.FreqDist(lista_normalizada)
def probabilidade(palavra_gerada):
    total_palavras = len(lista_normalizada)
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
    A função 'corretor2', vai chamar a função 'gerador_palavras' dentro de uma variável 'palavras_geradas'
    Uma variável 'todas_palavras' receberá todas as palavras criadas a partir das da função geradora
    Vai criar uma variável 'palavra_correta' que recebe uma built-in chamada 'max', que retorna a probabilidade 
de cada uma das palavras geradas ser a palavra correta
'''

def novo_corretor(palavra):
    palavras_geradas = gerador_palavras(palavra)
    melhor_escolha = [palavra]
    palavras_escopo = aumenta_escopo(palavras_geradas)
    todas_palavras = set(palavras_geradas + palavras_escopo)
    for palavra in todas_palavras:
        if palavra in vocabulario:
            melhor_escolha.append(palavra)
    palavra_correta = max(melhor_escolha, key=probabilidade)
    return palavra_correta
'''    
    A função 'corretor2', vai chamar a função 'gerador_palavras' dentro de uma variável 'palavras_geradas', e vai aumentar
o escopo de erros de digitação com a função 'aumenta_escopo()' que recebe a variável 'palavras_geradas'.
    Uma variável 'todas_palavras' receberá todas as palavras criadas a partir das da função geradora e da função que aumenta
seu escopo, salvando as possiveis candidatas a palavra correta na variável 'melhor_escolha'
    Vai criar uma variável 'palavra_correta' que recebe uma built-in chamada 'max', que retorna a probabilidade 
de cada uma das palavras geradas ser a palavra correta
    São passados dois parametros para a função 'max'
 1 - 'palavras_geradas': Variável criada que recebe o retorno da função 'gerador_palavras()'
 2 - 'key=probabildiade': Função que calcula a probabilidade da palavra correta 
'''

#____________________________FUNÇÃO AVALIADORA DE ACERTOS____________________________
def cria_dados_teste(nome_arquivo):
    lista_palavras_teste = []
    f = open(nome_arquivo, "r", encoding='utf-8')
    for linha in f:
        correta, errada = linha.split()
        lista_palavras_teste.append((correta, errada))
    f.close()
    return lista_palavras_teste

lista_teste = cria_dados_teste('dados/palavras.txt')
'''
    Uma função, que vai criar dados para testar na função avaliadora, é criada, nela passamos o aquivo de testes e tratamos
para que retorne uma lista com essas palavras
'''

def avaliador(testes, vocabulario):
    numero_palavras = len(testes)
    acertou = 0
    desconhecida = 0
    for correta, errada in testes:
        palavra_corrigida = corretor(errada)
        desconhecida += (correta not in vocabulario)
        if palavra_corrigida == correta:
            acertou += 1
    taxa_acerto = acertou / numero_palavras
    taxa_desconhecida = desconhecida / numero_palavras
    print(f'Taxa de acerto: {round((taxa_acerto) * 100, 2)}%')
    print(f'Taxa de palavras desconhecidas: {round((taxa_desconhecida) * 100, 2)}%')
'''    
    A função 'avaliador()' foi criada afim de testar a taxa de acerto fazendo com que o 'corretor()' corrija uma lista de 
palavras, passando as corretas para a avaliação.
    Essa função auxilia no desenvolvimento do programa para contestar sua acuracidade 
'''


#____________________________FUNÇÃO EXCLUSIVA DO PYCHARM PARA TESTAR O CORRETOR____________________________

texto_escolha = ('Escolha entre 3 opções abaixo: \n'
                 'Corretor simples      - 1\n'
                 'Corretor de 2 erros   - 2\n'
                 'Finalizar programa    - 3\n'
                 'Opção: ')

def menu_selecao(escolha):
    while True:
        if escolha == '1':
            resultado = corretor(input('Palavra: '))
            print(resultado)
        elif escolha == '2':
            resultado = novo_corretor(input('Palavra: '))
            print(resultado)
        elif escolha == '3':
            print('Programa finalizado.')
            break
    return escolha

menu_selecao(input(texto_escolha))
'''
    O tempo de execução da leitura e tokeninzação do arquivo de corpusTextual é alto, principalmente no PyCharm
    O loop criado no final (while True) permite testar a função 'corretor' pulando a parte de carregar e tratar os dados
'''