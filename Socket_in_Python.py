import socket

# 创建 socket 对象，使用 IPv4 和 TCP
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器（域名/IP，端口号）
mysock.connect(('data.pr4e.org', 80))

# 构造 HTTP 请求命令（注意结尾必须有 \r\n\r\n）
cmd = 'GET /romeo.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'
mysock.send(cmd.encode())  # 编码成字节流发送

# 接收并打印数据
while True:
    data = mysock.recv(512)  # 每次接收 512 字节
    if len(data) < 1:
        break
    print(data.decode(), end='')  # 解码并输出

# 关闭 socket
mysock.close()
