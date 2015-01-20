__author__ = 'xuhuan'
import csvfile
import sys
import csv
import os
import functions
import dedup


ads_channels = ['百度搜索', '百度网盟', '360搜索', '搜狗搜索']
keys_bdss = []
keys_bdwm = ['网站', '推广计划', '推广组', '推广组状态', '所属一级行业', '所属二级行业', '出价(元)',
             '展现次数', '展现独立访客', '展现频次', '点击次数', '点击独立访客', '点击率',
             '独立访客点击率', '平均点击价格(元)', '平均独立访客点击价格(元)', '千次展现成本(元)',
             '总费用(元)', '到达率', '二跳率', '停留时间', '直接转化', '间接转化']
keys_360ss = ['推广账户', '推广计划', '推广组', '关键词', '平均排名', '展示次数', '点击次数', '点击率', '总费用', '平均每次点击费用']
keys_sgss = []
keys_adm_wm = ['spreader_id', '广告商', 'plkw', 'keyword', '注册人数', '有效人数', '次留人数',
               '二登人数', '活跃人数', '总充值人数', '总充值', '新充值人数', '新充值',
               '有效率', '次留率', '二登率', '活跃率']
keys_adm_ss = ['keyword_id', '关键词', '开始时间', '结束时间', '游戏', '弹出PV', '弹出IP',
               '注册人数', '激活人数', '有效人数', '次留人数', '二登人数', '活跃人数',
               '总充值人数', '总充值', '新充值人数', '新充值', '注册转换率', '激活率',
               '有效率', '次留率', '二登率', '活跃率']
# 输出顺序
keys_order_360ss = ['推广账户', '推广计划', '推广组', '关键词', '总费用', '注册人数', '注册成本',
                    '次留人数', '次留成本', '次留率', '平均排名', '展示次数', '点击次数', '点击率',
                    '平均每次点击费用', '弹出PV', '弹出IP', '激活人数', '有效人数', '二登人数',
                    '活跃人数', '新充值人数', '新充值', '注册转换率', '激活率', '有效率',
                    '二登率', '活跃率']

keys_order_bdwm = ['网站', '推广计划', '推广组', '推广组状态', '总费用(元)', '注册人数',
                   '注册成本', '次留人数', '次留成本', '所属一级行业', '所属二级行业',
                   '出价(元)', '展现次数', '展现独立访客', '展现频次', '点击次数',
                   '点击独立访客', '点击率', '有效人数', '二登人数', '活跃人数',
                   '新充值人数', '新充值', '有效率', '次留率',
                   '二登率', '活跃率', '独立访客点击率', '平均点击价格(元)',
                   '平均独立访客点击价格(元)', '千次展现成本(元)', '到达率', '二跳率',
                   '停留时间', '直接转化', '间接转化']
keys_order_bdss = []
keys_order_sgss = []
keys_order = {'百度搜索': keys_order_bdss, '百度网盟': keys_order_bdwm, '360搜索': keys_order_360ss, '搜狗搜索': keys_order_sgss}
account_2_game_360 = {'游族大皇帝': '大皇帝'}
keys_channels = {'百度搜索': keys_bdss, '百度网盟': keys_bdwm, '360搜索': keys_360ss, '搜狗搜索': keys_sgss}
bd_account_prefix = {'Baidu-大皇帝1-8141563': ['百度网盟-大皇帝', '大皇帝']}

def getdata(file):
    file = csvfile.CsvFile(file)
    if 'file_from' in file.info:
        file.get_data()
    else:
        print('--表格内容错误--')
        sys.exit()
    if file.info['file_from'] == '360搜索':
        var = file.data[0]['推广账户']
        file.info['game'] = account_2_game_360[var]
    elif file.info['file_from'] == '百度搜索':
        var = file.data[0]['账户']
        file.info['game'] = bd_account_prefix[var][1]
    elif file.info['file_from'] == '百度网盟':
        pass
    elif file.info['file_from'] == '页游后台':
        # data[0] 是和 key_adm_xx 只有顺序不同的list
        st = set(list(file.data[0].keys()))
        st_ss = set(keys_adm_ss)
        st_wm = set(keys_adm_wm)
        # if list(file.data[0].keys()) == adm_ss_keys:
        # todo:判断方法有问题?
        if st_ss == st and len(keys_adm_ss) == len(list(file.data[0].keys())):
            file.info['game'] = file.data[0]['游戏']
            file.info['begin_date'] = file.data[0]['开始时间']
            file.info['end_date'] = file.data[0]['结束时间']
            file.info['type'] = '搜索'
        elif st_wm == st and len(keys_adm_wm) == len(list(file.data[0].keys())):
            file.info['type'] = '网盟'
        else:
            print('--页游后台表格有问题--')
            sys.exit()
    else:
        print('--不能识别来源的表格--')
        # todo: 哪个对象的 print
    return file


