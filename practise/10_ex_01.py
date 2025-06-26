'''
练习 1: 修改之前的程序如下:读取并解析“From”行, 并从行中提取地址。
使用字典计算来自每个人的消息数量。
示例行：
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

输入文件名: mbox-short.txt
cwen@iupui.edu 5

输入文件名: mbox.txt
zqian@umich.edu 195
在读取所有数据后，通过从字典创建 (count, email) 元组列表来打印提交次数最多的人。
然后按逆序对列表进行排序，并打印出提交次数最多的人。'''
fname = input('输入文件名: ')
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
        if len(line) >= 2:  # 确保有足够的元素
            word = line[1]# 直接获取完整邮箱
            counts[word]=counts.get(word,0) + 1# 简化计数逻辑


'''
lst = []
for key, val in counts.items():
    lst.append((val, key))  # 把(次数,邮箱)存入列表
lst.sort(reverse=True)  # 按次数降序排序
m = lst[0]  # 取第一个（次数最多的）
print(m[1], m[0])  # 输出邮箱和次数

问题：

    不必要的排序：你只需要最大值，完整排序浪费资源

    变量名不清晰：m, lst 不能直观表达含义

    缺少空字典检查：如果 counts 为空，lst[0] 会报错
'''
# 2. 找出出现次数最多的邮箱（不用max+lambda）
if counts:  # 如果字典不是空的
    max_count = -1  # 初始化最大次数
    most_common_email = None  # 初始化最常出现的邮箱
    
    # 遍历字典，手动找最大值
    for email, count in counts.items():
        if count > max_count:
            max_count = count
            most_common_email = email
        '''逻辑：遍历字典，记录当前遇到的最大值和对应的邮箱
            相当于：用 for 循环实现了 max() 的功能''' 
        
    # 3. 打印结果
    print("出现最频繁的邮箱:", most_common_email)
    print("出现次数:", max_count)
else:
    print("文件中没有有效的From行")

'''
fname = input('输入文件名: ')
try:
    with open(fname) as fhand:  # 使用with自动关闭文件
        counts = dict()
        
        for line in fhand:
            line = line.rstrip()
            if line.startswith('From '):
                parts = line.split()
                if len(parts) >= 2:  # 必要的安全检查
                    email = parts[1]
                    counts[email] = counts.get(email, 0) + 1

        if counts:  # 检查字典是否为空
            # 直接使用max函数找出出现次数最多的邮箱
            most_common = max(counts.items(), key=lambda item: item[1])
            print(f"最多出现的邮箱: {most_common[0]}, 出现次数: {most_common[1]}")
        else:
            print("文件中没有找到有效的From行")

except FileNotFoundError:
    print('文件无法打开:', fname)
    exit()
'''

'''具体改进说明

    文件操作改进：

        使用 with 语句自动处理文件关闭

        避免忘记关闭文件导致资源泄露

    安全增强：

        保留必要的 len(parts) >= 2 检查

        添加了 if counts 检查字典是否为空

    优化查找逻辑：

        使用 max() 函数直接找出最大值

        避免不必要的完整排序

        key=lambda item: item[1] 指定按值(出现次数)比较

    输出更友好：

        使用f-string格式化输出

        变量名更有意义(most_common)

    错误处理完善：

        处理了文件不存在的情况

        处理了没有有效From行的情况

为什么原始代码可能有误？

    如果文件没有有效的From行，lst 会是空列表，lst[0] 会引发 IndexError

    如果有多邮箱出现次数相同且都是最大值，你的代码只会返回其中一个

    变量名 m, x, y 让代码难以理解

最佳实践建议

    总是检查可能引发异常的情况

    使用更有意义的变量名

    优先使用Python内置函数 (如max) 替代手动实现

    使用with语句处理文件

    考虑所有可能的边界情况 (空文件、格式不正确的行等)

这样修改后，代码更健壮、更易读，也能正确处理各种边界情况。'''