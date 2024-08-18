# s24020
# 沖縄の推定人口ページ
# https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html

import requests
from bs4 import BeautifulSoup

# URL
url = 'https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html'

# ページのHTMLを取得
response = requests.get(url)
response.encoding = 'shift_JIS'  # 文字コードを設定

# BeautifulSoupで解析
soup = BeautifulSoup(response.text, 'lxml')

# ページタイトルを表示
title = soup.find('title').get_text()
print(title.strip())

# テーブルの抽出
table = soup.find('table')

# データを格納する辞書
data = {}

# テーブルの行を取得
rows = table.find_all('tr')

# 各行からデータを抽出
for row in rows:
    cols = row.find_all('td')
    if len(cols) == 2:
        label = cols[0].get_text(strip=True)
        value = cols[1].get_text(strip=True)
        data[label] = value

# データの表示
print("総人口:", data.get("総人口", "情報なし"))
print("男:", data.get("男", "情報なし"))
print("女:", data.get("女", "url"))

