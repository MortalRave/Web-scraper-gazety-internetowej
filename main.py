from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

http = 'http://www.gloszabrza24.pl'
url = urlopen(http)

bs = BeautifulSoup(url,'html.parser')

choice = 0

#Wyświetlenie artykułu
def article(ch, links):

    os.system('clear')

    httpchoice = http + links[int(ch)-1]
    urlchoice = urlopen(httpchoice)
    bschoice = BeautifulSoup(urlchoice, 'html.parser')
    c = 0
    for child in bschoice.find_all('tr'):
        c += 1
        if c == 5 or c == 3:
            print(child.get_text().lstrip())

    nextchoice = input('Chcesz kontynuować? y/n\n')
    if nextchoice == 'n':
        os.system('clear')
    elif nextchoice == 'y':
        os.system('clear')
        menu()
    else:
        os.system('clear')
        print('Nie ma takiej opcji, program zostanie zamknięty.')

#Wyświetlanie menu
def menu():
    os.system('clear')
    count = 0
    links = []
    titles = []
    for link in bs.find_all('a',{'class':'contentpagetitle'}):
        count+=1
        if count == 13:
            pass
        else:
            if 'href' in link.attrs:
                links.append(link.attrs['href'])
                titles.append(link.get_text())

    print('Głos Zabrza\n')
    print('Wybierz artykuł')
    for i in range(len(links)):
        if i < 9:
            print(f'' + str(i + 1) + '.  ' + (titles[i]).lstrip())
        else:
            print(f'' + str(i + 1) + '. ' + (titles[i]).lstrip())
    
    choice = input("Jaki artykuł otworzyć?\n")
    
    try:
        article(choice,links)
    except:
        os.system('clear')
        nextchoice = input("Nieodpowiedni wybór, chcesz kontynuować? y/n\n")
        if nextchoice == 'y':
            menu()
        else:
            os.system('clear')
            print('Program zostanie zamkniety.')

menu()
