import requests
import csv
from bs4 import BeautifulSoup


class Reuters:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko'
                              ') Chrome/61.0.3163.100 Safari/537.36'
            }
        )
        self.channel = ['businessNews', 'marketsNews', 'fundsFundsNews', 'financialsSector']

    def getNewList(self, date):
        url = 'https://www.reuters.com/resources/archive/us/%s.html' % str(date)
        page = requests.get(url).content.decode()
        soup = BeautifulSoup(page, 'html5lib')
        news_list = soup.find_all('div', {'class': 'headlineMed'})
        result = ''
        for news in news_list:
            url = news.a.get('href')
            print(url)
            title = news.a.text
            print(title)
            if 'article' in url:
                content = self.getNewsContent(url)
                if not content:
                    continue
            else:
                print('This is a video, continue')
                continue
#            print(url, title)
            result += content
        with open('Reuters.csv', 'a', encoding='utf-8', newline='') as f:
            csvwriter = csv.writer(f, dialect=("excel"))
            csvwriter.writerow([date, result])

    def getNewsContent(self, url):
        try:
            page = requests.get(url).content.decode()
            soup = BeautifulSoup(page, 'html5lib')
            channel = soup.find('meta', {'name': 'DCSext.ContentChannel'}).get('content')
            if channel not in self.channel:
                print('Not in channel, continue')
                return 0
# find the whole text content
#            content = ''
#            for p in soup.find('div', {'class': 'body_1gnLA'}).find_all('p'):
#                content += p.text
#            print(content[:100] + '...')
#            return content
# find the description of the content
            description = soup.find('meta',{'name':'description'}).get('content')
            print(description)
            return description
        except Exception as e:
            print(e)
            return 0

    def run(self):
        with open('Reuters.csv', 'a', encoding='utf-8', newline='') as f:
            csvwriter = csv.writer(f, dialect=("excel"))
            csvwriter.writerow(['date', 'content'])
        for year in range(2017, 2019):
            for month in range(1, 13):
                for day in range(1, 32):
                    datetime = '%d%02d%02d' % (year, month, day)
                    self.getNewList(datetime)


Reuters().run()
