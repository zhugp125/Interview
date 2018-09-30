# coding=GBK
# 迅投格式文件转换为O32文件
# 文件编码：GBK
# python2.7 32-bit
# 需要安装的第三方库：dbfread,dbfpy,xlrd,xlwt

import csv
import dbfread
from dbfpy import dbf
import xlrd
import xlwt
import itertools

'''
读取TXT文件，返回列头（第一行）和内容（其余行）
'''
def readTxtFile(filename):
    content = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip('\n')
            if line == '':
                continue
            content.append(line.split('\t'))
    
    # 空文件或者只有列头的文件，返回None
    if len(content) > 1:
        return content[0], content[1:]

'''
写TXT文件
@filename 文件名
@header   列头
@content  内容
'''
def writeTxtFile(filename, header, content):
    with open(filename, "w") as f:
        # 写列头
        f.write('\t'.join(header) + '\n')
        # 写文件内容
        for line in content:
            f.write('\t'.join(line) + '\n')

'''
读取XLS,XLSX文件，返回列头（第一行）和内容（其余行）
'''
def readExcelFile(filename):
    # 打开工作表
    workbook = xlrd.open_workbook(filename=filename)
    # 用索引取第一个工作薄
    booksheet = workbook.sheet_by_index(0)
    # 返回的结果集
    result = []
    for i in range(booksheet.nrows):
        result.append(booksheet.row_values(i))
    
    if len(result) > 1:
        return result[0], result[1:]

'''
写XLS,XLSX文件
@filename 文件名
@header   列头
@content  内容
'''
def writeExcelFile(filename, header, content):
    # 因为输入都是Unicode字符，这里使用utf-8，免得来回转换
    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)

    # 写列头
    row = 0
    for col in range(len(header)):
        booksheet.write(row, col, header[col])

    # 写内容
    for lines in content:
        row += 1
        for col in range(len(lines)):
            booksheet.write(row, col, lines[col])

    # 保存文件
    workbook.save(filename)

'''
读取CSV文件，返回列头（第一行）和内容（其余行）
'''
def readCsvFile(filename):
    content = []
    with open(filename, "rb") as f:
        spamreader = csv.reader(f, delimiter=' ', quotechar='|')
        for row in spamreader:
            content.append(row[0].split(','))

    # 空文件或者只有列头的文件，返回None
    if len(content) > 1:
        return content[0], content[1:]

'''
写CSV文件
@filename 文件名
@header   列头
@content  内容
'''
def writeCsvFile(filename, header, content):
    with open(filename, "wb") as f:
        f.write(','.join(header) + '\n')

        for line in content:
            f.write(','.join(line) + '\n')

'''
读取DBF文件，返回列头（第一行）和内容（其余行）
'''
def readDbfFile(filename):
    table = dbfread.DBF(filename, encoding='GBK')

    content = []
    for record in table:
        line = []
        for field in record:
            line.append(record[field])
        # 添加到返回列表中
        content.append(line)

    if len(content) > 0:
        return table.field_names, content

'''
写DBF文件
@filename 文件名
@header   列头
@content  内容
'''
def writeDbfFile(filename, header, content):
    # 打开dbf
    db = dbf.Dbf(filename, new=True)
    # 写列头
    for field in header:
        # 此处需要改成长度可配的，长度太短会导致数据被截断
        if type(field) == unicode:
            field = field.encode('GBK')
        db.addField((field, 'C', 20))

    # 写数据
    for record in content:
        rec = db.newRecord()
        for key, value in itertools.izip(header, record):
            if type(value) == unicode:
                rec[key] = value.encode('GBK')
            else:
                rec[key] = value
            rec.store()
    # 关闭文档
    db.close()

header, content = readExcelFile("D:/文件单/position.xls")
print(header)
print(len(content))

writeDbfFile("D:/文件单/position_copy.dbf", header, content)