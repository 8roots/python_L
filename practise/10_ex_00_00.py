#如果参数是一个序列（字符串、列表或元组），
# 调用 tuple 的结果是一个包含该序列元素的元组：
q = tuple('lupins')
print(q)
print()
a = (1,2,3,4,5,)
b = 'asdfg'
t = tuple(a)
print(t)
print()
s = t+q
print(s)
print()

print('将是诗句里的单词，按单词数，降序排列')
txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))#列表里边 添加 元组
print(f'统计出来了，但是乱序{t}')
#  [(3, 'but'), (4, 'soft'), (4, 'what'), (5, 'light'), (2, 'in'), (6, 'yonder'), (6, 'window'), (6, 'breaks')]
print()
t.sort(reverse=True)
#元组比较  if (3, 'but') > (4, 'soft')：
#sort 首先比较第一个元素（长度），只有在比较第一个元素结果相同时
# 才考虑第二个元素来打破平局。
# 关键字参数 reverse=True 告诉 sort 按大到小降序排列。
print(f'降序排序：{t}')
print()
res = list()
for length, word in t:
    res.append(word)
print(f'最终结果：{res}')
'''第二个循环遍历元组列表，并按长度降序构建一个单词列表。
四个字符的单词按字母顺序倒序排序
所以在下面的列表中“what”出现在“soft”之前。'''
# 代码: https://www.py4e.com/code3/soft.py
print()
print()
'''元组赋值'''
print('元组赋值')
m = ('have', 'fun')
x, y = m  # 这是序列解包，不是元组赋值
print(f'x: {x},y: {y}')
'''
    Python 不会将 x, y 视为待创建的元组

    而是将其识别为 解包模式'''
# 错误理解：认为这是在创建元组
# (x, y) = m 实际上这是解包操作，不是创建元组
print()
print('元组不可变')
(d, y) = (1, 2)#元组不可变
print(type(x))
print()

'''单元素元组需加逗号'''
x, = (1,)  # 正确解包单元素元组
x = (1,)    # 这是将元组赋值给x，不是解包

print()

'''字典解包（Python 3.5+）'''
d = {'a': 1, 'b': 2}
x, y = d.values()  # 解包字典值
print('字典解包',x)
print()
'''💡 设计哲学

这种语法设计体现了 Python 的核心理念：

    明确优于隐晦：虽然括号可省略，但行为始终保持一致

    实用性：简化多变量赋值操作

    对称性：a, b = b, a 这样的交换操作极其优雅

总结来说，x, y = m 是 Python 的 序列解包语法，而非元组赋值。
理解这一点后，你会更自如地运用这个特性处理复杂的数据结构！'''


addr = 'monty@python.org'
uname, domain = addr.split('@')
print(type(uname))
a=(1,2,3)
print(type(a))

print('结合 items、元组赋值和 for，你可以看到一个很好的代码模式，用于在单个循环中遍历字典的键和值：')
d = {'a':10, 'b':1, 'c':22}
for key, val in d.items():
    print(val, key)
'''这个循环有两个迭代变量，因为 items 返回一个元组列表，而 key, val 是一个元组赋值，它依次迭代字典中的每个键值对。

对于循环的每次迭代，key 和 val 都前进到字典中的下一个键值对（仍然是哈希顺序）。'''
