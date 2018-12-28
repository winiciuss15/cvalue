import pandas as pd
import sys 
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk.corpus import stopwords
import time
import math
# time python ex2.py a.csv

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')

def wordList(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))


ini = time.time()
textos = pd.read_csv(sys.argv[1])
print(textos['ab'])

print("\n ")
print("Iniciando Cvalue em: " + str(len(textos)) + " grupos")

for z in range(len(textos)): 
    

    print("\n ")
    print("ENTRANDO NO LOOP: " + str(z))
    print("\n ")
    a = textos['ab'][z]

    print("leu grupo " + str(z))

    print("\n ")

    tokens = nltk.word_tokenize(a)

    print("token")

    # stop_words=set(stopwords.words("english"))

    print("\n ")

    b = nltk.pos_tag(tokens)

    print("tagueou")

    texto = pd.DataFrame(data = b, columns = ['terms', 'token']) 

    print texto.head(n = 20)

    print("\n ")

    teste = texto['token']
    terms = texto['terms']

    tags = ['NP', 'JJ', 'NN', 'NNS', 'NPS']

    token = [] 
    i = 0

    while i < len(teste):
        #if i == 0:
        #    print 'inicio do loop
        #print('loop i: ' + str(i))
        if teste[i] in tags or i  == 9:
            # print('tag i: ' + str(i) + ' encontrada ')
            f = False
            j = i + 1
            temp = ''
            while f == False:
                #print('Entra no While ' + str(j))
                if j < len(teste):
                    if teste[j] in tags:
                        #print('tag j: ' + str(j) + ' encontrada ')
                        if temp == '':
                            temp = terms[i] + ' ' + terms[j]
                        else:
                            temp = temp + ' ' + terms[j]
                        #print(temp)
                        j = j + 1
                    else:
                        f = True
                else:
                    f = True
            token.append(temp)
            i = j
        else:
            i += 1

    token = filter(None, token)

    token2 = wordList(token) 
    token3 = pd.DataFrame(token2.items(), columns = ['w', 'Freq'])
    token3['Size'] =  token3['w'].apply(lambda x: len(str(x).split(" ")))
    token3['log'] = token3['Size'].apply(lambda x: math.log(x,2))
    token3['cvalue'] = token3['log'] * token3['Freq'] 
    token4 = token3.sort_values(by='cvalue', ascending = False)

    print(token4)

    print("\n ")

    print token4.shape

    print("\n ")

    token4.to_csv("cv"+ str(z) +".csv")
    
    print("Ecreveu csv grupo: " + str(z))

    print("\n ")
    fim = time.time()
    tempo = (fim-ini)/60
    print("Realizado em: " + str(tempo) + " minutos" )
    #
