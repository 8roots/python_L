# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     count = count + 1
#     print(line.rstrip())#line变量是迭代文件每一行，包括行末的换行符\n
# print('Line Count:', count)

# 代码: https://www.py4e.com/code3/open.py
'''
import dis
dis.dis('x = 1 + 2')  # 显示简单表达式的字节码
print()
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    # 跳过 '不有趣的行'
    if not line.startswith('From:'):
        continue
    # 处理我们 '有趣的' 行
    else:
        count = count + 1  
    print(line)
print('Line Count:', count)'''

# 代码: https://www.py4e.com/code3/search3.py
'''
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()#exit 函数终止程序。它是我们调用的一个永不返回的函数。
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
'''
# 代码: https://www.py4e.com/code3/search7.py
#任何软件开发团队的一个重要组成部分是一个称为质量保证（Quality Assurance，简称 QA）的人员或小组，他们的工作就是做尽可能疯狂的事情，试图破坏程序员创建的软件。
# 代码: https://www.py4e.com/code3/search6.py
'''
追求“更 Pythonic”的目标体现了编程既是工程学也是艺术的概念。
我们并不总是只对让某事能够工作感兴趣，我们也希望我们的解决方案是优雅的，并被我们的同行认为是优雅的。'''



#output.txt文件的原内容是：a person of focus commitment sheer will !
# 打开文件（自动清空原内容）
fout = open('output.txt', 'w')

# 写入内容
line1 = "This here's the wattle,\n"
z = fout.write(line1)  # z会返回写入的字符数（这里是23）

# 必须关闭文件才能确保写入完成
fout.close()

# 验证写入结果
with open('output.txt') as f:
    print(f.read())  # 输出: This here's the wattle,
