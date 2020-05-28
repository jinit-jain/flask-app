# money control news article's scrapper
import requests 
from bs4 import BeautifulSoup

def extract_article (url):
    # request for article web page
    try:
        req = requests.get(url) 
    except Exception:
        'bhai request bhi nahi kiya'

    # extract html data using the 'lxml' parser  
    try:
        soup = BeautifulSoup(req.content, 'lxml')
    except Exception:
        return 'soup bohot chutiya hai'

    # extract news article
    news_article = ''

    try:
        paras = soup.find_all('p')
    except Exception:
        return 'jinit ki maa ka bhosda'

    try:
        for para in paras:
            news_article = news_article + para.text
    except Exception:
        return 'Jinit ki maa ki ...'

    print(news_article)
    return news_article

if __name__ == "__main__":
    doc = extract_article("https://www.moneycontrol.com/news/business/markets/reliance-industries-rights-entitlement-jumps-to-rs-209-90-up-16-intraday-5321661.html")