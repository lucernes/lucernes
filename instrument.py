import random
from bs4 import BeautifulSoup
import requests
import lxml
print("выберите нужный инструмент")
choi = input('1 = generation password, 2 = htmlparser\n\n\n\n>>>>: ')
if choi == '1':
  letters = input("введите ключевые слова:\n>>>>: ")
  num = int(input("Ведите колчиство паролей:\n>>>>: "))
  length = int(input("введите длину пароля:\n>>>>: "))
  for x in range(num):
    password = '' 
    for i in range(length):
        password += random.choice(letters)
    print(password)
elif choi == '2':
  url = input('введите ссылку на сайт:\n>>>>: ')
  tags = input(str('теги по которым вы будете искать текст:\n>>>>: '))
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "lxml")
  quotes = soup.find_all(tags)
  
  for quote in quotes:
    print(quote.text)
