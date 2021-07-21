import urllib.request
import urllib.parse
from bs4 import BeautifulSoup


def main():
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_brd&fbm=1&ie=utf8&query='

    url2 = input('Search : ')
    url3 = url + urllib.parse.quote_plus(url2)
    html = urllib.request.urlopen(url3).read()
    verification = BeautifulSoup(html, 'html.parser')

    data = verification.find_all(class_='sh_blog_title')

    for item in data:
        print(f" Title : {item.attrs['title']} | Link : {item.attrs['href']}")


if __name__ == '__main__':
    main()
