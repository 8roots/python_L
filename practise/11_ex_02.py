'''练习 2： 编写一个程序来查找以下形式的行：

New Revision: 39772

使用正则表达式和 findall() 方法从每行中提取数字。计算这些数字的平均值，并将平均值打印为整数。

输入文件:mbox.txt
38549

输入文件:mbox-short.txt
39756

'''
# import re
# try:
#     filename = input('输入文件：')
# except FileNotFoundError:
#     print('FileNotFound')
#     exit()

# file = open(filename,encoding='utf-8') 
# list = []
# for line in file:
#     lst = re.findall(r'\d+',line)
# print(lst)


import re

filename = input('输入文件：')
numbers = []  # 避免使用list作为变量名  

try:
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # 匹配所有数字（包括小数和负数）
            matches = re.findall(r'^N.*:\s(\d+\.?\d*)', line)
            numbers.extend(matches)  # 将每行的结果添加到总列表中
except FileNotFoundError:
    print(f'错误：文件 {filename} 未找到')
    exit()
except UnicodeDecodeError:
    print('错误：文件编码问题，尝试其他编码')
    exit()

print('找到的数字：', numbers)
sum_numbers= []
for n in numbers:
    n = int (n)
    sum_numbers.append(n)

sum_numbers = sum(sum_numbers)
print(sum_numbers)

length_numbers = len(numbers)
print(length_numbers)

average_numbers = sum_numbers / length_numbers
print(int(average_numbers))