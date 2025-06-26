import re

text = "Hello, my name is Alice."

match = re.search(r"Alice", text)
if match:
    print("Found:", match.group())
else:
    print("Not found")

print(type(match))
print(match)

print()
print()

import re
line = "From stephen.marquard@uct.ac.za Sat Jan 5"

match = re.search(r'^From (\S+@\S+)', line)

if match:
    print("group(0):", match.group(0))  # 整个匹配："From stephen.marquard@uct.ac.za"
    print("group(1):", match.group(1))  # 括号中的内容："stephen.marquard@uct.ac.za"
print(match)


print()
print()
text = "abc 123 def 456"
# 找第一个数字
m = re.search(r'\d+', text)
print("search:", m.group()) #`re.search()`在整个字符串中搜索第一个符合 
lst = re.findall(r'\d+', text)
print("findall:", lst) 