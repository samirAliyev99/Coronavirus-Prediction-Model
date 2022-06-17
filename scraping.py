from bs4 import BeautifulSoup
import requests
from parse import parse
import time
import pandas as pd


# fetch html code from given url
def fetch_data(url):

    response = requests.get(url)

    # print(response)
    if '200' in str(response):
        return BeautifulSoup(response.text, 'html.parser')


with open('data.csv', 'w+', encoding='utf-8') as out:
    out.write('Date,Day,Infected,Released\n')


pages = range(6, 19)
day = 78
url = 'https://koronavirusinfo.az/az/page/xeberler?category=4&page='

format1 = 'Azərbaycan Respublikasında {} yeni koronavirus infeksiyasına yoluxma faktı qeydə alınmış, ' \
         '{} nəfər müalicə olunaraq sağalmış və evə buraxılmışdır.'

format2 = 'təvəllüdlü {} nəfər vəfat etmişdir.'
format3 = 'Ötən müddət ərzində yeni yoluxma hallarının müəyyənləşdirilməsi ilə əlaqədar {} test aparılmışdır.'

df = pd.DataFrame()

for page in pages:

    # all news are in <a> tag, with classname "news_card"
    all_news = fetch_data(url + str(page)).findAll('a', {'class': 'news_card'})

    for news in all_news:
        # all statistics containing news has this header
        if news.find('p').getText() == 'Azərbaycan Respublikası Nazirlər Kabineti yanında Operativ Qərargahın məlumatı':
            date = news.find('span').getText().split(' - ')[0]
            stats_url = news['href']

            print(date, stats_url)

            data = [date, str(day)]
            day -= 1

            # get texts in this page
            text = fetch_data(stats_url).find('section', {'class': 'readmore'}).find('div').find('div').findAll('p')

            for t in text[1::2]: # skip empty lines

                line = t.getText()
                tmp = None

                if 'yeni koronavirus infeksiyasına yoluxma faktı qeydə alınmış' in line:  # 1st line
                    tmp = parse(format1, line)

                    if tmp:
                        data.extend(list(tmp))
                    else:
                        print(f'Not all data fetched from {stats_url}')
                        data.append('')

            if len(data) > 2:
                with open('data.csv', 'a+', encoding='utf-8') as out:
                    out.write(','.join(data))
                    out.write('\n')

            time.sleep(1)

    print()

