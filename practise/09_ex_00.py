'''练习 1： 下载文件副本
www.py4e.com/code3/words.txt
编写一个程序，读取 words.txt 中的单词并将它们存储为字典的键。
值是什么并不重要。
然后你可以使用 in 运算符作为一种快速检查字符串是否在字典中的方法。'''
fa = open('words.txt')
bg = dict()
for w in fa:
    w = w.split()
    # a = range(len(w))
    for f in w:
        a = '-'
        bg[f]=a
    
print(bg)
print()
print()

#假设给定一个字符串，你想计算每个字母出现的次数。
#你可以创建一个字典，以字符为键，以计数器为相应的值。
# 第一次遇到某个字符时，你将向字典中添加一个新项。
# 之后，你将增加现有项的值。
word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)
#{'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}

print()

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
print(counts.get('jan', 0))         #100
#                                   字典有一个名为 get 的方法，
#                                   它接受一个键和一个默认值如果键出现在字典中，
#                                   get 返回相应的值；否则返回默认值。
print(counts.get('tim', 0))         #0
print(counts)                       #{'chuck': 1, 'annie': 42, 'jan': 100}
print()
'''
我们可以使用 get 来更简洁地编写我们的直方图循环。
因为 get 方法自动处理键不在字典中的情况，
我们可以将四行代码缩减为一行，并消除 if 语句。'''
word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1
print(d)
'''
使用 get 方法简化这个计数循环最终成为 Python 中一个非常常用的“惯用法”(idiom)，
我们将在本书的其余部分多次使用它。
所以你应该花点时间比较一下使用 if 语句和 in 运算符的循环与使用 get 方法的循环。
它们做的事情完全相同，但后者更简洁。
'''