cheeses = ['Cheddar', 'Edam', 'Gouda']

print(cheeses[-1:-2:-1])
'''
#### 1. Python 切片的基本语法
Python 的完整切片语法是：
```python
list[start:end:step]
```
- `start`：起始索引（包含）
- `end`：结束索引（不包含）
- `step`：步长（正数从左到右，负数从右到左）
'''

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
#t =t.sort()#错误做法
#大多数列表方法是无返回值的（void）；
# #它们修改列表并返回 None。
# #如果你不小心写了 t = t.sort()，你会对结果感到失望。
print(t)
print()
s = 'pining for the fjords'
t = s.split()
a = list(s)
print(t)
# ['pining', 'for', 'the', 'fjords']
print(t[2])
print(type(t))
print()
print(a)
print(a[2])
print(type(a))
'''
list 函数将字符串分解为单个字母。如果你想将字符串分解为单词，可以使用 split 方法：
'''
print()
print()


print('3')
t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
dell =delimiter.join(t)
print(dell)
# 'pining for the fjords'
'''join 是 split 的逆操作。它接受一个字符串列表并将元素连接起来。
join 是一个字符串方法，所以你必须在分隔符上调用它，并将列表作为参数传递：
在这种情况下，分隔符是空格字符，所以 join 在单词之间放置一个空格。
要连接没有空格的字符串，你可以使用空字符串 "" 作为分隔符。'''

'''
通常，当我们读取文件时，我们想对行做些事情，而不仅仅是打印整行。
我们常常想找到“有趣的行”，然后解析 (parse) 该行以找到行中一些有趣的部分 (part)。
如果我们想从那些以“From”开头的行中打印出星期几该怎么办？

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
'''
fhandle = open('mbox-short.txt')
for parse in fhandle:
    parse = parse.rstrip()
    if not parse.startswith('From '):continue
    world = parse.split()
    print(world[2])
'''
错误写法：

if not parse.startswith('From'):  # 少了空格

    会匹配到：

        From （正确分隔行）

        From:（错误匹配，这是邮件头字段）

        From-Text: ...（意外匹配无关行）'''


print()
print()
import os

# 模块对象的属性字典
#print(os.__dict__)  # 包含所有模块变量和函数

# 模块本身就是对象
print(os.__name__)  # 'os'
print(id(os))       # 唯一内存地址
# 模块函数本身就是对象
print(os.sys.__name__)  # 'os,sys'
print(id(os.sys))       # 唯一内存地址

def greet(name):
    return f"你好, {name}!"

print(type(greet))        # <class 'function'>
print(id(greet))          # 内存地址（唯一身份）
print(greet.__name__)     # 'greet'（属性）


print()


#切片运算符创建了一个新列表，赋值使 t 引用它，但这一切对作为参数传递的列表没有任何影响。
def delete_head(t):
    del t[0]

letters = ['a', 'b', 'c']
delete_head(letters)
x= print(letters)
# ['b', 'c']
print(x is letters)
print(letters)

print()

#另一种方法是编写一个创建并返回新列表的函数。例如，tail 返回列表中除第一个元素之外的所有元素：
def tail(t):
    return t[1:]
letters = ['a', 'b', 'c']
rest = tail(letters)
print(rest)
print(letters)
['b', 'c']