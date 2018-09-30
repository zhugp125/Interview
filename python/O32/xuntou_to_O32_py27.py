# coding=GBK
# ѸͶ��ʽ�ļ�ת��ΪO32�ļ�
# �ļ����룺GBK
# python2.7 32-bit
# ��Ҫ��װ�ĵ������⣺dbfread,dbfpy,xlrd,xlwt

import csv
import dbfread
from dbfpy import dbf
import xlrd
import xlwt
import itertools

'''
��ȡTXT�ļ���������ͷ����һ�У������ݣ������У�
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
    
    # ���ļ�����ֻ����ͷ���ļ�������None
    if len(content) > 1:
        return content[0], content[1:]

'''
дTXT�ļ�
@filename �ļ���
@header   ��ͷ
@content  ����
'''
def writeTxtFile(filename, header, content):
    with open(filename, "w") as f:
        # д��ͷ
        f.write('\t'.join(header) + '\n')
        # д�ļ�����
        for line in content:
            f.write('\t'.join(line) + '\n')

'''
��ȡXLS,XLSX�ļ���������ͷ����һ�У������ݣ������У�
'''
def readExcelFile(filename):
    # �򿪹�����
    workbook = xlrd.open_workbook(filename=filename)
    # ������ȡ��һ��������
    booksheet = workbook.sheet_by_index(0)
    # ���صĽ����
    result = []
    for i in range(booksheet.nrows):
        result.append(booksheet.row_values(i))
    
    if len(result) > 1:
        return result[0], result[1:]

'''
дXLS,XLSX�ļ�
@filename �ļ���
@header   ��ͷ
@content  ����
'''
def writeExcelFile(filename, header, content):
    # ��Ϊ���붼��Unicode�ַ�������ʹ��utf-8���������ת��
    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)

    # д��ͷ
    row = 0
    for col in range(len(header)):
        booksheet.write(row, col, header[col])

    # д����
    for lines in content:
        row += 1
        for col in range(len(lines)):
            booksheet.write(row, col, lines[col])

    # �����ļ�
    workbook.save(filename)

'''
��ȡCSV�ļ���������ͷ����һ�У������ݣ������У�
'''
def readCsvFile(filename):
    content = []
    with open(filename, "rb") as f:
        spamreader = csv.reader(f, delimiter=' ', quotechar='|')
        for row in spamreader:
            content.append(row[0].split(','))

    # ���ļ�����ֻ����ͷ���ļ�������None
    if len(content) > 1:
        return content[0], content[1:]

'''
дCSV�ļ�
@filename �ļ���
@header   ��ͷ
@content  ����
'''
def writeCsvFile(filename, header, content):
    with open(filename, "wb") as f:
        f.write(','.join(header) + '\n')

        for line in content:
            f.write(','.join(line) + '\n')

'''
��ȡDBF�ļ���������ͷ����һ�У������ݣ������У�
'''
def readDbfFile(filename):
    table = dbfread.DBF(filename, encoding='GBK')

    content = []
    for record in table:
        line = []
        for field in record:
            line.append(record[field])
        # ��ӵ������б���
        content.append(line)

    if len(content) > 0:
        return table.field_names, content

'''
дDBF�ļ�
@filename �ļ���
@header   ��ͷ
@content  ����
'''
def writeDbfFile(filename, header, content):
    # ��dbf
    db = dbf.Dbf(filename, new=True)
    # д��ͷ
    for field in header:
        # �˴���Ҫ�ĳɳ��ȿ���ģ�����̫�̻ᵼ�����ݱ��ض�
        if type(field) == unicode:
            field = field.encode('GBK')
        db.addField((field, 'C', 20))

    # д����
    for record in content:
        rec = db.newRecord()
        for key, value in itertools.izip(header, record):
            if type(value) == unicode:
                rec[key] = value.encode('GBK')
            else:
                rec[key] = value
            rec.store()
    # �ر��ĵ�
    db.close()

header, content = readExcelFile("D:/�ļ���/position.xls")
print(header)
print(len(content))

writeDbfFile("D:/�ļ���/position_copy.dbf", header, content)