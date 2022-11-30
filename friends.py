import random
import requests
from bs4 import BeautifulSoup

def friends_quote():
    URL = "https://www.washingtonpost.com/arts-entertainment/2019/09/22/friends-premiered-years-ago-here-are-beloved-sitcoms-most-memorable-quotes/"
    page = requests.get(URL)

    quotes = []

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div",id="__next")
    article_body = results.find_all("div", class_="article-body")
    for each in article_body:
        header = each.find("h3")
        if header:
            quote_val = header.find("div")
            quotes.append(quote_val.text.strip()[3:])
    
    # print(quotes, end="\n"*2)
    return random.choice(quotes)


# print(friends_quote())