#编写一个 while 循环，从字符串的最后一个字符开始，反向工作到字符串的第一个字符，将每个字母打印在单独的行上，但是是反向的。

count = 0
fruit = 'banana'
length = len(fruit)#  6
while True:
    length = length -1
    last = fruit[length]# 5
    print(last)    
    if length ==0:
        break

# fruit = 'banana'
# length = len(fruit)

# while True:
#     length -= 1#54321
#     print(fruit[length])
#     if length == 0:
#         break
print()

for char in fruit:
    print(char)
print()
print(fruit[:])
print()
print()
