'''练习 5：极简电子邮件客户端

MBOX（邮箱）是一种流行的文件格式，用于存储和共享电子邮件集合。
早期的电子邮件服务器和桌面应用程序使用这种格式。
不涉及太多细节，MBOX 是一个文本文件，它连续存储电子邮件。
电子邮件由以 From 开头的特殊行（注意空格）分隔。
重要的是，以 From: 开头的行（注意冒号）描述电子邮件本身，并不起分隔符的作用。
想象一下，你编写了一个极简的电子邮件应用程序，
它列出用户收件箱中发件人的电子邮件地址并计算电子邮件的数量。

编写一个程序，通读邮箱数据，当你找到以“From”开头的行时，
你将使用 split 函数将该行分割成单词。
我们感兴趣的是谁发送了消息，也就是 From 行上的第二个单词。

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

你将解析 From 行并为每个 From 行打印出第二个单词，
然后你还将计算 From（不是 From:）行的数量，并在最后打印出计数。'''
count = 0
fname = input('Enter a file name: ')


try:
    fhandle = open(fname)
except FileNotFoundError:
    print(f'没找到{fname}文件，请重新输入文件名')
    exit()#退出程序


for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    else:
        line = line.split()
        print(line[1])
        count += 1
print(f'There were {count} lines in the file with From as the first word')