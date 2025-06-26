import re               #导入正则表达式模块，用于提取特定格式的文本
hand = open('mbox-short.txt')# 打开文件 mbox-short.txt，返回文件句柄
numlist = list()        # 创建一个空列表，用于存储提取出的浮点数
for line in hand:       # 遍历文件中的每一行
    line = line.rstrip() # 去除行末的换行符和多余空格
    stuff = re.findall('X-DSPAM-Confidence: ([0-9.]+)',line)
     # 使用正则表达式查找形如 'X-DSPAM-Confidence: 0.8475' 的行
     # # 提取冒号后面的数字（整数或小数），返回一个列表
    #找到以X-DSPAM -Confidence:开头的行,提取中间0-9内出现的数字,并返回到stuff为列表
    if len(stuff) != 1 : continue # 如果没有找到匹配项（即列表为空或多个匹配），跳过本行
    #如果列表stuff里的元素量不等于1,那就回到for循环,继续遍历下一行,直到符合条件才进入下一行
    num= float(stuff[0])# 将匹配到的字符串（第一个元素）转换为浮点数
    numlist.append(num) #将数字加入numlist列表
print('Maxium: ', max(numlist))# 输出列表中的最大值，即最大置信度


