#!/usr/bin/env python
# coding: UTF-8
import configparser
import urllib2
from bs4 import BeautifulSoup
# import csv
import unicodecsv as csv

# configparserの宣言とiniファイルの読み込み
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

# アクセスするURL
url = config_ini['DEFAULT']['url']

# URLにアクセスする
html = urllib2.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

# イベントのdivを全取得
# textは全てunicode文字列でくる。u"" を忘れるな
events = soup.find_all(class_="eventOnce",)
import codecs
f = codecs.open('result.csv', 'w', 'shift_jis')
head = u'タイトル,リンク,開催日' + u"\n";
f.write(head)
for event in events:
    # タイトル取得
    event_title = event.find('h1')
    if event_title is None:
        # タイトル要素がない場合は対象外。skip
        continue
    title = event_title.text
    # print title
    
    # リンク取得
    a = event.find('a')
    if a is None:
        # リンクがない場合は対象外。skip
        continue
    link = a.attrs['href']
    # print link

    # 開催日取得
    day = event.find(class_="day")
    if day is None:
        # 開催日要素がない場合は対象外。skip
        continue
    open_day = day.text.replace(u'開催日：', u'')
    # print open_day

    # CSVにイベント情報を書き込む
    # ignoreをすることで機種依存文字列を無視してエンコード(unicode -> str)。さらにdecodeしてunicodeに直す
    record = title + u',' + link + u',' + open_day + u"\n"
    record = record.encode('shift_jis','ignore').decode('shift_jis')
    # print record
    f.write(record)
f.close()


