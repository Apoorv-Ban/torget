# TorGet torrent getter 
# made by Apoorv Bandyopdhyay
# A simple cli based application to get the best torrent for your favorate application without all the hassal and irritating pop ups 
# Version 1.0 made by python 3.10.8 
# Gets the result from 1337x.to(more will be added in the future) make sure the url works on your network
# tested with qbittorrent 

#importing libraries

import random
from sqlite3 import DataError
from matplotlib.streamplot import OutOfBounds
import requests
from bs4 import BeautifulSoup
import os
import time 
import webbrowser


wipe = "" 
url = 'https://1337x.to/home/'




#function to load torrent hompage
def HomePage(url):
   
    os.system(wipe)
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        namelist = soup.find_all(class_="coll-1 name")
        datelist = soup.find_all(class_="coll-date")
        printlist = SplitList(namelist  , datelist)
        PrintResult(printlist)
        print("\n")
        print("-------------------------------------------------------------------------------------")
        print("  Press 1 to Select a Torrent for Downloading , Press 2 to go back to main menu")
        print("-------------------------------------------------------------------------------------")
        print("\n")
        print('# 1. Select Torrent')
        print('# 2. Back to Menu')
        print("\n")
        print("\n")
        
        userinput = int(input('# Enter Choice ==> '))
        if(userinput == 1 or userinput ==2):
            if(userinput == 1):
                userinput = int(input('# Select Torrent ==> '))
                GetTorrent(userinput ,printlist)
                
            else:
                menu()
        else:
            print('# Invalid Input Press enter to continue')
            char = input()
            menu()
    except Exception:
        print('# Unable to load homepage please check connection or run the program again')
        char = input('# Press Enter to Continue')
        menu()
        
        

#function to split text 
def SplitList(namelist , datelist):
    
    listsize = len(namelist)
    templist = []
    
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
            templist.append(infodict)
    return templist

def SearchList(namelist , datelist ):
    listsize = len(namelist)
    rlist = []
    
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
            rlist.append(infodict)
    return rlist


#function to print the result 
def PrintResult(printlist):
    os.system(wipe)
    print('Sno. Name Date')
    for x in range(0,len(printlist)-1):
        print( " # ",printlist[x]['num'] ," ==> ",printlist[x]['name'][0:-10],"\t",printlist[x]['date'])
        
    
    
    
    
#fuction to load torrent page 
def GetTorrent(userinput , printlist):
    os.system(wipe)
    
    

    for x in printlist:
        if(int(x['num']) == userinput):
            TorPage(x['href'] , x['name'])
            
    menu()    

#function to set search url 
def AdvanceSearch(keyword):
    searchlist = []
    os.system(wipe)
    url = 'https://www.1337x.to/'
    searchlist = []

    cleanedkeyword = keyword.strip()
    cleanedkeyword = cleanedkeyword.replace(" ",'+')

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
    print('# 6.XXX')
    print('# 7.Anime')
    print('# 8.Other')
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
    elif(categoryinput == 6):
            category = 'XXX/'
    elif(categoryinput == 7):
          category = 'Anime/'
    elif(categoryinput == 8):
          category ='Other/'
    else:
            print("invalid category")
            print('# Press Enter to Continue')
            char = input()
            menu()
        
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
            sort = 'seeders'
    sort_keyword = '/'+ category  + sort + '/desc/'

    new_url = url + search + cleanedkeyword + sort_keyword + str(page) + '/'
    return new_url




