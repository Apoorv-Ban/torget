# TorGet torrent getter 
# made by Apoorv Bandyopdhyay
# A simple cli based application to get the best torrent for your favorate application without all the hassal and irritating pop ups 
#Version 1.0 made by python 3.10.8 
#Gets the result with 1337x.to(more will be added in the future) make sure the url works on your network
#tested with qbittorrent 

#importing libraries
from fileinput import hook_encoded
import random
from sqlite3 import DataError
import requests
from bs4 import BeautifulSoup
import os
import time 
import webbrowser


wipe = "" 
printlist = []
url = 'https://www.1337x.to/'

#function to load torrent hompage
def HomePage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #tags
    namelist = soup.find_all(class_="coll-1 name")
    # seedlist = soup.find_all(class_="coll-2 seeds")
    # leechlist = soup.find_all(class_="coll-3 leeches")
    datelist = soup.find_all(class_="coll-date")
    

    
    

    SplitList(namelist  , datelist)
    PrintResult(printlist)
    userinput = int(input('# Select Torrent ==> '))
    os.system(wipe)
    GetTorrent(userinput)

#function to split text 
def SplitList(namelist , datelist):
    
    listsize = len(namelist)
    
    
    for x in range(0,listsize-1):
        if (str(namelist[x].text.strip()) == 'name'):
            x = x - 1
            continue
        else:
            href = namelist[x].find_all('a', href=True)

            infodict = {
                'num' : x,
                'name' : str(namelist[x].text.strip()),
                'date' : str(datelist[x].text.strip()),
                'href' : str(href[1]['href'])
                
            };
            printlist.append(infodict)


#function to print the result 
def PrintResult(printlist):
    os.system(wipe)
    print('Sno. Name Date')
    for x in range(0,len(printlist)-1):
        
        print( " # ",x ," ==> ",printlist[x]['name'],"\t",printlist[x]['date'])


#setting page url 
def SetPageUrl(page):
    os.system(wipe)
    print('# 1. Load more ?')
    print('# 2. back')
    userinput = int(input("# Enter Choice ==> "))
    if(userinput == 1):
        page = page + 1
        more = True
        return more , page
    else:
        more = False
        page = 1
        return more , page
    

#funtion to set url 
def DisplayPage(input):
    
    page = 1
    more = True
    url = 'https://www.1337x.to/'
    #choice statements 
    if(input ==  1):
        url = url + 'home/'
        HomePage(url)
    elif(input == 2):
        url = url + 'trending'
    elif (input == 3):
        url = url + 'top-100'
    elif (input == 4):
        while(more):
            url = url + "cat/Movies/"+ str(page) + "/"
            more , page = SetPageUrl(page)
    elif (input == 5):
        while(more):
            url = url + "cat/Games/"+ str(page) + "/"
            more , page = SetPageUrl(page)
    elif (input == 6):
        while(more):
            url = url + "cat/Music/"+ str(page) + "/"
            more , page = SetPageUrl(page)
    elif (input ==7 ):
        while(more):
            url = url + "cat/Anime/"+ str(page) + "/"
            more , page = SetPageUrl(page)
    elif (input ==8):
         while(more):
            url = url + "cat/TV/"+ str(page) + "/"
            more , page = SetPageUrl(page)

    return url


#fuction to load torrent page 
def GetTorrent(userinput):
    os.system(wipe)
    temp = False
    
    for x in printlist:
        if(x['num'] == userinput):
            TorPage(x['href'] , x['name'])
            temp = True
    if(temp == False):
        print('# Invalid input please try again')
        char = input('# press any key to continue')
        menu()
    

#function to set search url 
def AdvanceSearch(keyword):
    url = 'https://www.1337x.to/'
    search = 'sort-search/'
    sort = 'seeders'
    sort_keyword = '/'+ sort + '/desc/'
    page = 1
    category =''
     
    

    
    search = 'sort-category-search/'
    print('# Select Search Category')
    print('# 1.Movies')
    print('# 2.TV')
    print('# 3.Games')
    print('# 4.Application')
    print('# 5.Music')
    categoryinput = int(input('# Enter Choice ==> '))
    print('# Enter sort category')
    print('# 1.Seeders')
    print('# 2.Time')
    print('# 3.Leechers')
    print('# 4.Size')
    sortinput = int(input('# Enter choice ==> '))

    if(categoryinput == 1):
            category = 'Movies/'
    elif(categoryinput == 2):
            category = 'TV/'
    elif(categoryinput == 3):
            category = 'Games/'
    elif(categoryinput == 4):
            category = 'Apps/'
    elif(categoryinput == 5):
            category = 'Music/'
    else:
            print("invalid category")
        
    if(sortinput == 1):
            sort = 'seeders'
    elif(sortinput == 2):
            sort = 'time'
    elif(sortinput == 3):
            sort = 'leechers'
    elif(sortinput == 4):
            sort = 'size'
    else:
            print("invalid choice sorting by seeders")
        
    sort_keyword = '/'+ category  + sort + '/desc/'

    new_url = url + search + keyword + sort_keyword + str(page) + '/'
    return new_url

