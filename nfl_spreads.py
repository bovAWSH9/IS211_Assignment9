#!/usr/bin/python
# -*- coding: utf-8 -*-
"""IS211_Assignment9 - Part 2.1"""

import requests
from bs4 import BeautifulSoup


def main():
    source = requests.get(
        'http://www.footballlocks.com/nfl_point_spreads.shtml').text
    soup = BeautifulSoup(source, features="html.parser")
    tables_rows = soup.find("table", {"width": "580"})

    tds = tables_rows.findAll('td')

    cur_line = ""
    i = 0
    for td in tds:
        if i < 4:
            cur_line += td.text.strip() + "#"
        else:
            cur_line = cur_line.split("#")
            print("%-15s %18s %10s %+30s" % (cur_line[0], cur_line[1], cur_line[2], cur_line[3]))
            cur_line = ""
            cur_line += td.text.strip() + "#"
            i = 0
        i += 1


main()
