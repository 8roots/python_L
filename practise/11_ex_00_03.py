# 搜索以 From 和一个字符开头
# 后跟一个 00 到 99 之间的两位数，再后跟 ':' 的行
# 如果找到数字，则打印该数字
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', line)
    '''这个正则表达式的翻译是，我们正在寻找以 From 开头（注意空格）， 
    后跟任意数量的字符 (.*)，再后跟一个空格，
    再后跟两个数字 [0-9][0-9]，最后是一个冒号字符的行。
    这就是我们正在寻找的那种行的定义。'''
    if len(x) > 0: print(x)

# 代码: https://www.py4e.com/code3/re13.py