def NormalSearch(keyword):
    url = 'https://www.1337x.to/'
    search = 'sort-search/'
    sort = 'seeders'
    sort_keyword = '/'+ sort + '/desc/'
    page = 1
    category =''
    new_url = url + search + keyword + sort_keyword + str(page) + '/'
    return new_url
    
#function to get torrent page
def TorPage(torurl , name):
    url = 'https://www.1337x.to'
    pageurl = url + torurl
    response = requests.get(pageurl)
    soup = BeautifulSoup(response.text, 'html.parser')
    torlist = soup.findAll('ul', {'class' : 'list'})
    os.system(wipe)
    print('#' + name)
    print(' ' +torlist[2].text.strip() + '\n')
    print(' ' + torlist[1].text.strip() + '\n')
    print('# 1. Download')
    print('# 2 Open in Browser')
    print('# 3. Back to Menu')
    userinput = int(input(" # Enter your choice ==> "))
    if(userinput == 1):
        MagnetDownload(soup)
        menu()
    elif(userinput == 2):
        webbrowser.open(pageurl, new=1, autoraise=True)
        menu()
    else:
        menu()


#funtion for magnet download
def MagnetDownload(soup):
    alist = soup.findAll('ul')
    atags = alist[4].find_all('a' ,href = True)
    href = atags[5]['href']
    webbrowser.open(href, new=1, autoraise=True)

#fuction for search page    
def SearchPage(keyword):

    print('# 1. Normal Search(Directly display 1 torrent with max seeders)')
    print('# 2. Advance Search(Display list of torrents with sorting)')
    userinput = int(input('# Enter Choice ==> '))

    if(userinput == 1):
        newurl = NormalSearch(keyword)
        response = requests.get(newurl)
        soup = BeautifulSoup(response.text, 'html.parser')
        namelist = soup.find_all(class_="coll-1 name")
        datelist = soup.find_all(class_="coll-date")
        SplitList(namelist  , datelist)
        TorPage(printlist[0]['href'],printlist[0]['name'])
        
        
        
    elif(userinput ==2):
        newurl = AdvanceSearch(keyword)
        response = requests.get(newurl)
        soup = BeautifulSoup(response.text, 'html.parser')
        namelist = soup.find_all(class_="coll-1 name")
        datelist = soup.find_all(class_="coll-date")
        SplitList(namelist  , datelist)
        PrintResult(printlist)
        userinput = int(input('# Select Torrent ==> '))
        os.system(wipe)
        GetTorrent(userinput)


def menu():

    #getting os name for screen clear function
    name = os.name
    wipe = ""
    if name == 'nt':
        wipe = 'cls'
    else:
        wipe = 'clear'

    exit = True
    while(exit):
        userinput = 0
        os.system(wipe)
        print('# TorGet ==> Hassel free torent getter <==')
        print('# Enter Choice ')
        print('# 1.Browse')
        print('# 2.Search')
        print('# 3.Exit')
        userinput = int(input('Input ==> '))

        if(userinput == 1):
            os.system(wipe)
            print('# 1.Homepage')
            print('# 2. Trending')
            print('# 3.Top 100')
            print('# 4.Top Movies')
            print('# 5.Top Games')
            print('# 6.Top Music')
            print('# 7.Top Anime')
            print('# 8.Top TV')
            userinput = int(input("# Enter Choice ==> "))
            DisplayPage(userinput)
        elif(userinput == 2):
            os.system(wipe)
            userinput = str(input("# Enter Keyword ==> "))
            SearchPage(userinput)
        else:
            os.system(wipe)
            print('# Thank you for using ')
            exit = False
        
        

    
def main():

    
    
    menu()

if __name__ == '__main__':
    main()