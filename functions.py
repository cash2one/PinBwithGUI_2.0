__author__ = 'xuhuan'

'''
data1 为各个广告渠道数据，data2 为 adm 表数据；
对于搜索表格数据，默认关键词已去重；
'''


def pinbiao_bdss(data1, data2, info):
    pass


def pinbiao_bdwm(data1, data2, info):
    data1.sort(key=lambda obj: obj.get('网站'))
    data2.sort(key=lambda obj: obj.get('plkw'))  # reverse=True
    if 'prefix' in info.keys():
        prefix = info['prefix'] + '-'
    adm_rest_keys = ['注册人数', '有效人数', '次留人数', '二登人数', '活跃人数', '新充值人数', '新充值', '有效率', '次留率', '二登率', '活跃率']
    adm_del_keys = ['spreader_id', '广告商', 'plkw', 'keyword', '总充值人数', '总充值']
    new_keys = ['注册成本', '次留成本']
    # channel_list = []
    for i in data1:
        new_dict = dict.fromkeys(adm_rest_keys + new_keys, 0)
        i.update(new_dict)
        for j in data2:
            if i['网站'] + prefix + '-' + i['推广组'] == j['plkw'] + j['广告商']:
                if int(j['注册人数']):
                    i.update({'注册成本': round(float(i['总费用(元)']) / int(j['注册人数']), 2)})
                if int(j['次留人数']):
                    i.update({'次留成本': round(float(i['总费用(元)']) / int(j['次留人数']), 2)})
                for del_key in adm_del_keys:
                    del j[del_key]
                i.update(j)
                data2.remove(j)
                break
    return data1, info


def pinbiao_360ss(data1, data2, info):
    # k = 0
    # data1.sort(key=lambda obj: obj.get('关键词'))
    # data2.sort(key=lambda obj: obj.get('关键词'))
    adm_rest_keys = ['弹出PV', '弹出IP', '注册人数', '激活人数', '有效人数', '次留人数', '二登人数', '活跃人数', '新充值人数', '新充值',
                     '注册转换率', '激活率', '有效率', '次留率', '二登率', '活跃率']
    adm_del_keys = ['keyword_id', '关键词', '开始时间', '结束时间', '游戏', '总充值', '总充值人数']
    new_keys = ['注册成本', '次留成本']
    for i in data1:
        # k += 1
        new_dict = dict.fromkeys(adm_rest_keys + new_keys, 0)
        i.update(new_dict)
        for j in data2:
            if i['关键词'] == j['关键词']:
                if int(j['注册人数']):
                    i.update({'注册成本': round(float(i['总费用']) / int(j['注册人数']), 2)})
                if int(j['次留人数']):
                    i.update({'次留成本': round(float(i['总费用']) / int(j['次留人数']), 2)})
                for del_key in adm_del_keys:
                    del j[del_key]
                i.update(j)
                data2.remove(j)
                break
                # if not k % 500:
                # print(k, len(i))
    return data1, info


def pinbiao_sgss(data1, data2, info):
    adm_rest_keys = ['弹出PV', '弹出IP', '注册人数', '激活人数', '有效人数', '次留人数', '二登人数', '活跃人数', '新充值人数', '新充值', '注册转换率', '激活率', '有效率', '次留率', '二登率', '活跃率']
    adm_del_keys = ['keyword_id', '关键词', '开始时间', '结束时间', '游戏', '总充值', '总充值人数']
    new_keys = ['注册成本', '次留成本']
    for i in data1:
        # k += 1
        new_dict = dict.fromkeys(adm_rest_keys + new_keys, 0)
        i.update(new_dict)
        for j in data2:
            if i['关键词'] == j['关键词']:
                if int(j['注册人数']):
                    i.update({'注册成本': round(float(i['总费用']) / int(j['注册人数']), 2)})
                if int(j['次留人数']):
                    i.update({'次留成本': round(float(i['总费用']) / int(j['次留人数']), 2)})
                for del_key in adm_del_keys:
                    del j[del_key]
                i.update(j)
                data2.remove(j)
                break
                # if not k % 500:
                # print(k, len(i))
    return data1, info