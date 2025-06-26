#第一种写法,不知道列表,不使用列表方法库
total = 0
count = 0
while True :
    inp = input('输入一个数字: ')
    if inp == 'done' : break
    value = float(inp)
    total = total+value
    count = count+1
average = total / count
print('Average: ' ,average)

#知晓列表,应用列表,应用sum()&len()
#列表能存储输入
#使用更多内存
numlist = list()
while True :
    inp = input('输入一个数字: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average: ' ,average)