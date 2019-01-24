# @author: ajfernandez
# @last_edit: 1/21/19
# @simple read/store with http responses code (and watermark) in http requests.

import requests
import csv

sites = ['http://www.youtube.com',
'https://www.ajfernandez.me',
'http://www.google.com',
'http://www.lavanguardia.com',
'http://www.boe.es',
'https://httpstat.us/306',
'https://httpstat.us/413',
'https://httpstat.us/302',
'https://httpstat.us/400',
'https://httpstat.us/500',
]
cnt = 1

with open('intrusions', 'w') as dst:
    dst.write('\n'.join(sites))

with open('intrusions', 'r') as src:
    line = [line.rstrip('\n') for line in open('intrusions')]

report = csv.writer(open("report.csv", 'w'))

for url in line:
    answer = requests.get(url)
    if answer.status_code != 200:
        report.writerow(['[-]',cnt,url,answer.status_code])
        cnt += 1
    else:
        report.writerow(['[+]',cnt,url,answer.status_code])
        cnt += 1
