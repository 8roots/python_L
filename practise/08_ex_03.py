#原始代码
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
       words = line.split()
       # print('Debug:', words)
       if len(words) == 0 : continue
       if words[0] != 'From' : continue
       print(words[2])
'''使用带有单个 if 语句的 or 逻辑运算符的复合逻辑表达式，
重写上面示例中的守护代码，而不是使用两个 if 语句。'''
#修改版
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
       words = line.split()
       # print('Debug:', words)
       if len(words) == 0 or words[0] != 'From' :continue
       print(words[2])

#  ai版
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
       words = line.split()
       # print('Debug:', words)
       if len(words) == 0 or words[0] != 'From' or len(words) < 3:continue
       print(words[2])
       