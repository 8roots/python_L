
# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#        words = line.split()
#        # print('Debug:', words)
#        if len(words) == 0 : continue
#        if words[0] != 'From' : continue
#        print(words[2])

'''
       找出上面程序中哪一行仍然没有得到适当的守护。
       看看你是否可以构造一个导致程序失败的文本文件，
       然后修改程序，使该行得到适当的守护，并对其进行测试，
       以确保它能处理你的新文本文件。
'''

'''
文件1的内容:

From: sdsijks, cbf
From+2 323@er  ere hgh

From- : sdsij  ks
'''

#下面这个是我改写的代码内容，但是不能解决文件1的问题，为什么
fhand = open('1.txt')
count = 0
for line in fhand:
       words = line.split()
       print('Debug:', words)
       if len(words) == 0 : continue
       if words[0] != '\S+From\S+' : continue
       print(words[2])

'''    正则表达式使用错误：

        你使用了 if words[0] != '\S+From\S+'，但在普通字符串比较中，这不会被视为正则表达式

        Python 需要 re 模块才能使用正则表达式

        即使使用正则，\S+From\S+ 匹配的是"任意非空白字符+From+任意非空白字符"，而你需要匹配的是以"From"开头的行

    核心问题未解决：

        原始代码的问题是：当一行以"From"开头但单词数不足3个时，访问 words[2] 会导致索引错误

        你的修改没有解决这个核心问题'''

# ai 答复
fhand = open('1.txt', 'r')  # 明确指定读取模式
for line in fhand:
    words = line.split()
    print('Debug:', words)
    
    # 跳过空行
    if len(words) == 0:
        continue
    
    # 检查是否以"From"开头（不区分大小写）
    if words[0].startswith('From'):
        # 核心修复：确保有足够的元素再访问words[2]
        if len(words) >= 3:
            print(words[2])
        else:
            print(f"警告：此行以'From'开头但元素不足: {line.strip()}")