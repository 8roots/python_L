'''练习 1： 更改套接字程序 socket1.py，使其提示用户输入 URL，以便它可以读取任何网页。

你可以使用 split('/') 将 URL 分解为其组成部分，以便为套接字 connect 调用提取主机名。
使用 try 和 except 添加错误检查，以处理用户输入格式不正确或不存在的 URL 的情况。'''

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

# 代码: https://www.py4e.com/code3/socket1.py
