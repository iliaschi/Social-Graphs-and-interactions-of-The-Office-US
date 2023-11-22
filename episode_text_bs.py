import requests
import os
from bs4 import BeautifulSoup

# Function to sanitize episode titles for use as filenames
def sanitize_filename(title):
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*', '&']
    for char in invalid_chars:
        title = title.replace(char, '_')
    return title

# Create a new directory for the episode transcripts
folder_name = 'episode_transcripts'
os.makedirs(folder_name, exist_ok=True)

# The main URL of the page with links to transcripts
main_url = 'https://transcripts.foreverdreaming.org/viewforum.php?f=574'

# Send a GET request to the main page
main_response = requests.get(main_url)

# Check if the main page request was successful
if main_response.status_code == 200:
    # Parse the HTML content of the main page
    main_soup = BeautifulSoup(main_response.content, 'html.parser')
    
    # Find the elements containing links to the transcripts
    links = main_soup.find_all('a', class_='topictitle')

    # Loop through all found links and fetch each transcript
    for index, link in enumerate(links):
        episode_title_raw = link.get_text(strip=True)
        episode_title = sanitize_filename(episode_title_raw)
        episode_url = 'https://transcripts.foreverdreaming.org' + link['href']
        episode_response = requests.get(episode_url)
        
        if episode_response.status_code == 200:
            episode_soup = BeautifulSoup(episode_response.content, 'html.parser')
            transcript_elements = episode_soup.find_all('div', class_='postbody')
            
            if transcript_elements:
                # Skip the first transcript element if it's the announcements
                start_index = 1 if index == 0 else 0
                for element in transcript_elements[start_index:]:
                    transcript_text = element.get_text(strip=True)
                    filename = os.path.join(folder_name, f'{episode_title}.txt')
                    
                    # Write the transcript text to a .txt file
                    with open(filename, 'w', encoding='utf-8') as file:
                        file.write(transcript_text)
                        print(f"Saved transcript to {filename}")
            else:
                print(f"No transcript elements found for {episode_title}")
        else:
            print(f"Failed to retrieve transcript page for {episode_title}")
else:
    print("Failed to retrieve the main page")

## For ULR 2

# Function to sanitize episode titles for use as filenames
def sanitize_filename(title):
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*', '&']
    for char in invalid_chars:
        title = title.replace(char, '_')
    return title

# Create a new directory for the episode transcripts with a different name
folder_name = 'episode_transcripts_pt2'
os.makedirs(folder_name, exist_ok=True)

# The main URL of the page with links to transcripts
main_url = 'https://transcripts.foreverdreaming.org/viewforum.php?f=574&start=78'

# Send a GET request to the main page
main_response = requests.get(main_url)

# Check if the main page request was successful
if main_response.status_code == 200:
    # Parse the HTML content of the main page
    main_soup = BeautifulSoup(main_response.content, 'html.parser')
    
    # Find the elements containing links to the transcripts
    links = main_soup.find_all('a', class_='topictitle')

    # Loop through all found links and fetch each transcript
    for link in links:
        episode_title_raw = link.get_text(strip=True)
        episode_title = sanitize_filename(episode_title_raw)
        episode_url = 'https://transcripts.foreverdreaming.org' + link['href']
        episode_response = requests.get(episode_url)
        
        if episode_response.status_code == 200:
            episode_soup = BeautifulSoup(episode_response.content, 'html.parser')
            transcript_elements = episode_soup.find_all('div', class_='postbody')
            
            for element in transcript_elements:
                transcript_text = element.get_text(strip=True)
                filename = os.path.join(folder_name, f'{episode_title}.txt')
                
                # Write the transcript text to a .txt file
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(transcript_text)
                    print(f"Saved transcript to {filename}")
        else:
            print(f"Failed to retrieve transcript page for {episode_title}")
else:
    print("Failed to retrieve the main page")

# For URL 3
# Function to sanitize episode titles for use as filenames
def sanitize_filename(title):
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*', '&']
    for char in invalid_chars:
        title = title.replace(char, '_')
    return title

# Create a new directory for the episode transcripts with a unique name
folder_name = 'episode_transcripts_pt3'
os.makedirs(folder_name, exist_ok=True)

# The main URL of the page with links to transcripts
main_url = 'https://transcripts.foreverdreaming.org/viewforum.php?f=574&start=156'

# Send a GET request to the main page
main_response = requests.get(main_url)

# Check if the main page request was successful
if main_response.status_code == 200:
    # Parse the HTML content of the main page
    main_soup = BeautifulSoup(main_response.content, 'html.parser')
    
    # Find the elements containing links to the transcripts
    links = main_soup.find_all('a', class_='topictitle')

    # Loop through all found links and fetch each transcript
    for link in links:
        episode_title_raw = link.get_text(strip=True)
        episode_title = sanitize_filename(episode_title_raw)
        episode_url = 'https://transcripts.foreverdreaming.org' + link['href']
        episode_response = requests.get(episode_url)
        
        if episode_response.status_code == 200:
            episode_soup = BeautifulSoup(episode_response.content, 'html.parser')
            transcript_elements = episode_soup.find_all('div', class_='postbody')
           for element in transcript_elements:
                transcript_text = element.get_text(strip=True)
                filename = os.path.join(folder_name, f'{episode_title}.txt')
                
                # Write the transcript text to a .txt file
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(transcript_text)
                    print(f"Saved transcript to {filename}")
        else:
            print(f"Failed to retrieve transcript page for {episode_title}")
else:
    print("Failed to retrieve the main page")