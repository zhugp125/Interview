#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import pathlib
import collections
from datetime import datetime

# 1. file or directory counter
counter = collections.Counter(p.suffix for p in pathlib.Path.cwd().iterdir())
print(counter)

# 2. directory tree
def tree(directory):
    print(f'- {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '   ' * depth
        print(f'{spacer}+ {path.name}')

tree(pathlib.Path.cwd())

# 3. find last modify file
directory = pathlib.Path.cwd()
time, file_path = max((f.stat().st_mtime, f) for f in directory.iterdir())
print(datetime.fromtimestamp(time), file_path)
