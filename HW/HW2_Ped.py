#title 
#publish date
#issues
#signatures

from bs4 import BeautifulSoup
import urllib.request
import re
import os
import csv
import unicodedata

os.chdir('C:/Users/jenna/Documents/GitHub/python_summer2020/HW')

with open('HW2_Ped.csv', 'w') as f:
    # Define our csv file
    w = csv.DictWriter(f, fieldnames = ("Petition Title", "Published Date", "Tagged Issues", "Signatures"))
    # Create the header for our csv
    w.writeheader()
    # First make an empty list to enter in the individual petition pages
    petition_pages = []
    
    
    # Now use a for loop to insert the petition urls into our list
    for i in range(1, 3):
        # This line allows me to collect data from page=1 and page=2 using + str(i)
        web_address='https://petitions.whitehouse.gov/?page=' + str(i)
        # Utilize urllib to name our web_address
        web_page = urllib.request.urlopen(web_address)
        # This "breaks apart" the contents of the webpage
        soup = BeautifulSoup(web_page.read())
        
        # Now we need to get the individual links of the petitions
        petition_url = soup.find_all('h3')
        # First 3 entries of tag 'h3' don't direct to petitions
        # Subset petition_url to the 3rd through the end of petition url
        petition_url = petition_url[3::]
        # Add petition_link + petition_pages to fill the empty list
        petition_pages = petition_pages + petition_url
        #print(petition_pages) Can run to determine if correct information found.
    # Now use a for loop to run through each petition page to gather relavent info
    for i in petition_pages[0::]:
        petition = {}
        # 'text' gives us the title because text is now an attribute of petition
        petition['Petition Title'] = i.text 
        #extension = i.attrs['href']
        extension = str(i.find('a')['href'])
        # Now we "create" each petition's individual URL to more easily extract data
        try:
            #petition_home = 'https://petitions.whitehouse.gov' + i.find('a')['href']
            petition_home = urllib.request.urlopen('https://petitions.whitehouse.gov%s' % extension)
            soup2 = BeautifulSoup(petition_home.read())
        except urllib.error.URLError:
              #petition['publish date'] = 'NA'
              #petition['issues'] = 'NA'
              #petition['signatures'] = 'NA'
              #w.writerow(petition)
              continue
        #Extract the Published date
        try:
            petition_publish = soup2.find('h4', {'class': 'petition-attribution'})
            petition["Published Date"] = petition_publish.get_text()
        except AttributeError:
            petition["Published Date"] = "NA"

        #Extract the Issues
        try:
            petition_issues = soup2.find('div', {'class': 'content'}).find_all('h6')
            #petition_issues[i].replace('<h6>', '')
            #petition_issues[i].replace('</h6>', '')
            #petition_issues[i].replace('&amp;', '&')
            petition["Tagged Issues"] =  petition_issues
        except AttributeError:
            petition["Tagged Issues"] = "NA"

        #Extract the Signatures
        try:
            petition_sigs = soup2.find('span', {'class': 'signatures-number'})
            petition["Signatures"] = petition_sigs.get_text()
        except AttributeError:
            petition["Signatures"] = "NA"
        print(petition)
        w.writerow(petition)      