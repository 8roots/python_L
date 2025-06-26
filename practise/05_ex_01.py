#编写一个程序，重复读取整数，直到用户输入“done”。一旦输入“done”，打印出整数的总和、计数和平均值。
#如果用户输入的不是整数，使用 try 和 except 检测他们的错误，打印错误消息，并跳到下一个整数。
#Enter a number: 4
#Enter a number: 5
#Enter a number: bad data
#Invalid input
#Enter a number: 7
#Enter a number: done
#16 3 5.333333333333333
#1先选择while循环
#2  try 主体  except valueerror： print('Enter a number: bad data') 然后continue，回到while
line = []## 在循环外部初始化列表
print('KeyboardInt')
while True:
    
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        zs = int(num)
        line.append(zs)# 将有效数字添加到列表中
    except ValueError:
        print('Invalid input')
        continue  

if line:  # 确保列表不为空
    print(sum(line), len(line), sum(line)/len(line))
else:
    print('No numbers were entered.')

'''
主要修正点：

    列表初始化位置：

        你的代码中 line = [] 放在循环内部，每次循环都会重置列表

        应该将列表初始化放在循环外部

    输入处理顺序：

        应该先检查是否是 'done'，再尝试转换为整数

        这样可以避免对 'done' 进行不必要的转换尝试

    列表操作：

        line = line.append(int(num)) 是错误的，因为 append() 方法返回 None

        应该直接使用 numbers.append(num)

    结果计算时机：

        应该在检测到 'done' 后立即计算结果并退出

        你的代码中打印的是 len(line) 而不是要求的三个统计量

    空输入处理：

        添加了对空列表的检查，避免除零错误

代码执行流程：

    初始化空列表 numbers

    进入无限循环

    获取用户输入

    如果是 'done'，计算并输出结果，然后退出

    如果不是 'done'，尝试转换为整数

        成功则添加到列表

        失败则提示错误并继续循环

    重复步骤3-5
'''