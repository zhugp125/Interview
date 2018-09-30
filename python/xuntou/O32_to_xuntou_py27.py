# coding=GBK
# 032�ļ�ת��ΪѸͶ��ʽ�ļ�
# �ļ����룺GBK
# python2.7 32-bit

import time
import os
import dbfread
import ConfigParser
from collections import namedtuple

# ��dbf�ļ���ȡ�����ݽṹ
Stock = namedtuple('Stock', ['code', 'volume'])

# ��ȡdbfһ�м�¼���ض�����
def getValue(field_list, record):
    for field in record:
        if field in field_list:
            return record[field]
    return ""

cf = ConfigParser.ConfigParser()
cf.read('./config.ini')

# ��ȡ�����ļ�
file_list = str(cf.get('input', 'file')).split(',')
input_path = cf.get('input', 'path')
output_path = cf.get('output', 'path')
code_list = str(cf.get('field', 'stock_code')).split(',')
volume_list = str(cf.get('field', 'volume')).split(',')
trade_type = cf.getint('trade', 'trade_type')
channel_no = cf.getint('trade', 'channel_no')
interval = cf.getint('time', 'interval')

# ������Ŀ¼�Ƿ���ڣ�������Ҫ����
if not os.path.exists(output_path):
    os.makedirs(output_path)

'''
��ȡdbf�ļ�
'''
def readDbfFile(filepath, encode=None):    
    # ���صĽ������
    stocks = []
    # ���ݱ��ļ���
    table = dbfread.DBF(filepath, encoding=encode)
    for record in table:
        code = getValue(code_list, record)
        volume_str = getValue(volume_list, record)
        volume = 0;
        if volume_str != "":
            volume = int(volume_str)
        
        if (volume > 0):
            stock = Stock(code, volume)
            stocks.append(stock)
    return stocks

# дѸͶĬ���ļ�����ʽ�ļ�
def writeFile(filepath, stocks):
    with open(filepath, 'w') as f:
        # д�������ͺ�ͨ����
        f.write(str(trade_type) + "," + str(channel_no) + "\n")
        # д�µ�����
        for stock in stocks:
            f.write(stock.code + "\t" + str(stock.volume) + "\n")

def main():
    while True:
        # ����
        time.sleep(interval)
        for file in file_list:
            filepath = input_path + file

            # �ļ������ڣ�����
            if (os.path.exists(filepath) != True):
                continue
            
            # ��ȡ����Ϊ�գ�����
            stocks = readDbfFile(filepath, encode='gbk')
            if (len(stocks) == 0):
                continue

            # д�ļ�
            basename = os.path.basename(filepath)
            output_file = output_path + os.path.splitext(basename)[0] + ".txt";
            writeFile(output_file, stocks)
            print('write file end - ' + output_file)

if __name__ == '__main__':
    main()