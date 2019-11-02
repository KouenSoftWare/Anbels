
import re
import os
import json
import time
import pprint
import requests
import urllib.request


def main():
    pass


def get_stock_code(path):
    pass
    start_page = 1
    end_page = 193
    codes = {}
    while start_page <= end_page:
        print(f'正在下载第{start_page}页')
        req = requests.get(f'http://41.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124049144764879305947_1572678629338&pn={start_page}&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&fields=f12,f14&_=1572678629361')
        data = json.loads(req.text[req.text.find('{'):-2])
        for row in data['data']['diff']:
            codes[row['f12']] = row['f14']
        time.sleep(1)
        start_page += 1
    print(f"正在写入本地文件 {len(codes)} 行")
    file = open(f'{root_dir}/stock_code.json', 'w')
    json.dump(codes, file)
    file.close()


def get_stock_industry(path, stock):
    if os.path.exists(f'{path}/{stock}'):
        return
    data = json.loads(requests.get(
        f"http://f10.eastmoney.com/CoreConception/CoreConceptionAjax?code=SH{stock}").text)
    if 'status' in data and data['status'] == -1:
        data = json.loads(requests.get(
            f"http://f10.eastmoney.com/CoreConception/CoreConceptionAjax?code=sz{stock}").text)

    try:
        行业 = list(filter(lambda x: '昨日' not in x and '今日' not in x, data['hxtc'][0]['ydnr'].split(' ')))
        经营范围 = list(map(lambda x: x[:x.find('(')] if '(' in x else x, data['hxtc'][1]['ydnr'].replace('、', '').split(';')))
    except (IndexError, ):
        return
    os.mkdir(f'{path}/{stock}')
    file = open(f'{path}/{stock}/industry.json', 'w')
    json.dump(行业, file)
    file.close()
    file = open(f'{path}/{stock}/business_scope.json', 'w')
    json.dump(经营范围, file)
    file.close()
    print(f'加载{stock}的行业数据: ', 行业, 经营范围)


def get_stock_report(path, stock):
    pass


def get_stock_quote(path, stock):
    pass


def get_all_stock_base_info(path, file):
    stocks = json.load(file)
    for code in stocks:
        get_stock_industry(path, code)
        time.sleep(0.1)


if __name__ == '__main__':
    root_dir = './Data'
    get_all_stock_base_info(root_dir, open('./Data/stock_code.json'))
