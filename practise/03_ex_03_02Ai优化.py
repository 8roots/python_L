while True:
    try:
        score = float(input('Enter Grade (0.0-1.0): '))
        
        if score < 0.0 or score > 1.0:
            print('Out of range. Please enter a value between 0.0 and 1.0')
            continue  # 跳过后续代码，重新开始循环
            
        # 等级判断
        if score >= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')  
        elif score >= 0.6:
            print('D')
        else:
            print('F')
            
        # 添加退出选项
        another = input("Convert another? (y/n): ").lower()
        if another != 'y':
            break  # 退出循环
            
    except ValueError:
        print('Error: Please enter a valid number')