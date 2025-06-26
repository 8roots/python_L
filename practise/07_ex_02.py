'''
练习 3：
有时程序员感到无聊或想找点乐子时，他们会在程序中添加一个无害的彩蛋 (Easter Egg)。
修改提示用户输入文件名的程序，以便当用户输入确切的文件名“na na boo boo”时，打印一条有趣的消息。
对于所有其他存在和不存在的文件，程序应正常运行。以下是该程序的一个示例执行：

python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt

python egg.py
Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt

python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!

'''
fname = input('Enter the file name: ')
count = 0
date = 0


try:
    fhandle = open(fname)
# except FileNotFoundError:
#     print('文件未找到，请输入正确文件名')

except:
    if fname == 'na na boo boo':
        print ("NA NA BOO BOO TO YOU - You have been punk'd!")  
    else: 
        print(f'未找到{fname}文件，请输入正确文件名')
    exit()#exit 函数终止程序。它是我们调用的一个永不返回的函数。

for line in fhandle:
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        date = float(line[20: ]) + float(date)

average = date / float(count)
print(f'Average spam confidence:{average}\nSum is:{date}\ncounts is:{count}')