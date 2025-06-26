'''使用字典进行多重赋值

结合 items、元组赋值和 for，你可以看到一个很好的代码模式，用于在单个循环中遍历字典的键和值：

d = {'a':10, 'b':1, 'c':22}
for key, val in d.items():
    print(val, key)

这个循环有两个迭代变量，因为 items 返回一个元组列表，而 key, val 是一个元组赋值，它依次迭代字典中的每个键值对。

对于循环的每次迭代，key 和 val 都前进到字典中的下一个键值对（仍然是哈希顺序）。

这个循环的输出是：

10 a
1 b
22 c

再次强调，它是按哈希键顺序（即没有特定顺序）。

如果我们将这两种技术结合起来，我们可以按存储在每个键值对中的值对字典内容进行排序并打印出来。

为此，我们首先创建一个元组列表，其中每个元组是 (value, key)。
items 方法会给我们一个 (key, value) 元组的列表，但这次我们想按值而不是键排序。
一旦我们构建了包含值-键元组的列表，对列表进行逆序排序并打印出新的、已排序的列表就很容易了。'''


import string
fhand = open('romeo-full.txt')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# 按值对字典排序
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)

# 代码: https://www.py4e.com/code3/count3.py

'''程序的第一部分读取文件并计算将每个单词映射到该单词在文档中计数的字典，这部分保持不变。但是我们不是简单地打印出 counts 并结束程序，而是构建了一个 (val, key) 元组的列表，然后按逆序对列表进行排序。

由于值是第一个元素，它将用于比较。如果存在多个具有相同值的元组，它将查看第二个元素（键），因此值相同的元组将进一步按键的字母顺序排序。

最后，我们编写了一个漂亮的 for 循环，它执行多重赋值迭代，并通过迭代列表的一个切片（lst[:10]）打印出十个最常见的单词。

所以现在输出终于看起来像我们想要的词频分析结果了。'''
#这个复杂的数据解析和分析可以用一个易于理解的 19 行 Python 程序完成，
# 这是 Python 成为探索信息的良好语言选择的原因之一。
print()
print('使用元组作为字典的键')
directory = {(1,2):111,('a','s'):2222,}
directory['last','first'] = 'number'
for last, first in directory:
    print(first, last, directory[last,first])
#这个循环遍历 directory 中的键，这些键是元组。
#它将每个元组的元素赋给 last 和 first，然后打印名字和对应的电话号码。
print()
'''reversed() 对元组的使用

    功能：返回一个反向迭代器（Iterator），而不是直接返回元组或列表。

    原因：避免内存浪费（迭代器惰性计算），需手动转换为元组或列表。
    
    由于元组不可变，返回新对象（列表或迭代器）是最安全的方案。'''
print('内置函数reversed() 对元组的使用')
my_tuple = (1, 2, 3)
reversed_iterator = reversed(my_tuple)
print('返回类型',type(reversed_iterator))
reversed_list = list(reversed_iterator)  # 转换为列表
print('list()转换为列表',reversed_list)  # 输出 [3, 2, 1]

# 如需元组结果
reversed_tuple = tuple(reversed(my_tuple))
print('tuple()转换元组',reversed_tuple)  # (3, 2, 1)
print()
'''sorted() 对元组的使用

    功能：返回一个新的排序后的列表（List），而不是元组。

    原因：排序操作属于“修改”行为，但元组不可变，所以 sorted() 返回一个新列表（可变）。'''
print('sorted() 对元组的使用')
my_tuple = (3, 1, 4, 2)
sorted_list = sorted(my_tuple)  # 返回列表
print(sorted_list)  # 输出 [1, 2, 3, 4]
print('sorted() 返回一个新列表',type(sorted_list))  # <class 'list'>

# 如需元组结果，需显式转换
sorted_tuple = tuple(sorted(my_tuple))
print('tuple()转换元组',sorted_tuple)  # (1, 2, 3, 4)