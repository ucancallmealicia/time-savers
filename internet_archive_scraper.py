#python3

import requests
import csv
import pprint
import os
import bs4

#Take from https://web.archive.org/web/*/http://www.priceofweed.com:80/* or something similar
#example: priceofweed.com:80/prices/United-States.html
#priceofweed.com:80/data/all
#priceofweed.com:80/prices/United-States/State-Name.html
invalid_input = True
def start():
     urlinput = input('Please enter URL for archived website (priceofweed.com:80/prices/United-States.html; priceofweed.com:80/prices/United-States/State-Name.html: ')

##     getURIs = requests.get("http://web.archive.org/cdx/search/cdx?url=" + urlinput)
     outfile = input('Please enter path to output file for archived URL list: C:\\Users\\amd243\\Desktop\\webscrape\\PROD\\State_Initialurllist.txt: ')
     outfolderinput = input('Please enter path to output folder for downloaded captures - i.e C:\\Users\\amd243\\Desktop\\webscrape\\PROD\\State-Name\\: ')

     ###mkdir here to create folders for each state or whatever
     outfolder = os.mkdir(outfolderinput)

     text = getURIs.text
     textlist = text.split(' ')

     #print(textlist)
##
##     ####gets timestamps - will have to change url stuff for different captures
     for i in textlist:
             if len(i) == 14:
                     with open(outfile, 'a') as f:
                             f.write('https://web.archive.org/web/'+i+'/http://www.'+ urlinput + '\n')
                     f.close()
                     
     urllist = open(outfile, 'r', encoding='utf-8')

     urllisty = urllist.read().split('\n')

     del urllisty[-1]

     print('URL list acquired...')

     for url in urllisty:
             getPages = requests.get(url)
             urlstring = str(url[28:42])
             if getPages.status_code == requests.codes.ok:
                     print('Connected! Downloading capture ' + urlstring)
                     pagetext = getPages.text
                     htmloutput = open(outfolderinput + urlstring +'.txt', 'w', encoding='utf-8')
                     htmloutput.write(pagetext)
                     htmloutput.close()
             else:
                     print('Error! Cannot retrieve page ' + urlstring + '!')
                     #add error log here

     print('Finished downloading files!' + '\n')

     moveon = input("Press Enter to continue analysis...")
     print(moveon)

     datafileinput = input("Enter path to output folder for data files i.e. C:\\Users\\amd243\\Desktop\\webscrape\\PROD\\State_Initialsdatafiles\\: ")

     datafile = os.mkdir(datafileinput)

     elements = input("Enter element pattern to search (i.e. enter tr td for priceofweed data): ")

     for filename in os.listdir(outfolderinput):
             filetoedit = open(outfolderinput + filename, encoding = 'utf-8')
             soupobject = bs4.BeautifulSoup(filetoedit, 'lxml')
             soupselect = soupobject.select(elements)
             for element in soupselect:
                      textelement = element.getText()
                      with open(datafileinput + 'datafile' + filename, 'a') as g:
                              g.write(textelement + '\n')
             g.close()
             print('Writing ' + str(filename) + ' data to file')

     print('Data files created!' + '\n')

     moveon = input("Press Enter to finish analysis...")
     print(moveon)

     directory = os.listdir(datafileinput)
     #print(directory)

     for datafiles in directory:
             data = open(datafileinput + datafiles)
             datalist = data.read().split('\n')
             #unsure if these numbers will hold across web pages...but this is the best I've got
             del datalist [0:112]
             del datalist [9:]
             y = str(datafiles)
             newitem = y[8:22]
     #        print(newitem)
             length = len(datalist)
             x = [datalist[i*length // 3: (i+1)*length // 3] for i in range(3)]
     #        print(x)
             for pricelist in x:
     #                print(pricelist)
     #                print(newitem)
                     pricelist.append(newitem)
     #                print(pricelist)
             with open(outfolderinput + 'State_Output.csv', 'a', newline='') as csvout:
                     writer = csv.writer(csvout)
                     writer.writerows(x)

     print('All Done! Check state folder for results!')
     print('\n' + '\n' + '\n' + '\n' + '\n' + '\n')
     print('Bye!' + '\n')

while invalid_input:
     start()
#str(url[28:42]

#add an if else statement so if the directory already exists no error is thrown - open the directory, unless it doesn't exist then create one
#0:109 - no idea if this will hold true across the different pages...                
