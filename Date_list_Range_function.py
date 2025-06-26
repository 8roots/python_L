print(range(4))#range(n) 生成一个从 0 到 n-1 的序列，但它是个 range对象。
#这是因为 range(4) 本身是一个 可迭代对象（range对象），并不是直接的列表。

#如果你想看到它的实际数字，你需要把它转成列表，比如：
print(list(range(4)))
# 输出: [0, 1, 2, 3]
friends = ['a','b','c']
print(len(friends))
print(list(range(len(friends))))
#list() 是一个 类型转换函数，
# 它的作用是把一个可迭代对象
# （如 range、str、tuple、set 等）转换成一个 列表（list）。
#list("abc") → ['a', 'b', 'c']
#list((1, 2, 3)) → [1, 2, 3]
#list({4, 5, 6}) → [4, 5, 6]（注意：集合无序）


#直接遍历打印型
#明了
friends = ['a','b','c']
for friend in friends :
    print('happy new year: ', friend)
    
#间接遍历打印型
friends = ['a','b','c']
for i in range(len(friends)):
    friend = friends[i]#按range返回的位置数值一次索引并传递列表里元素值到friend里
    print('happy new year: ', friend)
    
