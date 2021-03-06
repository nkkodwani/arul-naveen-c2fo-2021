import requests               #gets html data from a website
from bs4 import BeautifulSoup #this is how python reads and understands the html data
import pandas as pd
import numpy as np

r = requests.get('https://mmr2410.com/robots') #requests info from 2410 server
mmr_html = r.text #stores html of the 2410 page as a string
soup = BeautifulSoup(mmr_html, 'lxml') #^
robot_year = []
robot_name = []
competitions = []

'''for team in soup.find_all('div', class_ = 'profile'):
    teammate_name = team.p.text 
    print(f"\t{teammate_name}")''' #for the team page: https://mmr2410.com/team
#print(team.prettify()) #keep this line commented out

print()
status = True
while(status == True):
    for season in soup.find_all('div', class_='jumbotron'):
        year = season.h1.b.text #gets season year
        name = season.h2.text #geats robot name from that particular season
        robot_year.append(year)
        robot_name.append(name)
        if year == '2008':
            status = False
            break 
    #print(f"\t{year}: {name}\n") #prints season year w/ robot name

#pandas data testing
data = { 'Robot Year' : robot_year,
        'Robot Name' : robot_name
}

df = pd.DataFrame(data, columns = ['Robot Year', 'Robot Name'])
df.set_index('Robot Year', inplace=True) #sets the index of the DF to be the season year
#print(f"{df}\n")
n=int(input("What year would you like to get the robot name? "))
print(df.loc[[f'{n}'], ['Robot Name']]) #prints the name of a robot for a specific year (2020)


