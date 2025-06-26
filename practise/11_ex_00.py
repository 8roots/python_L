# 搜索包含 'From' 的行
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

# 代码: https://www.py4e.com/code3/re01.py
print()
# 搜索以 'From' 开头的行
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)

# 代码: https://www.py4e.com/code3/re02.py
print()
# 搜索以 'F' 开头，后跟
# 2 个字符，再后跟 'm:' 的行
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:', line):
        print(line)

# 代码: https://www.py4e.com/code3/re03.py
print()
# 搜索以 From 开头并包含 @ 符号的行
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)

# 代码: https://www.py4e.com/code3/re04.py