#function to get torrent page
def TorPage(torurl , name):
    url = 'https://www.1337x.to'
    pageurl = url + torurl
    response = requests.get(pageurl)
    soup = BeautifulSoup(response.text, 'html.parser')
    torlist = soup.findAll('ul', {'class' : 'list'})
    os.system(wipe)
    print('#' + name[0:-10])
    print(' ' + torlist[2].text.strip() + '\n')
    print(' ' + torlist[1].text.strip() + '\n')
    print('\n')
    print('-------------------------------------------------------------------------------------------------------')
    print('Press 1 to download using a torrent client, Press 2 to Open in Browser, Press 3 to go back to main menu')
    print('-------------------------------------------------------------------------------------------------------')
    print('\n')
    print('# 1. Download')
    print('# 2. Open in Browser')
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

            
            newurl = AdvanceSearch(keyword)
            response = requests.get(newurl)
            soup = BeautifulSoup(response.text, 'html.parser')
            namelist = soup.find_all(class_="coll-1 name")
            datelist = soup.find_all(class_="coll-date")
            if(len(namelist) == 0):
                    print('# Search error please try again later press any key to return to menu')
                    char = input()
                    menu()
            else:
                
                searchlist = SearchList(namelist  , datelist )
                PrintResult(searchlist)
                
                


                print("\n")
                print("-------------------------------------------------------------------------------------")
                print("Press 1 to Search Again Press 2 ,To select a torrent, 3 To go back to main menu")
                print("-------------------------------------------------------------------------------------")
                print("\n")
                print("# 1. Search again")
                print("# 2. Continue")
                print('# 3. Go back to Menu')
                userinput = int(input("# Enter Choice ==> "))
                if(userinput == 1):
                    keyword = str(input("# Enter Choice ==> "))
                    SearchPage(keyword)
                elif(userinput == 2):
                    userinput = int(input('# Select Torrent ==> '))
                    os.system(wipe)
                    GetTorrent(userinput,searchlist)
                else:
                    menu()
        
            
   
def menu():

    #getting os name for screen clear function
    
    name = os.name
    wipe = ""
    if name == 'nt':
        wipe = 'cls'
    else:
        wipe = 'clear'

   
    while(True):
        userinput = 0
        os.system(wipe)
        asciiGen()
        print('# TorGet ==> Hassel free torent getter <==')
        print('# Enter Choice ')
        print('# 1.Browse')
        print('# 2.Search')
        print('# 3.Exit')
        userinput = int(input('# Input ==> '))

        if(userinput == 1):
            url = 'https://www.1337x.to/'
            url = url + 'home/'
            HomePage(url)
            
        elif(userinput == 2):
            os.system(wipe)
            print('# Please use accurate keywords and select appropriate categories in search for correct results')
            userinput = str(input("# Enter Keyword ==> "))
            SearchPage(userinput)
        elif(userinput == 3):
            os.system(wipe)
            print('# Thank you for using ')
            break;
        
def checkconnection(url):
    try:
        requests.get(url)
        return print('# Connection Established press enter to continue')
    except requests.exceptions.ConnectionError:
        print(f"URL {url} not reachable")

def asciiGen():
    print("    .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. ")
    print("    | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
    print("    | |  _________   | || |     ____     | || |  _______     | || |    ______    | || |  _________   | || |  _________   | |")
    print("    | | |  _   _  |  | || |   .'    `.   | || | |_   __ \    | || |  .' ___  |   | || | |_   ___  |  | || | |  _   _  |  | |")
    print("    | | |_/ | | \_|  | || |  /  .--.  \  | || |   | |__) |   | || | / .'   \_|   | || |   | |_  \_|  | || | |_/ | | \_|  | |")
    print("    | |     | |      | || |  | |    | |  | || |   |  __ /    | || | | |    ____  | || |   |  _|  _   | || |     | |      | |")
    print("    | |    _| |_     | || |  \  `--'  /  | || |  _| |  \ \_  | || | \ `.___]  _| | || |  _| |___/ |  | || |    _| |_     | |")
    print("    | |   |_____|    | || |   `.____.'   | || | |____| |___| | || |  `._____.'   | || | |_________|  | || |   |_____|    | |")
    print("    | |              | || |              | || |              | || |              | || |              | || |              | |")
    print("    | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |")
    print("     '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' ")
    print("By Apoorv Bandyopadhyay")
    
def main():
    os.system(wipe)
    asciiGen()
    try:
        url = 'https://1337x.to/home/'
        checkconnection(url)
        char = input()
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        menu()
    except Exception:
        print('# Unable to connect to 1337x check your network or try again')
        char = input("Press any key to return to menu")
        menu()
    

if __name__ == '__main__':
    main()