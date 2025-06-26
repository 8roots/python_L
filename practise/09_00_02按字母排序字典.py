counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    print(key, counts[key])
print()  
print()


#我们可以使用这种模式来实现我们之前描述的各种循环惯用法。
#例如，如果我们想在字典中找到所有值大于十的条目
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10 :
        print(key, counts[key])

print()
print()

#如果你想按字母顺序打印键，你首先使用字典对象中可用的 keys 方法创建一个字典键的列表，
# 然后对该列表进行排序并遍历排序后的列表，查找每个键并按排序顺序打印出键值对，如下所示：
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
lst = list(counts.keys())
print(lst)
lst.sort()
print(lst)
for key in lst:
    print(key, counts[key])    
# 首先你看到我们从 keys 方法得到的非字母顺序的键列表。
# 然后我们看到 for 循环产生的按字母顺序排列的键值对。  