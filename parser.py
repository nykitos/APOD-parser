import requests
from bs4 import BeautifulSoup


print('Получаю ссылку на изображение')
try:
    r = requests.get(r'https://apod.nasa.gov/apod/astropix.html')
except:
    print('Отсутствует соединение')
    input()
    exit()
html =  r.text
soup = BeautifulSoup(html, 'lxml')
path_img = str(soup.find_all('a')[1]).split('\"')[1]
url = 'https://apod.nasa.gov/apod/'+ str(path_img)
print(f'Ссылка: {url}')
print('Начинаю загрузку')
file_data = requests.get(url, stream=True)
name = url.split('/')[-1]
file = open(name, 'bw')
for chunk in file_data.iter_content(4096):
        file.write(chunk)
