name = 'adva lavas'

# 友好的问候语（首字母大写）
greeting = f"Hello {name.title()}, would you like to learn some Python today?"
print(greeting)

# 大小写转换演示
print(f"Lowercase: {name.lower()}")
print(f"Uppercase: {name.upper()}")
print(f"Title Case: {name.title()}")
# 示例1：移除特定后缀
file1 = "data.csv"
print(file1.removesuffix(".csv"))  # 输出: "data"

# 示例2：后缀不匹配时返回原字符串
file2 = "image.png"
print(file2.removesuffix(".jpg"))  # 输出: "image.png"（未修改）

# 示例3：链式调用
path = "config.backup.yaml"
print(path.removesuffix(".yaml").removesuffix(".backup"))  # 输出: "config"