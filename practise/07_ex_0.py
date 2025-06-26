'''
练习 1： 编写一个程序，通读一个文件并以全大写形式打印文件的内容（逐行）。执行该程序将如下所示：

python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
     BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
     SAT, 05 JAN 2008 09:14:16 -0500
'''
fname = input('Enter a file name: ')
#fhandle = open(fname, 'r', encoding='utf-8')
fhandle = open(fname,'r')
for line in fhandle :
    line = line.upper()
    str = line.rstrip()
    print(str)

'''
fname = input('Enter a file name: ')

try:
    # 显式使用 'r' 并指定编码
    with open(fname, 'r', encoding='utf-8') as fhandle:
        for line in fhandle:
            line = line.upper()
            clean_line = line.rstrip()  # 避免使用 str 作为变量名（覆盖内置函数）
            print(clean_line)
            
except FileNotFoundError:
    print(f"错误：文件 {fname} 不存在")
except UnicodeDecodeError:
    print("错误：文件编码不兼容，请尝试其他编码")
'''