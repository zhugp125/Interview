# coding=GBK
# 032文件转换为迅投格式文件
# 文件编码：GBK
# python2.7 32-bit

import time
import os
import dbfread
import ConfigParser
from collections import namedtuple

# 从dbf文件读取的数据结构
Stock = namedtuple('Stock', ['code', 'volume'])

# 读取dbf一行记录中特定的列
def getValue(field_list, record):
    for field in record:
        if field in field_list:
            return record[field]
    return ""

cf = ConfigParser.ConfigParser()
cf.read('./config.ini')

# 读取配置文件
file_list = str(cf.get('input', 'file')).split(',')
input_path = cf.get('input', 'path')
output_path = cf.get('output', 'path')
code_list = str(cf.get('field', 'stock_code')).split(',')
volume_list = str(cf.get('field', 'volume')).split(',')
trade_type = cf.getint('trade', 'trade_type')
channel_no = cf.getint('trade', 'channel_no')
interval = cf.getint('time', 'interval')

# 检查输出目录是否存在，不存在要创建
if not os.path.exists(output_path):
    os.makedirs(output_path)

'''
读取dbf文件
'''
def readDbfFile(filepath, encode=None):    
    # 返回的结果集合
    stocks = []
    # 数据表文件名
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

# 写迅投默认文件单格式文件
def writeFile(filepath, stocks):
    with open(filepath, 'w') as f:
        # 写交易类型和通道号
        f.write(str(trade_type) + "," + str(channel_no) + "\n")
        # 写下单参数
        for stock in stocks:
            f.write(stock.code + "\t" + str(stock.volume) + "\n")

def main():
    while True:
        # 休眠
        time.sleep(interval)
        for file in file_list:
            filepath = input_path + file

            # 文件不存在，返回
            if (os.path.exists(filepath) != True):
                continue
            
            # 读取内容为空，返回
            stocks = readDbfFile(filepath, encode='gbk')
            if (len(stocks) == 0):
                continue

            # 写文件
            basename = os.path.basename(filepath)
            output_file = output_path + os.path.splitext(basename)[0] + ".txt";
            writeFile(output_file, stocks)
            print('write file end - ' + output_file)

if __name__ == '__main__':
    main()