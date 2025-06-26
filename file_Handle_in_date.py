#仅打开文件并显示文件对象信息，
# 若要读取文件内容，应该使用 for 循环逐行读取。
file_hand = open('mbox-short.txt')
print(file_hand)

#使用 for 循环,逐行读取文件并打印内容
file_hand = open('mbox-short.txt')
for line in file_hand:
    print(line)

#将整个文件读取成一个字符串并打印
fhand = open('mbox-short.txt')
a = fhand.read()
print(a)
print(len(a))#输出的是文件内容的字符长度（即所有字符的总数）
print(a[:20])#输出文件内容的前20个字符。

#统计文件的行数
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
	count += 1
print ('Line Count:',count)

#定向显示以From开头的内容
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()# 去掉每行末尾的换行符
    if line.startswith('From'):
        print(line)
        
#定向显示以From开头的内容_其他写法
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()# 去掉每行末尾的换行符
    if not line.startswith('From'):# 如果行不以'From'开头,当条件成立时,continue被触发
         continue## 跳过当前行循环，回到上头的for循环,进入下一行循环。
    print(line)# 只有行以 'From' 开头时才会打印

    #if not line.startswith('From'): 检查当前行是否不以 'From' 为开头。
    # 如果是，则 continue 跳过该行，进入下一次循环。
    #在 for 或 while 循环中，continue 会跳过当前循环体中剩余的代码，直接进入下一次循环。
    #continue 仅影响当前循环中的剩余部分，而不会结束整个循环。
    #not 用来 反转条件，使得你可以测试某个条件的反面。
    #两者的输出结果是相同的，主要差异在于控制流的写法。
    # continue 可以让代码的逻辑更简洁和直观，避免嵌套过多。
    #这两者配合使用时，可以让代码逻辑更简洁、清晰。

#使用in来挑选文件里符合条件的行
fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if not '@ut.ca.cza' in line :
		continue
	print(line)


#自由选择读取不同的文件
#将文件名作为参数,输入,并传递给open函数
#查询出在文件中有多少以 Subject 开头的文件行数     
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
      if line.startswith('Subject:') :
            count += 1
print('There were ', count, 'subjectlines in',fname)


#自由选择读取不同的文件_优化写法
# 输入错误的文件名时
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
      print('File cannot opened: ' ,fname)# 如果文件无法打开（如文件不存在），执行这里
      quit()# 终止程序
count = 0
for line in fhand:
      if line.startswith('Subject:') :
            count += 1
print('There were ', count, 'subjectlines in',fname)

#try 块：
    #try 语句块包含可能会引发异常（错误）的代码。
    # 如果 try 中的代码执行时发生了异常，程序会跳转到 except 块，
    # 执行 except 中的代码。
#except 块：
    #如果在 try 块中发生了异常，程序会转到对应的 except 块执行。
    # except 可以指定处理特定类型的错误，也可以使用 except 来捕捉所有异常。