__author__ = 'xuhuan'
import sys


# 对搜索表按关键词去重
def dedup(data, channel):
    if channel == '百度搜索':
        for ii in data:
            if '短语'in ii['推广单元'] or '词组'in ii['推广单元']:
                ii['关键词'] += 'p'
            if '广泛' in ii['推广单元']:
                ii['关键词'] += 'b'
        for i in data:
            index = data.index(i)
            for j in data[index + 1:]:
                if i['关键词'] == j['关键词']:
                    i['展现量'] += j['展现量']
                    i['点击量'] += j['点击量']
                    i['消费'] += j['消费']
                    if int(i['展现量']):
                        i['点击率'] = round(int(i['点击量']) / int(i['展现量']), 4)
                        i['点击率'] = str(i['点击率'] * 100) + '%'
                    if int(i['点击量']):
                        i['平均点击'] = round(int(i['消费']) / int(i['点击量']), 2)
                    data.remove(j)
        data.sort(key=lambda obj: obj.get('关键词'))
        return data
    elif channel == '360搜索':
        for ii in data:
            if '短语'in ii['推广组'] or '词组'in ii['推广组']:
                ii['关键词'] += 'p'
            if '广泛' in ii['推广组']:
                ii['关键词'] += 'b'
        for i in data:
            index = data.index(i)
            for j in data[index + 1:]:
                if i['关键词'] == j['关键词']:
                    i['展示次数'] += j['展示次数']
                    i['点击次数'] += j['点击次数']
                    i['总费用'] += j['总费用']
                    if int(i['展示次数']):
                        i['点击率'] = round(int(i['点击次数']) / int(i['展示次数']), 4)
                        i['点击率'] = str(i['点击率'] * 100) + '%'
                    if int(i['点击次数']):
                        i['平均每次点击费用'] = round(int(i['总费用']) / int(i['点击次数']), 2)
                    data.remove(j)
        data.sort(key=lambda obj: obj.get('关键词'))
        return data
    elif channel == '页游后台':
        for i in data:
            index = data.index(i)
            for j in data[index + 1:]:
                if i['关键词'] == j['关键词']:
                    i['弹出PV'] += j['弹出PV']
                    i['弹出IP'] += j['弹出IP']
                    i['总充值人数'] += j['总充值人数']
                    i['总充值'] += j['总充值']
                    i['新充值人数'] += j['新充值人数']
                    i['新充值'] += j['新充值']
                    if int(j['注册人数']):
                        i['注册人数'] += j['注册人数']
                        i['注册转换率'] = round(int(i['注册人数']) / int(i['弹出PV']), 4)
                        i['注册转换率'] = str(i['注册转换率'] * 100) + '%'
                    if int(j['激活人数']):
                        i['激活人数'] += j['激活人数']
                        i['激活率'] = round(int(i['激活人数']) / int(i['注册人数']), 4)
                        i['激活率'] = str(i['激活率'] * 100) + '%'
                    if int(j['有效人数']):
                        i['有效人数'] += j['有效人数']
                        i['有效率'] = round(int(i['有效人数']) / int(i['注册人数']), 4)
                        i['有效率'] = str(i['有效率'] * 100) + '%'
                    if int(j['次留人数']):
                        i['次留人数'] += j['次留人数']
                        i['次留率'] = round(int(i['次留人数']) / int(i['注册人数']), 4)
                        i['次留率'] = str(i['次留率'] * 100) + '%'
                    if int(j['二登人数']):
                        i['二登人数'] += j['二登人数']
                        i['二登率'] = round(int(i['二登人数']) / int(i['注册人数']), 4)
                        i['二登率'] = str(i['二登率'] * 100) + '%'
                    if int(j['活跃人数']):
                        i['活跃人数'] += j['活跃人数']
                        i['活跃率'] = round(int(i['活跃人数']) / int(i['注册人数']), 4)
                        i['活跃率'] = str(i['活跃率'] * 100) + '%'
                    data.remove(j)
        data.sort(key=lambda obj: obj.get('关键词'))
        return data
    elif channel == '搜狗搜索':
        pass
    else:
        return data