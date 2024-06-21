import requests
from bs4 import BeautifulSoup
import random

resp = requests.get(
	url="https://en.wikipedia.org/wiki/Batman",
)

soup = BeautifulSoup(resp.content, 'html.parser')

# Extracting the title from the HTML
title = soup.find(id="firstHeading")
print(title.string)

# Get all the links from <a> tags
allLinks = soup.find(id="bodyContent").find_all("a")
random.shuffle(allLinks)