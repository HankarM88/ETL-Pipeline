# imports
import pandas as pd 
from bs4 import BeautifulSoup
import requests

FIRST_PAGE = 1
LAST_PAGE = 36
# define a helper function to scrape British Airline Reviews 
def scrape_page(url):
    reviews = [] 
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    review_tags = soup.find_all("div",attrs={"class":"text_content"})
    for tag in review_tags:
        reviews.append(tag.text.strip())
    print ("Done")
    # save to a dataframe 
    df = pd.DataFrame({"Review": reviews})
    return df
# loop over all the pages to scrape 
for page in range(FIRST_PAGE,LAST_PAGE+1):
    print(f"SCRAPING PAGE {page} ...", end="\n")
    page_url = f"https://www.airlinequality.com/airline-reviews/british-airways/page/{page}/?sortby=post_date%3ADesc&pagesize=100" 
    df = scrape_page(page_url)
    df.to_csv("data/reviews.csv", mode='a',index=False)

