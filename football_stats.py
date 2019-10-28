#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211_Assignment9 - Part I"""

import re

from bs4 import BeautifulSoup
import requests


def edit_output_string(cur_str, indicator):
    result = ""
    if indicator == 0:
        for i in range(0, 30):
            if len(cur_str) > i:
                result += cur_str[i]
            else:
                result += " "
    else:
        for i in range(0, 10):
            if len(cur_str) > i:
                result += cur_str[i]
            else:
                result += " "

    return result


def main():
    source = requests.get(
        'https://www.cbssports.com/nfl/stats/playersort/nfl/year-2019-season-regular-category-touchdowns').text
    soup = BeautifulSoup(source, 'lxml')

    tables_rows = soup.findAll("tr", class_=re.compile("^row"))

    players_number = 20

    print("the list of top 20 players")

    print("       Name                ", end='')
    print("Position     ", end='')
    print("Team  ", end='')
    print("Total Touch Down")

    for row in tables_rows:
        if players_number <= 0:
            break
        row_info = row.findAll('td')
        idx = 0
        for info in row_info:
            if idx in [0, 1, 2, 5]:
                print(edit_output_string(info.text, idx), end='')
            idx += 1
        players_number -= 1
        print('')


main()
