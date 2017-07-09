import requests

from bs4 import BeautifulSoup

pages=5
url = 'http://abesit.in/author/webmaster/'
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, 'lxml')

fw = open('abesitwebmaster.txt', 'w')
dict={}
# title=[]
# content=[]
# for item in soup.findAll('h2', {'class' : 'entry-title'}):
#     print(item.contents[0])
# header->a->href


# for item in soup.findAll('article', {'class' : 'post'}):
#     title = item.find('h2', {'class' : 'entry-title'}).contents[0].strip()
#     content = item.find('div', {'class' : 'entry-content'}).find('p').contents[0].strip()
#     dict[title] = content

    # print(title + '\n' + content + '\n\n')

# for k, v in dict.items():
#     print(k+'\n'+v+'\n\n')

for item in soup.findAll('article', {'class' : 'post'}):
    title = item.find('h2', {'class' : 'entry-title'}).contents[0].strip()
    content = item.find('div', {'class' : 'entry-content'}).find('p').contents[0].strip()
    link = (item.find('header').find('a'))['href']
    imgurl = (item.find('img'))['src']
    print(link+'\n'+title+'\n'+content+'\nImageUrl: '+imgurl+'\n\n')





    # dict[title] = content


#
# for k, v in dict:
#     print(k +'\n'+v+'\n\n')
#     fw.write(title + '\n' + content + '\n\n')
#
# fw.close()
