# 要运行此程序，请下载 BeautifulSoup zip 文件
# http://www.py4e.com/code3/bs4.zip
# 并在与此文件相同的目录中解压缩

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# 忽略 SSL 证书错误
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# 检索所有锚点标签
tags = soup('a')
for tag in tags:
    # 查看标签的各个部分
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)

# 代码: https://www.py4e.com/code3/urllink2.py
