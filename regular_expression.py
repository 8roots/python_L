import re
x = 'From stephen.marquard@utc.ac.za Sat Jan  5 09:14:16 2008'
z = 'From: Using the : character'
a = re.findall('^F.+:',z)#贪婪匹配#匹配以F开头--以:结尾

b = re.findall('^F.+?:',z)
print()
print(a)
print()
print(b)
print()
y = re.findall(r'\S+@\S+',x)#r原始字符串，避免 `\` 被 Python 转义（如 `\n`, `\t` 等）
print(y)
print()


x = 'From stephen.marquard@utc.ac.za Sat Jan  5 09:14:16 2008'
c = re.findall(r'^From (\S+@\S+)',x)
print(c)
#  r'...'  	原始字符串，防止 \ 被 Python 转义
#  ^From  匹配行首必须是 "From"（如果前面有空格就不匹配）
#  捕获组（括号）——提取一个邮箱地址
#  @	字面匹配 @ 符号
#匹配开头,提取回来括号里的内容,括号表示开始提取与结束提取
#\S+匹配一个或多个非空白字符，用于用户名和域名
# 用括号指定你想得到的返回值
#因为你用了括号 () 包住 \S+@\S+，这在正则中是捕获组（group），表示：
#   “我只想要这部分内容作为结果返回”。
