
fhand = open('romeo.txt')                 # 打开文件 'romeo.txt'
counts = dict()                           # 创建一个空字典用于统计单词出现次数

for line in fhand:                        # 遍历文件的每一行
    words = line.split()                  # 使用 .split() 将一行拆分为单词列表
    for word in words:                    # 遍历该行的每个单词
        counts[word] = counts.get(word, 0) + 1  # 使用 get() 方法统计每个单词出现的次数

lst = list()                              # 创建一个空列表，用于存放 (次数, 单词) 形式的元组

for key, val in counts.items():           # 遍历字典中的 (单词, 次数) 键值对
    newtup = (val, key)                   # 创建新元组，把次数放前面，便于排序
    lst.append(newtup)                    # 将新元组添加到列表中

lst = sorted(lst, reverse=True)           # 对列表进行降序排序（默认按元组第一个元素，即次数排序）

for val, key in lst[:10]:                 # 取出排序后前10个高频单词的元组，解包为 val（次数）、key（单词）
    print(key, val)                       # 打印出单词和它对应的出现次数


c = {'a':10, 'b':1,'c':22}
print(sorted([(v,k) for k,v in c.items()]))
#🔁 是一个列表推导式：
#- 它将字典中的 `(key, value)` 反转成 `(value, key)`
#- 然后 `sorted()` 把这些元组按 **value 排序**
#- 最终输出排序后的结果
    