from bs4 import BeautifulSoup
from requests_html import HTMLSession
import spacy



session = HTMLSession() # Criando a sessão

# settando os sites que iremos usar
sites = ['https://hbr.org/2022/04/the-power-of-natural-language-processing',
         'https://towardsdatascience.com/your-guide-to-natural-language-processing-nlp-48ea2511f6e1',
         'https://www.tutorialspoint.com/artificial_intelligence/artificial_intelligence_natural_language_processing.htm',
         'https://path.com.br/noticias/o-que-e-natural-language-processing/',
         'https://www.lexalytics.com/blog/machine-learning-natural-language-processing/']

matrix = []

for site in sites:
  r = session.get(site) # Acessando os sites
  req = r.content
  soup = BeautifulSoup(req, 'html.parser')

  all_text = soup.find_all('p')# Pegando todos os <p>{conteúdo}</p> do site
  
  nlp = spacy.load("en_core_web_sm") # Usando o spacy
  all_sents = []
  
  for txt in all_text:
    doc = txt.get_text()
    document = nlp(doc).sents
    
    for doc in document:
      all_sents.append(doc)
  
  
  
  # Criando um vetor que o conteúdo é uma matrix, e o vetor 0
  # é o primeiro site, o vetor 1 é o segundo site....
  

  # Para organizar os sites tem como fazer em dicionário.

  matrix.append(all_sents)