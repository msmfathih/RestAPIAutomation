import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://www.bbc.com/news'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all elements with the specified class for top stories
top_stories = soup.find_all(class_='gs-c-promo-heading')

# Extract and print titles and links of the top stories
for story in top_stories:
    title = story.find('a').text.strip()
    link = 'https://www.bbc.com' + story.find('a')['href']
    print("Title:", title)
    print("Link:", link)
    print()
