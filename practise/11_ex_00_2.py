# 搜索以 'X' 开头，后跟任何非空白字符和 ':'
# 再后跟一个空格和任何数字的行。
# 该数字可以包含小数。
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+', line):
        print(line)
# # 代码: https://www.py4e.com/code3/re10.py
print()
'''
当我们运行程序时，我们看到数据被很好地过滤，只显示了我们正在寻找的行。
输出：
X-DSPAM-Confidence: 0.8475
X-DSPAM-Probability: 0.0000
X-DSPAM-Confidence: 0.6178
X-DSPAM-Probability: 0.0000
...

但现在我们必须解决提取数字的问题。
虽然使用 split 足够简单，但我们可以使用正则表达式的另一个特性来同时搜索和解析行。
圆括号是正则表达式中的另一个特殊字符。
当你向正则表达式添加圆括号时，它们在匹配字符串时会被忽略。
但是当你使用 findall() 时，
'''
# 搜索以 'X' 开头，后跟任何非空白字符和 ':'
# 再后跟一个空格和任何数字的行。该数字可以包含小数。
# 然后如果数字大于零，则打印该数字。
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    '''圆括号表示虽然你希望整个表达式都匹配，
    #但你只对提取匹配正则表达式的子字符串的一部分感兴趣。'''
    if len(x) > 0:
        print(x)
# 代码: https://www.py4e.com/code3/re11.py
'''我们没有调用 search()，而是在表示浮点数的正则表达式部分周围添加了圆括号，以表明我们只希望 findall() 返回匹配字符串的浮点数部分。

这个程序的输出如下：

['0.8475']
['0.0000']
['0.6178']
['0.0000']
['0.6961']
['0.0000']
...'''
print()



'''Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772'''
# 搜索以 'Details: rev=' 开头
# 后跟数字的行
# 如果找到数字，则打印该数字

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9]+)', line)
    if len(x) > 0:
        print(x)

# 代码: https://www.py4e.com/code3/re12.py
'''
翻译我们的正则表达式，我们正在寻找以 Details: 开头，
后跟任意数量的字符 (.*)，再后跟 rev=，然后是一个或多个数字的行。
我们想找到匹配整个表达式的行，但我们只想提取行末尾的整数，
所以我们将 [0-9]+ 用圆括号括起来。
当我们运行程序时，我们得到以下输出：
['39772']
['39771']
['39770']
['39769']
...
'''