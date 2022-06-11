##Este programa tem como objetivo formatar de forma apropriada
##códigos html que estão visualmente mal organizados

from bs4 import BeautifulSoup
destination_path= "index.html"
with open(destination_path,'r') as file:
    contents = file.read()
    soup = BeautifulSoup(contents,'lxml')
    with open(destination_path,'w') as file:
        file.write(soup.prettify())
