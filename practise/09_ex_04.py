'''这个程序记录消息发送自的域名（而不是地址），而不是邮件来自谁（即完整的电子邮件地址）。
在程序结束时，打印出字典的内容。
示例行：
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

output:
python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}'''

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for line in fhand:  
    line = line.rstrip()
    if line.startswith('From '):
        line = line.split()
        if len(line) >= 2:  # 安全检查
            word = line[1]
            word = word.split('@')[-1] # 获取域名部分
            counts[word]=counts.get(word,0) + 1 # 简化计数逻辑
            # print(word)
            # print(line)
print(counts)