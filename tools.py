import random
from bs4 import BeautifulSoup
import requests
import lxml
import os
version = '1.0'
print("выберите нужный инструмент")
choi = input('1 = generation password\n2 = htmlparser\n3 = сканер nmap без ввода команд в терминале\n\nVERSION: 1.1\n>>>>: ')
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
elif choi == '3':
  devs = input('ip адрес жертвы: ')
  dev = str(devs)
  opt = input("введите что вы хотите сканировать:\n1 = Сканировать Все Порты\n2 = Определить какие IP Протоколы (TCP, UDP, ICMP, и т.д.) поддерживает сканируемый хост\n3 - определение OC\n>>>>: ")
  if opt == '1':
    os.system(f'nmap -p "*" {dev}')
  if opt == '2':
    os.system(f"nmap -sO {dev}")
  if opt == '3':
    os.system(f"nmap -O {dev}")