

# url of website used for text - transcript taking 'https://transcripts.foreverdreaming.org/viewforum.php?f=574&sid=94b0037dd75d5d5e63fa017926b95996&start=156'
# Format of files is as follows:
    # SeasonYYxEpisodeYY - TitleYY

#/*how to get the names of cast from imdb url = https://www.imdb.com/title/tt0386676/fullcredits/?ref_=tt_cl_sm with beatuful soup */


# importing the modules 
from imdb import Cinemagoer # API for series info 
import pandas as pd # for dataframes and saving to csv

# create an instance of the Cinemagoer class
ia = Cinemagoer()
# id 
code = "0386676"
# getting information 
series = ia.get_movie(code) 
# getting cast of the series 
cast = series.data['cast'] 
# printing the object i.e name 
print(series) 
# print the cast person at index 0 
print(cast[0])
df_cast = pd.DataFrame(data=cast)

# df_cast.to_csv(r'C:/Users/test/Documents/Github/repos/social_graphs_project/df_cast.csv')

import requests
from bs4 import BeautifulSoup

# URL of the IMDb page
url = "https://www.imdb.com/title/tt0386676/fullcredits/?ref_=tt_cl_sm"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the section of the page that contains the cast information
    cast_section = soup.find('table', class_='cast_list')

    # Extract the cast members
    cast_members = []
    for row in cast_section.find_all('tr')[1:]:
        columns = row.find_all(['td', 'th'])
        if columns:
            actor_name = columns[1].get_text(strip=True)
            cast_members.append(actor_name)

    # Print the cast members
    print("Series Cast:")
    for i, actor in enumerate(cast_members, start=1):
        print(f"{i}. {actor}")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
