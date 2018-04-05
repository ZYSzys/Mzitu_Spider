#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

import requests
from bs4 import BeautifulSoup
import os

class Mz:
    def __init__(self):
        self.url = 'http://www.mzitu.com'
        self.headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36', 
        'Referer': 'http://www.mzitu.com/'
        }
        self.req = requests.session()
        self.all_a = []
        self.all_a_title = []
        self.all_a_max = []
        os.makedirs(os.path.join(os.getcwd(), 'Mzitu'))
        os.chdir(os.path.join(os.getcwd(), 'Mzitu'))
        self.initpwd = os.getcwd()

    def Domainhtml(self):
        html = self.req.get(self.url, headers=self.headers)
        lis = BeautifulSoup(html.text, 'lxml').find('div', class_='postlist').find_all('li')
        for a in lis:
            imgurl = a.find('a')['href']
            self.all_a.append(imgurl)

    def Getmaxpage(self):
        for a in self.all_a:
            imghtml = self.req.get(a, headers=self.headers)
            title = BeautifulSoup(imghtml.text, 'lxml').find('h2', class_='main-title').string
            #print title
            last = BeautifulSoup(imghtml.text, 'lxml').find('div', class_='pagenavi').find_all('span')
            last = int(last[-2].string)
            self.all_a_title.append(title)
            self.all_a_max.append(last)

    def Downloadimg(self):
        cnt = 0
        print('total: %s' % len(self.all_a))
        for a in self.all_a:
            print('Downloading %s now...' % (cnt+1))
            os.makedirs(os.path.join(os.getcwd(), self.all_a_title[cnt]))
            os.chdir(os.path.join(os.getcwd(), self.all_a_title[cnt]))
            for i in range(1, self.all_a_max[cnt]+1):
                nurl = a+'/'+str(i)
                imghtml = self.req.get(nurl, headers=self.headers)
                aaa = BeautifulSoup(imghtml.text, 'lxml').find('div', class_='main-image').find('img')['src']
                img = self.req.get(aaa, headers=self.headers)
                f = open(str(i)+'.jpg', 'ab')
                f.write(img.content)
                f.close()
            cnt += 1
            os.chdir(self.initpwd)

        print('Dowmload completed!')

if __name__ == '__main__':
    test = Mz()
    test.Domainhtml()
    test.Getmaxpage()
    test.Downloadimg()