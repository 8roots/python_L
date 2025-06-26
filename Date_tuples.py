
t1 = (1, 2, 3)         # 常规写法
t2 = ()                # 空元组
t3 = (1,)              # 一个元素的元组，要加逗号！
t4 = tuple([1, 2, 3])  # 使用 tuple() 函数将列表转为元组
t = (3, 1, 2, 3)
print(len(t))     # 元素个数 -> 4
print(max(t))     # 最大值 -> 3
print(min(t))     # 最小值 -> 1
print(t.count(3)) # 3 出现了几次 -> 2
print(t.index(2)) # 元素 2 的索引位置 -> 2


def stats(x, y):
    return x + y, x * y

s = stats(2, 3)
print(s)        # 输出 (5, 6)
a, b = stats(2, 3)  # 元组解包
print(a)        # 输出 5
print(b)        # 输出 6


d = {'a': 1, 'b': 2}
for k, v in d.items():
    print((k, v))  # 每一项就是一个元组 ('a', 1)

coords = (3, 4)


print()
print()
print('将字典转变成元组')
#将字典转变成元组
d = {'name': 'Tom', 'age': 20}
v = d.items()#d.items() 返回一个 dict_items 对象（视图），是一个可迭代的键值对元组序列
print(v)
print(type(v))
m = tuple(v)#使用tuple转换为一个 包含多个元组的元组
print(m)
print()
print('将字典还原回来（从元组转换回字典）')
#将字典还原回来（从元组转换回字典）
new_dict = dict(m)
print(new_dict)
# 输出：{'name': 'Tom', 'age': 20}


print()
print()

d = {'name': 'Tom', 'age': 20}
n = max(d.items())
print(n)
print(type(n))
#为什么这个就直接变成了元组<class 'tuple'>

print()
print('按值排序字典，特别是在你想要从大到小排序')
#按值排序字典，特别是在你想要从大到小排序
d = {'a': 10, 'c' : 22, 'b':1}
tmp = list()
for k , v in d. items() :
    tmp.append((v,k))# 注意这里是 (value, key) # 值放前面，键放后面
    #d.items() 返回的是 (key, value)，你这里手动调换成 (value, key) 存入列表：
print(tmp)# 输出: [(10, 'a'), (22, 'c'), (1, 'b')]
tmp = sorted(tmp,reverse=True)#若设为 `True`，则降序排序（默认是升序）
print(tmp)# 输出: [(22, 'c'), (10, 'a'), (1, 'b')] — 按“值”从大到小排序
#把这个技巧用到一个实战中：比如“分析邮箱文件中哪个人发邮件最多”，效果非常明显

