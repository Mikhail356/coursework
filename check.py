import aiosqlite
import sqlite3
import sys
import requests
import bs4
from dateutil.parser import parse

if len(sys.argv) < 3:
  print("Err inp parametres:", sys.argv[0], "way_to_.html_file",
                                 'url_on_this_page', sep = ', ')
  sys.exit()

#----Проверка базы данных и составление списка кортежей из нее----
db = sqlite3.connect('webmention-logger.sqlite')
cursor = db.cursor()
cursor.execute("SELECT * FROM webmentions")
record = cursor.fetchall()
cursor.close()

# эта часть для чтения/записи в файл даты последней проверки
#  и подготовки таблицы
s = sys.argv[1]
s = s.split('/')
way, i ='', 0
while i != len(s)-1:
  way += s[i]
  way += '/'
  i+=1
way += 'd_check'

with open(way, 'r+') as f:
  datetime = f.readline()
datetime = parse(datetime)
'''   #UNCOMENT THIS PART IN FUTURE
with open(way, 'w') as f:
  f.write(record[-1][3])
'''
for i in record:
  if parse(i[3]) < datetime:
    record.remove(i)
#-----------------------------------------------------------------
with open(sys.argv[1]) as fp:
    soup = bs4.BeautifulSoup(fp, features="html5lib")

# record - список новых записей в бд после последнего скачивания

# Проверка всех новых обращений к текущей странице
# и добавление в список всех откликнувшихся страниц

  # Parsing url's wm-server 
wm = soup.find_all('link')
for i in wm:
  if i['rel'][0] == 'webmention':
    wm = i['href']
    break
else:
  print('Who is webmention server?')
  sys.exit()
  # end parse ^

cur_link = sys.argv[2]#"http://127.0.0.1:808" + s[-2] + '/'
to_add, to_remove = [], []
for i in record:
  if i[2] == cur_link and 'http://'+i[-1] == wm:
    try:
      fil = requests.get(i[1])
      fil.encoding = "html5lib"
      tmp = bs4.BeautifulSoup(fil.text, features="html5lib")
      tmp = tmp.title.text.split()
      name = tmp[0]+' '+tmp[1][0]+'. '+tmp[2][0]+'.'
      to_add.append((i[1], name)) # for add url and/or name on page
    except OSError:
      to_remove.append(i[1]) # for remove url on page

# итоговые списки для изменения данных страницы это to_add to_remove
print('I want to change this part:','\t to_add:', to_add, 
                                    '\t to_remove:', to_remove, 
                                    sep = '\n')
print("(Y/N):", end = ' ')
ans = str(input()).lower()
if(ans == 'y'):
  step = soup.find(class_ = "h-istina-coauthors")
  find = step.find_all(class_ = 'p-name u-url')

  if len(to_add) > 0:
    for i in to_add:
      for j in find:
        check = j.contents[0][0:-1]
        if i[1] == check:
          j['href'] = i[0]
          break
      else:
        upd = find[-1].contents[0][0:-1]+','
        find[-1].string = upd
        add = bs4.BeautifulSoup('<span class=\"h-card\"></span>', 
                                features = 'html5lib')
        an = add.span
        new_tag = add.new_tag("a", class_="p-name u-url", href = i[0])
        an.append(new_tag)
        add.span.a.string = i[1]+'.'
        add.span.a.attrs = {'class':'p-name u-url', 
                            'href': add.span.a.attrs['href']}
        step.append(add.span)

  if len(to_remove) > 0:
    find = step.find_all(class_ = 'p-name u-url')
    for i in to_remove:
      for j in find:
        check = j.contents[0][0:-1]
        if i[1] == check:
          j['href'] = ' '
          print(check, j.contents[0][0:-1], find)
  print(soup.prettify(formatter='html5'))

  with open(sys.argv[1], 'w') as fp:
    fp.writelines(str(soup.prettify(formatter='html5')))
