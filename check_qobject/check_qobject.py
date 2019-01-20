#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys
import os
import re

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

def check_object(file):
    with open(file, 'r') as f:
        pattern = 'class\s+(\S+)\s+:\s+(public|private|protected)\s+(\S+)\s+{([^{]+)};'
        for item in re.finditer(pattern, f.read(), re.M):
            class_name = item.group(1)
            inherit_property = item.group(2)
            inherit_name = item.group(3)
            section_text = item.group(4)
            
    return False, ""

def main():
    input_dir, output_file = ParserCommand()

    error_msg = ''
    for file in getAllHeaderFile(input_dir):
        success, msg = check_object(file)
        if not success:
            error_msg += msg
    
    with open(output_file, 'w') as f:
        f.write(error_msg)
    
if __name__ == '__main__':
    main()