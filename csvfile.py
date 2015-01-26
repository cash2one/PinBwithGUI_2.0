﻿__author__ = 'xuhuan'
import csv
import re
import os

file_from = ['百度搜索', '百度网盟', '360搜索', '搜狗搜索', '页游后台']
bd_account_prefix = {'Baidu-大皇帝1-8141563': ['百度网盟-大皇帝', '大皇帝']}


class CsvFile(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.info = self._file_info()

    def _file_info(self):
        if not os.path.exists(self.file_path):
            info = {'tip': '--- 不存在的文件 ---'}
            # self.data = info
            return info
        prefix, suffix = self.file_path.split('.')

        if suffix != 'csv':
            info = {'tip': '-- 不支持的文件类型 --'}
            # self.data = info
            return info
        file_name = prefix.split('/')[-1]
        info = {'file_from': '', 'begin_date': '', 'end_date': '', 'game': '', 'type': ''}

        if file_name.startswith('Baidu-') and '投放网络' in file_name:
            info['file_from'] = '百度网盟'
            info['type'] = '网盟'
            reg = re.compile('^.*-.*-\d{7}')
            account = reg.findall(file_name)
            # account is a  list
            prefix = bd_account_prefix[account[0]][0]
            info.update({'prefix': prefix})
            regx = re.compile('20\d{2}-\d{2}-\d{2}')
            date = regx.findall(file_name)
            if not len(date) == 2:
                print('date catch error')
            else:
                info['begin_date'] = date[0]
                info['end_date'] = date[1]
        elif file_name.startswith('guanjianci_baogao'):
            info['file_from'] = '百度搜索'
            info['type'] = '搜索'
            regx = re.compile('2015\d{4}')
            date = regx.findall(file_name)
            if not len(date) == 2:
                print('date catch error')
            else:
                info['begin_date'] = date[0]
                info['end_date'] = date[1]
        elif file_name.startswith('效果评估报告'):
            info['file_from'] = '360搜索'
            info['type'] = '搜索'
            regx = re.compile('20\d{2}-\d{2}-\d{2}')
            date = regx.findall(file_name)
            if not len(date) == 2:
                print('date catch error')
            else:
                info['begin_date'] = date[0]
                info['end_date'] = date[1]
        elif file_name == '统计报告':
            info['file_from'] = '搜狗搜索'
            info['type'] = '搜索'
        elif file_name.startswith('adm_'):
            info['file_from'] = '页游后台'
        if '大皇帝' in file_name:
            info['game'] = '大皇帝'
        return info

    def get_data(self):
        direct_read = ['页游后台', '360搜索', '百度搜索', '搜狗搜索']
        if self.data == self.info:
            return self.data
        if self.info['file_from'] in direct_read:
            with open(self.file_path, 'r') as f:
                reader = csv.DictReader(f, restkey='标记', restval=0)
                dicts = [row for row in reader]
        elif self.info['file_from'] == '百度网盟':
            with open(self.file_path, 'r') as f:
                reader = csv.reader(f)
                rows = [row for row in reader]
            s = rows[3][1]
            if s:
                ds = {}
                ss = s.split('/')
                del ss[0]
                for i in ss:
                    a, b = i.split('：')
                    ds.update({a: b})
            rows = rows[5:]
            dicts = []
            for i in range(len(rows) - 1):
                dct = dict(zip(rows[0], rows[i + 1]))
                dct.update(ds)
                dicts.append(dct)
        self.data = dicts
        return dicts




