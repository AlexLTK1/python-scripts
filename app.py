import requests
from bs4 import BeautifulSoup

# Send an HTTP request to the webpage and store the response
url = 'https://forum.gamer.com.tw/B.php?bsn=29919'
page = requests.get(url)

# Parse the HTML of the webpage
soup = BeautifulSoup(page.text, 'html.parser')

# Find all the div elements with the class 'single-post'
posts = soup.find_all('div', {'class': 'single-post'})

# Iterate through the list of posts and extract the username and content of each post
for post in posts:
  username = post.find('div', {'class': 'username'}).text
  content = post.find('div', {'class': 'content'}).text
  print(f'Username: {username}\nContent: {content}\n---')
