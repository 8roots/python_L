'''
使用正则表达式解析 HTML

解析 HTML 的一种简单方法是使用正则表达式重复搜索和提取匹配特定模式的子字符串。

这是一个简单的网页：

<h1>The First Page</h1>
<p>
If you like, you can switch to the
<a href="http://www.dr-chuck.com/page2.htm">
Second Page</a>.
</p>

我们可以构建一个格式良好的正则表达式来匹配并从上述文本中提取链接值，如下所示：

href="http[s]?://.+?"

我们的正则表达式查找以 “href="http://"” 或 “href="https://”” 开头，后跟一个或多个字符 (.+?)，再后跟另一个双引号的字符串。[s]? 后面的问号表示搜索字符串“http”后跟零个或一个“s”。

添加到 .+? 的问号表示匹配应以“非贪婪”方式而不是“贪婪”方式进行。非贪婪匹配尝试找到最小可能匹配的字符串，而贪婪匹配尝试找到最大可能匹配的字符串。

我们在正则表达式中添加圆括号来指示我们想要提取匹配字符串的哪个部分，并生成以下程序：
'''

# 在 URL 输入中搜索链接值
import urllib.request, urllib.parse, urllib.error
import re
import ssl
# 忽略 SSL 证书错误
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
links = re.findall(b'href="(http[s]?://.*?)"', html)
for link in links:
    print(link.decode())

# 代码: https://www.py4e.com/code3/urlregex.py