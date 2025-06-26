x = list()
x.append('book')
x.append(99)
print(x)

a = [1,2,5,8,4,576,55]
a.sort()
print(a)
b = ['Jason','Glean','Slly']#不能比较字符串与浮点数
#not supported between instances of 'int' and 'str'
b.sort()
print(b)

print(len(a))
print(max(a))
print(min(a))
print(sum(a))
print(sum(a)/len(a))