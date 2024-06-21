import requests
from bs4 import BeautifulSoup
import random

#Recursive function that scrapes an article from the given URL/current article
#url - access to the wiki article
def scrapeArticle(url): 
    resp = requests.get(
        url=url,
    )

    soup = BeautifulSoup(resp.content, 'html.parser')

    # Extracting the title from the HTML
    title = soup.find(id="firstHeading")

    # Get all the links from <a> tags
    allLinks = soup.find(id="bodyContent").find_all("a")
    random.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks:
        #To find links to other wiki articles
        if link['href'].find("/wiki/") == -1:
            continue

        # Gets random wiki link to a different article from within the original article
        linkToScrape = link
        break

    #Calls the method on the selected article
    scrapeArticle("https://en.wikipedia.org" + linkToScrape['href'])

