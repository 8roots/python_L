while True:

    try:
        score = float(input('Enter Grade: '))
        if score < 0.0 or score >1.0 :
            print('Bad score')
        elif score >= 0.9 :
            print('A')
        elif score >= 0.8 :
            print('B')
        elif score >= 0.7 :
            print('C')  
        elif score >= 0.6 :
            print('D')
        else :
            print('F')
            
        another = input("Convert another? (y/n): ").lower()
        if another != 'y':
            break  # 退出循环
    except ValueError:
        print('Bad score')

#Ai优化后：


#Score   Grade
#>= 0.9     A
#>= 0.8     B
#>= 0.7     C
#>= 0.6     D
# < 0.6     F
