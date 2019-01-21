# @author: ajfernandez
# @last_edit: 1/21/19
# @simple read/store with http responses code (and watermark) in http request.

import requests
import csv

cnt = 1

with open('intrusions') as src:
    # line = src.readlines() # Dont handle newline chars '\n'
    line = [line.rstrip('\n') for line in open('intrusions')]

writer = csv.writer(open("reporte.csv", 'w'))

for url in line:
    answer = requests.get(url)
    if answer.status_code != 200:
        writer.writerow(['[-]',cnt,url,answer.status_code])
        cnt += 1
    else:
        writer.writerow(['[+]',cnt,url,answer.status_code])
        cnt += 1
