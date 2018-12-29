关于python编程的一些指南

---

### 优雅的Python指南

1. 遍历一个范围内的数字

``` python
for i in xrange(6)
    print i ** 2
```

xrange会返回一个迭代器，用来一次一个值地遍历一个范围。这种方式会比range更省内存。<br>
xrange在python3中已经改名为range

2. 遍历一个集合

``` python
colors = ['red', 'green', 'blue', 'yellow']
for color in colors:
    print color
```

3. 反向遍历

``` python
colors = ['red', 'green', 'blue', 'yellow']
for color in reversed(colors):
    print color
```

4. 遍历一个集合及其下标

``` python
colors = ['red', 'green', 'blue', 'yellow']
for i, color in enumerate(colors):
    print i, '--->', color
```

5. 遍历两个集合

``` python
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']
for name, color in izip(names, colors):
    print name, '--->', color
```
zip在内存中生存一个新的列表，需要更多的内存。izip比zip效率更高。<br>
python3中，izip改名为zip，并替换了原来的zip成为内置函数。

6. 有序地遍历

``` python
colors = ['red', 'green', 'blue', 'yellow']
# 正序
print sorted(colors)

# 倒序
print sorted(colors, reverse=True)
```

7.自定义排序顺序

``` python
colors = ['red', 'green', 'blue', 'yellow']
print sorted(colors, key=len)
```

8. 调用一个函数直到遇到标记值

```python
blocks = []
for block in iter(partial(f.read, 32), ''):
    blocks.append(block)
```

9. 在循环内识别多个退出点

```python
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i
```

10. 遍历字典的key

```python
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

for k in d:
    print k

for k in d.keys():
    del d[k]
```
第二种方法可以修改字典的key。<br>
另外python3，需要显示地写list(d.keys())

11. 遍历一个字典的key和value

```python
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
for k, v in d.iteritems():
    print k, '--->', v
```
python3中已经没有iteritems()了

12. 用key-value对构建字典

```python
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']
d = dict(izip(names, colors))
```

13. 用字典计数

```python
colors = ['red', 'green', 'red', 'blue', 'yellow', 'red']

d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1

# defaultdict
d = defaultdict(int)
for color in colors:
    d[color] += 1
```

14. 字典分组

```python
names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']

d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)
```

15. 字典的原子操作popitem

```python
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
while d:
    key, value = d.popitem()
    print key, '--->', value
```

16. 连接字典

```python
d1 = {'key1': 'value1', 'd1': 'v1'}
d2 = {'key2': 'value2', 'd2': 'v2'}

# python 3
d = ChainMap(d1, d2)
```

17. 用namedtuple提高多个返回值的可读性

```python
TestResults = namedtuple('TestResults', ['failed', 'attempted'])
```

18. unpack序列

```python
p = 'Raymond', 'Hettinger', 30, 'python@com.cn'

fname, lname, age, email = p
```

19. 交换两个变量的值

```python
x, y = y, x
```

20. 连接字符串

```python
names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']

print ','.join(names)
```

21. 打开关闭文件

```python
with open('data.txt') as f:
    data = f.read()
```

22. 如何使用锁

```python
# 创建锁
lock = threading.Lock()

with lock:
    print 'Critical section 1'
    print 'Critical section 2'
```

23. 列表解析和生成器

```python
print sum(i**2 for i in xrange(10))
```