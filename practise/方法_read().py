with open('clown.txt', 'rb') as file:
    content = file.read()  # 返回bytes
    print(content)
print()
print('打开文本文件（默认文本模式）')
# 打开文本文件（默认文本模式）
with open('clown.txt', 'r', encoding='utf-8') as file:
    # 读取整个文件内容
    full_content = file.read()
    print(f"类型: {type(full_content)}")  # <class 'str'>
    print(f"内容:\n{full_content}")
    
    # 重置文件指针到开头
    file.seek(0)
    
    # 读取前100个字符
    partial_content = file.read(100)
    print(f"前100个字符:\n{partial_content}")
print()
print('打开二进制文件')
    # 打开二进制文件
with open('cover3.jpg', 'rb') as file:
    # 读取整个文件内容
    image_data = file.read()
    print(f"类型: {type(image_data)}")  # <class 'bytes'>
    print(f"数据长度: {len(image_data)} 字节")
    
    # 重置文件指针到开头
    file.seek(0)
    
    # 读取文件头（前8字节）
    header = file.read(8)
    print(f"文件头: {header}")