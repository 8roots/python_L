'''
向09_ex_02的程序添加代码，以找出文件中谁的消息最多。
在读取所有数据并创建字典后，
使用最大值循环（参见第 5 章：最大值和最小值循环）遍历字典，
找出谁的消息最多，并打印该人有多少条消息。

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195

'''
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
# print(counts)
# c = counts.values()
# # print(c)
# da = max(c)
# print(da)
# largest = None
# print('Before:', largest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if largest is None or itervar > largest :
#         largest = itervar
#     print('Loop:', itervar, largest)
# print('Largest:', largest)
# largest_num = None
largest_num = 0
for itervar in counts:
    # print(itervar)
    Value = counts[itervar]
    if Value > largest_num :
        largest_num = Value
        # print('Loop:',itervar, largest_num)
        largest_itervar = itervar
print(largest_itervar,largest_num)
