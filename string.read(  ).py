fhand = open('mbox-short.txt')
inp = fhand.read()#如果你知道文件相对于你的主内存大小来说比较小，
#你可以使用文件句柄上的 read 方法将整个文件读入一个字符串中。
print(len(inp))
94626
print(inp[:20])#使用字符串切片打印出存储在 inp 中的字符串数据的前 20 个字符
print(type(inp))

#请记住，只有当文件数据能够舒适地容纳在你计算机的主内存中时，才应使用这种形式的 open 函数。
#如果文件太大而无法放入主内存，你应该编写程序使用 for 或 while 循环分块读取文件。