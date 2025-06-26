str = 'X-DSPAM-Confidence: 0.8475'
x = str.find(':')
c = str[x+2:]
v = float(c)
print(v)
print(type(v))
'''获取以下存储字符串的 Python 代码：

str = 'X-DSPAM-Confidence: 0.8475'

使用 find 和字符串切片提取冒号字符之后的部分字符串，然后使用 float 函数将提取的字符串转换为浮点数。'''
print("The sum of 1 + 2 is {0}".format(1+2))
print("{0} + {1} = {2}".format(1, 2, 1+2))
'''    format(1+2) 只传入 一个参数（即 3）。

    {0} 表示 第一个参数（索引从 0 开始）。

    如果写成 {1}，会报错，因为 .format() 只传入了 1 个参数，而 {1} 试图访问第 2 个参数（不存在）。'''