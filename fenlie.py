__author__ = 'xuhuan'
import csv
import re
'''
with open('qwe123.csv', 'r') as f:
    reader = csv.DictReader(f)
    dicts = [d for d in reader]
'''
ll = 'http://weather.news.qq.com/index.shtml?icity=01012'
reg = re.compile('(?<=http").*?(?=com")')
dom = reg.findall(ll)
print(dom)
'''
for i in dicts:
    url = i['plkw']
    domain = reg.findall(url)
'''