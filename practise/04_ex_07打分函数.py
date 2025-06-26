def computegrade(score):
    if score < 0 or score > 1:
        return 'Error: 请输入0.0到1.0之间的数字'
    elif score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'        
    elif score >= 0.6:
        return 'D'
    else:
        return 'F'
    # 函数只负责计算，不负责输出
    #输入输出由主程序处理
    #
try:
    s = float(input('Enter Score: '))
    
    result = computegrade(s)
    print(f'Grade: {result}')
    
except ValueError:
    print(f'error,please input numbers')










