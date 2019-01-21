#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys
import os
import re

class ClassInfo:
    def __init__(self, file, class_name, inherit_name, inherit_property, section_text):
        self._file = file
        self._class_name = class_name
        self._inherit_name = inherit_name
        self._inherit_property = inherit_property
        self._has_qobject = section_text.find('Q_OBJECT') is not -1
        self._has_slots = re.search('slots|Q_SLOTS', section_text, re.M) is not None
        self._has_signal = re.search('signals|Q_SIGNALS', section_text, re.M) is not None
        self._error_msg = ''
    
    def get_file(self):
        return self._file

    def get_class_name(self):
        return self._class_name
    
    def get_inherit_name(self):
        return self._inherit_name

    def get_inherit_property(self):
        return self._inherit_property

    def has_qobject(self):
        return self._has_qobject

    def has_slots(self):
        return self._has_slots

    def has_signal(self):
        return self._has_signal

    def display(self):
        print('file : {}'.format(self._file))
        print('class name : {}'.format(self._class_name))
        print('inherit name : {}'.format(self._inherit_name))
        print('inherit property : {}'.format(self._inherit_property))
        print('has qobject : {}'.format(self._has_qobject))
        print('has slots : {}'.format(self._has_slots))
        print('has signal : {}'.format(self._has_signal))
        print('')

    def parse(self):
        ret = self._has_qobject is not (self._has_signal or self._has_slots)
        if ret:
            if self._has_qobject:
                self._error_msg = '{} {} needless "Q_OBJECT"\n'.format(self._file, self._class_name)
            else:
                self._error_msg = '{} {} need to add "Q_OBJECT"\n'.format(self._file, self._class_name)
        return ret
    
    def get_error_msg(self):
        return self._error_msg

def ParserCommand():
    output_file = 'msg.txt'
    if len(sys.argv) is 1:
        raise ValueError('must input a directory in command line')
    elif len(sys.argv) > 2:
        output_file = sys.argv[2]

    input_dir = sys.argv[1]
    if not os.path.isdir(input_dir):
        raise ValueError('{} is not a directory'.format(input_dir))

    output_dir = os.path.split(output_file)[0]
    if len(output_dir) > 0 and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    return input_dir, output_file

def getAllHeaderFile(dirname):
    result = []

    for fpath, dpath, files in os.walk(dirname):
        [result.append(os.path.join(fpath, file)) for file in files if file.endswith('.h') or file.endswith('.hpp')]
        
    return result

def check_object(file, result):
    with open(file, 'r') as f:
        pattern = 'class\s+(\S+)\s+:\s+(public|private|protected)\s+(\S+)\s+{([^{]+)};'
        for item in re.finditer(pattern, f.read(), re.M):
            class_name = item.group(1)
            inherit_property = item.group(2)
            inherit_name = item.group(3)
            section_text = item.group(4)
            info = ClassInfo(file, class_name, inherit_name, inherit_property, section_text)
            result.append(info)
            
def main():
    input_dir, output_file = ParserCommand()

    items = []
    for file in getAllHeaderFile(input_dir):
        check_object(file, items)

    for item in items:
        item.display()

    with open(output_file, 'w') as f:
        [f.write(item.get_error_msg()) for item in items if item.parse()]
    
if __name__ == '__main__':
    main()