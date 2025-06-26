'''
编写一个程序 根据提交是在星期几对每封邮件消息进行分类。
为此 查找以“From”开头的行 然后查找第三个单词 并对每周的每一天进行运行计数。
在程序结束时打印出字典的内容（顺序无关紧要）。
示例行：
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
示例执行：
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}'''
import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    
    if line.startswith('From '):
        words = line.split() 
        # print(words)
        word = words[2]
        
        if  word not in counts:
            counts[word] = counts.get(word,0) + 1
        else:
            counts[word] += 1

print(counts)