import string

text = "Hello\\World!123"
translator = str.maketrans('', '', string.digits + string.punctuation)
cleaned = text.translate(translator)
print(cleaned)  # 输出什么？
print()
# 搜索在字符之间包含 @ 符号的行
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall(r'\S+@\S+', line)
    #这样设置，我们的一些电子邮件地址在开头或结尾有不正确的字符，如“<”或“;”
    if len(x) > 0:
        print(x)

# 代码: https://www.py4e.com/code3/re06.py
'''
为此，我们使用正则表达式的另一个特性。方括号用于指示我们愿意考虑匹配的一组多个可接受字符。从某种意义上说，\S 是要求匹配“非空白字符”的集合。现在我们将更明确地指定我们将匹配的字符。

这是我们的新正则表达式：

[a-zA-Z0-9]\S*@\S*[a-zA-Z]
'''
# 搜索在字符之间包含 @ 符号的行
# 字符必须是字母或数字
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        print(x)

# 代码: https://www.py4e.com/code3/re07.py
'''
这变得有点复杂了，你可以开始明白为什么正则表达式本身就是一门小语言了。
翻译这个正则表达式，我们正在寻找以单个小写字母、大写字母或数字“[a-zA-Z0-9]”开头，
后跟零个或多个非空白字符 (\S*)，再后跟一个 @ 符号，
再后跟零个或多个非空白字符 (\S*)，最后跟一个大写或小写字母的子字符串。
请注意，我们将 + 切换为 * 来表示零个或多个非空白字符，
因为 [a-zA-Z0-9] 已经是一个非空白字符。记住 * 或 + 应用于紧邻其左侧的单个字符。
如果我们在程序中使用这个表达式，我们的数据会干净得多：'''

