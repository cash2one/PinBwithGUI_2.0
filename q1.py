__author__ = 'xuhuan'
import csv
games = ['三国志', '三国群英传', '三国无双', '三国无敌', '三国战记', '三国争霸', '三国风云', '三国英杰传', '三国游戏', '三国群侠传', '三国英雄', '最三国', '三国赵云传']
ios = ['ios', 'ios版', 'iphone', '苹果', 'app', 'ipad', 'ipad版']
apk = ['apk', '安卓', '安卓版', '手机游戏', '手游', '手机版']

dct = {}
for j in [ios, apk]:
    for i in games:
        lst = list(map(lambda x, y=i: y + x, j))
        dict1 = dict(zip(games[]))
print(ls1)