date = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
a = date.find('@')
print(a)
b = date.find(' ',a)#我们将找到 @ 符号后面第一个空格的位置`
print(b)
c = date[a+1 : b]
print(c)


print()


print('双重分割split()法')
x = 'From stephen.marquard@utc.ac.za Sat Jan  5 09:14:16 2008'

words = x.split()          # 按空格分割成单词列表
email = words[1]           # 第二个单词是 email
pieces = email.split('@')  # 再按 @ 分割 email
print(pieces[1])           # 打印域名部分


print()


x = 'From stephen.marquard@utc.ac.za Sat Jan  5 09:14:16 2008'
import re
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
x = 'From stephen.marquard@utc.ac.za Sat Jan  5 09:14:16 2008'
import re
l = re.findall('@([^ ]*)',x)
print(l)
#| 使用位置          | 含义                        |
#| ------------- | ------------------------- |
#| `^` 在正则**开头** | 匹配“行的开始”位置（**行首符号**）      |
#| `^` 在 `[]` 中  | 表示“**取反**”，匹配**不在集合里的字符** |
