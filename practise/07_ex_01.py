'''
练习 2： 编写一个程序，提示输入文件名，然后通读文件并查找以下形式的行：

X-DSPAM-Confidence: 0.8475

当你遇到以“X-DSPAM-Confidence:”开头的行时，解析该行以提取行上的浮点数。
计算这些行的数量，然后计算这些行的垃圾邮件置信度值的总和。
当你到达文件末尾时，打印出平均垃圾邮件置信度。

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745

Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519

在 mbox.txt 和 mbox-short.txt 文件上测试你的文件。
'''
# f = 'X-DSPAM-Confidence: 0.8475'
# print(f.find(' '))
# print(f[20:])

fname = input('Enter the file name: ')
count = 0
date = 0


try:
    fhandle = open(fname)
# except FileNotFoundError:
#     print('文件未找到，请输入正确文件名')
except:
    print(f'未找到{fname}文件，请输入正确文件名')
    exit()#exit 函数终止程序。它是我们调用的一个永不返回的函数。


for line in fhandle:
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        date = float(line[20: ]) + float(date)


average = date / float(count)
print(f'Average spam confidence:{average}\nSum is:{date}\ncounts is:{count}')
