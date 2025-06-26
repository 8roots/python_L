'''练习 6

重写提示用户输入数字列表
并在用户输入“done”时最后打印出数字的最大值和最小值的程序。
编写程序将用户输入的数字存储在列表中，
并在循环完成后使用 max() 和 min() 函数计算最大值和最小值。'''
date = []

# a = input('Enter numbers or done:')
# f = int(a)
# f = input('Enter numbers or done:')


while True:
    f = input('Enter numbers or done:')
    # try:
    #     a = input('Enter numbers or done:')
    #     f = int(a)
    # except ValueError:
    #     print('wrong input')
    #     continue
    # date.append(f)
    if f == 'done':
        M = max(date)
        MI = min(date)
        print(f'MAX: {M},MIN: {MI}')
        break
    # elif f == ' ':
    #     not date.append(f)
    else:
        date.append(f)
'''为什么你的原始代码有问题：

    你在循环外预先获取了一次输入，但没处理这个输入

    直接将字符串添加到列表中，没有转换为数字

    缺少错误处理，当用户输入非数字时会崩溃

    没有处理空列表的情况，如果直接输入"done"会出错'''  
#AI版本
numbers = []

while True:
    user_input = input('Enter a number or "done": ')
    if user_input == 'done':
        if numbers:  # 确保列表不为空
            print(f'MAX: {max(numbers)}, MIN: {min(numbers)}')
        else:
            print('No numbers entered.')
        break
    try:
        num = float(user_input)  # 使用float可以处理整数和小数
        numbers.append(num)
    except ValueError:
        print('Invalid input. Please enter a number or "done".')

# 主要修改点：
#     输入处理：
#         将输入直接存储在user_input中，不需要预先定义
#         使用float()而不是int()可以同时处理整数和小数

#     错误处理：
#         添加了try-except块来捕获非数字输入
#         当输入无效时会提示用户重新输入

#     空列表检查：
#         在计算max和min前检查列表是否为空，避免运行时错误

#     变量命名：
#         使用更有意义的变量名numbers代替date
#         使用user_input代替f使代码更易读

#     用户提示：
#         修改提示信息更清晰明确

    
