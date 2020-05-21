from bs4 import BeautifulSoup
import requests
import csv
#import pandas as pd
#df = pd.DataFrame(records, columns=['year', 'month', 'day', 'state', 'river', 'fly_name', 'fly_size', 'tippet', 'fly_color', 'conditions', 'new_report']) // save for possible use with pandas later
fields = ['year', 'month', 'day', 'state', 'river', 'fly_name', 'fly_size', 'tippet', 'fly_color', 'conditions', 'new_report']  
i = 0
while i < 999:
  i += 1
  print(i)
  r = requests.get('https://www.orvis.com/fishing_report.aspx?locationid=5{i}')
  #need to set condition here if 404 returned 
    soup = BeautifulSoup(r.text, 'html.parser')
    flyTable = soup.find('table', attrs={'id':'flypatterns'})
    records = []
    flyTable.find_all('td')
    tippet = soup.find('div', attrs={'id' : "dvRecommendedTippetWithLink"})
    tippet = tippet.text
    tippet = tippet.split(':', 1)[1]
    records.append(tippet)
    #year =
    #month =
    #day =
    state = soup.find('div', attrs={'id' : "headingtext"})
    state = state.text
    state = state.split(',')[1]
    state = state.split('Fly')[0]
    records.append(state)
    river =  soup.find('div', attrs={'id' : "headingtext"})
    river = river.text
    river = river.strip().rstrip().lstrip()
    river = river.split(',')[0]
    records.append(river)
    #conditions = // unsure what this is
    #new_report = // date of most recent report? 
    flyTable = flyTable.text
    flyTable = flyTable.split('\n')
    while("" in flyTable) :
      flyTable.remove("")
    for fly in flyTable:
      try:
        fly = fly.strip().rstrip().lstrip()
        records.append(fly)
      except:
        pass 
      
      
    csv_file = open('scrape.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([records])
    csv_file.close()