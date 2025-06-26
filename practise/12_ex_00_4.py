import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)  # 每次最多读取100KB
    if len(info) < 1: break  # 数据读取完毕时退出循环
    size = size + len(info)  # 累计字节数
    fhand.write(info)        # 写入当前数据块

print(size, 'characters copied.')
fhand.close()

# 代码: https://www.py4e.com/code3/curl2.py