try:
    celsius = float(input("请输入摄氏温度: "))          # 提示用户输入摄氏温度
    fahrenheit = (celsius * 9/5) + 32                  # 转换公式：华氏温度 = (摄氏温度 × 9/5) + 32
    print(f"{celsius} 摄氏度 = {fahrenheit:.2f} 华氏度")# 打印转换结果（保留2位小数）
except ValueError:
    print("错误：请输入有效的数字")
    
#程序说明：

#    输入处理：
#        使用 input() 获取用户输入
#        用 float() 将输入字符串转换为浮点数（支持小数输入）

#    转换公式：
#        华氏温度 = (摄氏温度 × 9/5) + 32
#        示例：0°C → (0 × 1.8) + 32 = 32°F

#    输出格式化：
#        使用 f-string 格式化输出
#        :.2f 表示保留2位小数