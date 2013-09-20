#!/usr/bin/env python
# # -*- coding: utf8 -*-

import webbrowser
import os.path
from bs4 import BeautifulSoup
import json

FILE = 'ril_export.html'

def main():
    soup = BeautifulSoup(open(FILE))
    links = soup.find_all('a')
    entries = [{
        'url' : link['href'],
        'title': link.string,
        'added' : int(link['time_added']),
        'tags' : [t for t in link['tags'].split(',') if t]
        } for link in links]

#    programming = [entry for entry in entries if 'github' in entry['url'] or 'sourceforge' in entry['url']]
#    for p in programming:
#        print p

#    print len(programming), len(entries)
#    print info[:10]
#            <li><a href="https://github.com/jasonmoo/t.js/blob/master/t.js" time_added="1346212802" tags="javascript">t.js/t.js at master · jasonmoo/t.js · GitHub</a></li>

    print json.dumps(entries, indent=2)

if __name__=='__main__':
    if os.path.isfile(FILE):
        main()
    else:
        print 'download the export file as ril_export.html and place in this folder'
        webbrowser.open('https://getpocket.com/export')
