'''
练习 3： 编写一个程序，读取一个文件并按频率降序打印其中的字母。

你的程序应将所有输入转换为小写，并且只计算字母 a-z。
你的程序不应计算空格、数字、标点符号或除字母 a-z 之外的任何其他内容。
查找来自几种不同语言的文本样本，看看字母频率在不同语言之间有何不同。
将你的结果与 https://wikipedia.org/wiki/Letter_frequencies 上的表格进行比较。
'''
import string
fname = input('输入文件名：')
try:
    fhand = open(fname)
except FileNotFoundError:
    print(fname,'文件未找到')
    exit()#总是忘记输入exit()

lst= dict()
for lines in fhand:
    lines = lines.lower()
    lines = lines.translate(lines.maketrans('','', string.digits + string.punctuation + string.whitespace ))

    if len(lines) >= 1 :
        for letter in lines:
            lst[letter] = lst.get(letter,0) + 1

sec = list(lst.items())
sec.sort(reverse=False)
for key,val in sec:
    print(key ,val)
'''
import string

fname = input('输入文件名：')
try:
    fhand = open(fname)
except FileNotFoundError:
    print(fname, '文件未找到')
    exit(1)

lst = dict()
for line in fhand:
    line = line.lower()
    line = line.translate(str.maketrans('', '', string.digits + string.punctuation + string.whitespace))
    for letter in line:
        lst[letter] = lst.get(letter, 0) + 1

if not lst:
    print('文件中没有字母可统计')
else:
    sec = list(lst.items())
    sec.sort(key=lambda x: x[0])  # 按字母顺序
    # sec.sort(key=lambda x: x[1], reverse=True)  # 如果想按频率排序，用这行

    for key, val in sec:
        print(key, val)

'''