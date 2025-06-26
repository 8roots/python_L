'''编写一个程序，通读邮件日志，使用字典构建一个直方图，
以计算来自每个电子邮件地址的消息数量，并打印该字典。'''
'''
Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}'''
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
        line = line.split()
        email_adress = line[1]
        if email_adress  not in counts:
            counts[email_adress]= counts.get(email_adress,0) + 1
        else:
            counts[email_adress] += 1
print(counts)

