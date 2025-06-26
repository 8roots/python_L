
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()
print(id(print_lyrics))
print(print_lyrics.__name__)
#身份（Identity）：每个对象在内存中都有唯一的地址（通过id()获取）。
# 代码: https://www.py4e.com/code3/lyrics.py