# 对字典切片，dic 为原始字典，slic 为原始字典所需的键值片段。
def dict_slice(dic, slic):
    if set(list(dic.keys()) + slic) != set(slic):
        print('--切片键值片段错误--')
        sys.exit()
    new_dic = {}
    for key in slic:
        new_dic.update(key, dic[key])
    return new_dic


def pinbiao(f1, f2, mod=None):
    f1 = getdata(f1)
    f2 = getdata(f2)
    if f1.info['type'] == f2.info['type']:
        if f1.info['file_from'] == '页游后台' and f2.info['file_from'] in ads_channels:
            f1, f2 = f2, f1
        elif f2.info['file_from'] == '页游后台' and f1.info['file_from'] in ads_channels:
            pass
        else:
            print('--请指定正确的表格1--')
            sys.exit()
    else:
        print('--请指定正确的表格2--')
        sys.exit()
    if mod is None:
        pass
    else:
        if set(keys_channels[f1.info['file_from']] + mod) != set(keys_channels[f1.info['file_from']]):
            # set(a + b) == set(a), b是a的子集
            print('--mod is not right--')
            sys.exit()
    f1.data = dedup.dedup(f1.data, f1.info['file_from'])
    # rst, information = functions.pb(f1.data, f2.data, f1.info)
    if f1.info['file_from'] == '百度搜索':
        rst, information = functions.pinbiao_bdss(f1.data, f2.data, f1.info)
    elif f1.info['file_from'] == '百度网盟':
        rst, information = functions.pinbiao_bdwm(f1.data, f2.data, f1.info)
    elif f1.info['file_from'] == '360搜索':
        rst, information = functions.pinbiao_360ss(f1.data, f2.data, f1.info)
    elif f1.info['file_from'] == '搜狗搜索':
        rst, information = functions.pinbiao_sgss(f1.data, f2.data, f1.info)
    else:
        print('--拼表没成功--')
        sys.exit()
    if mod:
        for x in rst:
            index = rst.index(x)
            rst[index] = dict_slice(x, mod)
            # x = dict_slice(x, slim_order), 这个写法无效。
    return rst, information


def excel_file_list(raw_path):
    all_files = os.listdir(raw_path)
    excel_files = {}
    j = 1
    for i in range(len(all_files)):
        filename = all_files[i].split('.')[0]
        extension = all_files[i].split('.')[-1]
        if extension == 'csv':
            excel_files[j] = all_files[i]
            j += 1
        elif extension == 'xls':
            excel_files[j] = all_files[i]
            j += 1
        elif extension == 'xlsx':
            excel_files[j] = all_files[i]
            j += 1
    for i in range(1, len(excel_files) + 1):
        print(i, ',', excel_files[i], '\n')
    return excel_files


if __name__ == '__main__':
    file1 = 'input/adm_20150120_232318.csv'
    file2 = 'input/Baidu-大皇帝1-8141563-投放网络-2015-01-19-2015-01-19.csv'
    input_folder = '原始表格'
    output_folder = '拼表结果'
    if os.path.isdir(input_folder):
        pass
    else:
        os.mkdir(input_folder)
    if os.path.isdir(output_folder):
        pass
    else:
        os.mkdir(output_folder)
    file_list = excel_file_list(input_folder)
    file1 = int(input('选择第一个表格：'))
    while file1 not in file_list.keys():
        file1 = int(input('重选第一个表格：'))
    file2 = int(input('选择第二个表格：'))
    while file2 not in file_list.keys() or file2 == file1:
        file2 = int(input('重选第二个表格：'))
    file1 = input_folder + '/' + file_list[file1]
    file2 = input_folder + '/' + file_list[file2]
    result, info = pinbiao(file1, file2)
    result_name = info['file_from'] + '-' + info['game'] + '-' + info['begin_date'] + '至' + info['end_date']
    with open(result_name + '.csv', 'w', newline='') as f:
        header = keys_order[info['file_from']]
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for i in result:
            writer.writerow(i)
    sys.exit()