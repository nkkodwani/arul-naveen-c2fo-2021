import requests               #gets html data from a website
from bs4 import BeautifulSoup #this is how python reads and understands the html data

r = requests.get('https://mmr2410.com/robots') #requests info from 2410 server
mmr_html = r.text #stores html of the 2410 page as a string
soup = BeautifulSoup(mmr_html, 'lxml') #^

'''for team in soup.find_all('div', class_ = 'profile'):
    teammate_name = team.p.text 
    print(f"\t{teammate_name}")''' #for the team page: https://mmr2410.com/team
#print(team.prettify()) #keep this line commented out

for season in soup.find_all('div', class_='jumbotron'):
    year = season.h1.b.text #gets season year
    bot_name = season.h2.text #geats robot name from that particular season
    print(f"\t\n{year}: {bot_name}") #prints season year w/ robot name