'''
练习 1： 编写一个名为 chop 的函数，它接受一个列表并修改它，移除第一个和最后一个元素，并返回 None。
然后编写一个名为 middle 的函数，它接受一个列表并返回一个新列表，其中包含除第一个和最后一个元素之外的所有元素。
'''
def chop(lie):
    
    del lie[0]
    del lie[-1]
    return None

def middle(li):
    return li[1:-1]

