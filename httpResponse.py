# @author: ajfernandez
# @last_edit: 1/21/19
# @simple read/store with http responses code (and watermark) in http request.
# @For this version the file must exist, to create by
# @itself see httpResponseCreateFile.py version

import requests
import csv

cnt = 1

with open('intrusions') as src:
    # line = src.readlines() # Dont handle newline chars '\n'
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
