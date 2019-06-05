import json # Importa um arquivo com um formato de interc�mbio de dados leve inspirado por JavaScript
import os # Dentre tantas funcionalidades, este m�dulo fornece tamb�m uma maneira port�til de usar a funcionalidade dependente do sistema operacional
from pylab import* # Dentre suas funcionalidades, assumir� a fun��o de gerar os gr�ficos
import urllib.request # Assumir� a fun��o de definir fun��es e classes que ajudam na abertura de URLs
import requests # Junto a BeautifulSoup abre v�rias ferramentas para serem utilizadas na extra��o de dados
from bs4 import BeautifulSoup #Essa biblioteca possibilita fazer a extra��o dos dados de uma forma mais pr�tica
#!/usr/bin/python
#! -*- encoding:utf-8 -*-

#LISTAS CRIADAS PARA ARMAZENAR A EXTRA��O DAS URL's
arquivos = ["armazena_extracao.txt"]
lista1=[]# NO DECORRER DO C�DIGO, MOSTRAREI A UTILIDADE DESSA LISTA
lista2=[]# NO DECORRER DO C�DIGO, MOSTRAREI A UTILIDADE DESSA LISTA

#ABERTURA DO ARQUIVO JSON
def abertura ():
     with open("analise.json","r") as data_file:
          data = json.load(data_file) 
     data_file.close()
     return data 

#AN�LISE DE INSER��O DO USU�RIO
def analise (data):
     abrir = True
     while abrir == True:

          letter =(input("Informe a Palavra:")).lower()#RECEBE A PALAVRA DA ENTRADA PADR�O E P�ES EM MINUSCULO PARA PADRONIZAR A LEITURA
          
          
          if letter in data:
               lista = data[letter]
               print(lista)
                             
               abrir = False
               return letter
          else:
               print('Palavra inv�lida')
         
#PROCURA NO ARQUIVO JSON AS NOT�CIAS
def procura_armazenamento (data,letter):
     #VARI�VEL "STRINGS" ARMAZENA A LISTA REFERENTE A CHAVE DIGITADA PELO USU�RIO
     #Ex.: "nome" : ["Martin", "Luther", "King", "Malcolm"] -> ESSA LISTA SER� ARMANEZADA EM "STRINGS"
     strings= data[letter]  
     # VARI�VEL CRIAR� UM VETOR E ORDENAR� A POSI��O DE CADA UM
     # Ex.: ["Martin", "Luther", "King", "Malcolm"], NESSA SITUA��O TEMOS 4 ELEMENTOS
     pos= arange(len(data[letter]))
     #ABRIR� O DIRET�RIO E ANALISAR� TODOS OS ARQUIVOS INSERIDOS NELE.
     files = [f for f in os.listdir(".") if f.startswith("armazena_extracao.txt") and f.endswith('.txt')]
     # 1� FOR TER� UTILIDADE DE PERCORRER TODOS OS TXT'S ALOCADOS NO DIRET�RIO
     for filename in files:
          #ESSAS VARI�VEIS AQUI, ASSUMIRAM O PAPEL DE ZERAR QUANDO FOR FEITA UMA ITERA��O
          lista1=[]
          lista2=[]
          with open(filename,encoding='utf-8', mode ='r') as f:
               arquivo = f.read()
          
               # 2� FAR� A COMPARA��O DE CADA ELEMENTO DA VARI�VEL "STRINGS" COM CADA ELEMENTO DO ARQUIVO TXT
               for s in strings:
                    print (filename, s, arquivo.count(s))
                    # LISTA1 ARMANEZA OS ELEMENTOS EM COMUM
                    lista1.append(s)
                    #LISTA2 ARMAZENA A INCID�NCIA DAS PALAVRAS NO TXT
                    lista2.append(arquivo.count(s))
          f.close()
     return lista1,lista2,pos
     
def grafico(lista1,lista2,pos):
#AP�S A PROCURA DO JSON NO ARQUIVO GERAREMOS O GR�FICO(HISTOGRAMA)
     bar(pos,lista2, align='center', color='orange')
     xticks(pos, lista1)
     plt.title("ScrapingWeb")
                       
     show()
     print(len(lista1))
     print(lista2)              
     
# FUN��O COM O PROP�SITO DE FAZER O SCRAPINGWEB
def url_search():
     try:
          #ABRE O ARQUIVO ONDE H� AS URL's PR� DEFENIDAS E AS DECODIFICA PARA A LEITURA DO PYTHON
          with open("Exemplo.txt",encoding='utf-8',mode='r') as data_file:
               #INICIALIZA A VARIAVEL PARA INSER��O DOS TEXTOS LIDOS NAS URL's
               soup_text = ""
               for line in data_file:
                    html_content = urllib.request.urlopen(line)
                    soup = BeautifulSoup(html_content,"lxml")
                    soup_text += soup.get_text()
               
          data_file.close()
          
          #ABRE ARQUIVO ONDE FORAM ARMAZENADOS OS TEXTOS DAS URL's
          with open("armazena_extracao.txt",encoding='utf-8',mode='a+') as out:
               out.write(soup_text)
               #print(out.write)
          
          
          out.close()
     #TRATAMENTO DE EXCE��ES PARA POSSIVEIS ERROS
     except ValueError:
          print("Url incompat�vel, certifique-se e digite novamente!")
     except TypeError:
          print("Error, tente novamente!")
     except urllib.error.HTTPError:
          print("Erro de solita��o de autentica��o")
     except urllib.error.ContentTooShortError:
          print("A quantidade de dados baixados � menor que o valor esperado")
     except urllib.error.URLError:
          print("Error!!! N�o h� conex�o de rede")
               
                                 


url_search() 
# FOR UTILIZADO PARA LER 3  VEZES O ARQUIVO "armazena_extracao.txt" COM  INSER��ES DIFERENTE DO USU�RIO
for i in range(6): 
     retorno = abertura()
     palavra = analise (retorno)
     lista1,lista2,pos= procura_armazenamento (retorno,palavra) 
     grafico(lista1,lista2,pos)      