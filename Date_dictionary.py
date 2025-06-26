cabinet = dict()
cabinet['Summer'] = 12#把值赋予到键
cabinet['fall'] = 3
cabinet['spring'] = 75
print(cabinet)
print(cabinet['fall'])#打印键对应的值
cabinet['fall'] = cabinet['fall'] + 2#通过+2改变值,并返回
print(cabinet)


print()
print('制作直方图histogram , 统计事物的频率')


# 制作直方图histogram , 统计事物的频率
counts = dict()
names = ['a','b','a','c','b']
for name in names :
    if name not in counts:# ✅ 判断是否已经在字典中
        counts[name] = 1 # 首次出现，初始化为1
    else:
        counts[name] = counts[name] + 1 # 已存在，+1
print(counts)
#输出:{'a': 2, 'b': 2, 'c': 1}

print()
print('制作直方图histogram , 统计事物的频率_优化写法')

# 制作直方图histogram , 统计事物的频率_优化写法
counts = dict()
names = ['a','b','a','c','b']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
#counts.get(name, 0)：如果 name 不在字典里，就返回 0，否则返回已有值。

print()
print('遍历字典')
## 遍历字典
#虽然字典没有正儿八经的存储顺序,
# 但我们还是可以通过`for`循环来遍历它
A = {'chu' : 1 , 'f' : 42 , 'jan' : 100 }
for key in A:
	print(key, A[key])
     #这个迭代变量 key 会遍历键,它不会遍历值

A = {'chunck': 1, 'f': 42, 'jan': 100}
print("只遍历值:")
for v in A.values():
    print(v)
print("同时遍历键和值:")
for k, v in A.items():#每次循环都会自动解包一个 (key, value) 元组。
    print(k, v)


A = {'chunck': 1, 'f': 42, 'jan': 100}
print('.items() 的实际返回值')
print(A.items())
print('将.items() 的实际返回值,转换成列表')
print(list(A.items()))
#.items() 是 Python 字典（dict）中一个非常重要的方法，
# 常用于遍历字典中的键值对。


print('统计词频后按键值输出')
counts = {'hello': 3, 'world': 5, 'dedication' :1}
for word, count in counts.items():
    print(f"'{word}' appears {count} times.")
#与 sorted() 配合使用（按键排序）
print('与 sorted() 配合使用（按键排序）')
for k, v in sorted(counts.items()):
    print(k, v)
 #与 max() 配合使用（找最大值）
print('与 max() 配合使用（找最大值）')
max_word = max(counts.items(), key=lambda item: item[1])
print("Most frequent word:", max_word)
# 输出: Most frequent word: ('world', 5)

print('朴素的找最大值）')
counts = {'hello': 3, 'world': 5, 'dedication' :1}
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword,bigcount)