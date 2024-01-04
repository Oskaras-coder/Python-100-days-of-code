from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)
article_tag = soup.find(name="a", rel="noreferrer")
article_text = article_tag.getText()

article_link = article_tag.get("href")
article_upvote = soup.find(name="span", id="score_38543229")
print(article_link)
print(int(article_upvote.getText().split()[0]))