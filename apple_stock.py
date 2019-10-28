#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211_Assignment9 - Part II"""

import re

import requests
from bs4 import BeautifulSoup
import urllib.request


def main():
    url = ' https://www.nasdaq.com/symbol/aapl/historical'
    web = urllib.request.urlopen(url)
    soup = BeautifulSoup(web.read(), 'lxml')

    table = soup.find("tbody", class_='historical-data__table-body')

    tables_rows = table.findAll('tr')
    print("Date\t Close Price:")

    print(tables_rows)
    for row in tables_rows:
        date = row.find('th').text

        close_price = row.find('td').text
        print(date, "\t", close_price)


main()
