 
import lxml 
# with open('template.html','r') as file:
#      content= file.read()
import os
from bs4 import BeautifulSoup
path=os.getcwd()
print(path)
files=os.path.join(os.getcwd(),'template.html') 
with open(files,'r') as file:
      content= file.read()
soup= BeautifulSoup(content,'lxml')
print(soup)
print("------------------------------",soup.prettify())