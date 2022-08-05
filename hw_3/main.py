from datetime import datetime
import requests
from bs4 import BeautifulSoup
import time


def get_page_with_previews(url, headers):
    page_url = url + '/ru/all/'
    response = requests.get(url=page_url, headers=headers)
    time.sleep(0.34)
    return response

def extract_previews(response):    
    soup = BeautifulSoup(response.text, features='html.parser')
    articles = soup.find_all(class_='tm-article-snippet')
    return articles

def get_post_hubs(article):
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = {hub.find('a').text.strip(' *') for hub in hubs}
    return hubs

def get_post_attrs(article, url):
    article_tag_a = article.find('h2').find('a')
    href = article_tag_a.attrs['href']
    
    article_name = article_tag_a.text
    article_url = url + href 
    article_date = article.find(class_='tm-article-snippet__datetime-published').find('time').text
    return {'post_date': article_date, 'post_name': article_name, 'post_url': article_url}

def get_post_page(article_url, headers):
    response = requests.get(article_url, headers=headers)
    time.sleep(0.34)
    return response

def get_post_body(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    article_body_ = 'article-formatted-body article-formatted-body article-formatted-body_version-2'
    article_body = soup.find(class_=article_body_)
    return article_body

def get_post_text(article_body):   
    article_text_p = article_body.find_all('p')
    article_text_h2 = article_body.find_all('h2')
    article_text = str(article_text_p).lower() + str(article_text_h2).lower()
    return article_text
               

if __name__ == "__main__":
    KEYWORDS = {'API', 'Python', 'Патентование', 'Администрирование баз данных'}
    URL = 'https://habr.com'
    HEADERS = {'User-Agent':'Chrome'}
    
    # Вывести в консоль список подходящих статей в формате: <дата> - <заголовок> - <ссылка>
    webpage = get_page_with_previews(URL, HEADERS)
    posts_previews = extract_previews(webpage)
    for post in posts_previews:
        hubs = get_post_hubs(post)
        post_attrs = get_post_attrs(post, URL)
        if hubs & KEYWORDS:
            print(f'keywords in hubs:')
            print(f'{post_attrs["post_date"]} - {post_attrs["post_name"]} - {post_attrs["post_url"]}')        
            print('------------')
        else:
            # Анализ не только preview статьи, но и всего текста статьи целиком.
            post_page = get_post_page(post_attrs["post_url"], HEADERS)
            post_body = get_post_body(post_page)
            if post_body is not None:
                post_text = get_post_text(post_body)
                for keyword in KEYWORDS:
                    if keyword.lower() in post_text:
                        print(f'keyword {keyword} in text:')
                        print(f'{post_attrs["post_date"]} - {post_attrs["post_name"]} - {post_attrs["post_url"]}')
                        print('------------')
                        break
                    else: continue