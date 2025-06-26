import math
print(math)
#  ratio = signal_power / noise_power
#  decibels = 10 * math.log10(ratio)
#第一个例子计算信噪比的以 10 为底的对数。
#math 模块还提供了一个名为 log 的函数，用于计算以 e 为底的对数。
radians = 0.7
height = math.sin(radians)
print(height)
#变量名提示 sin 和其他三角函数（cos、tan 等）接受以弧度为单位的参数。
# 要从度转换为弧度，需除以 360 再乘以 2 π:
degrees = 45
radians = degrees / 360.0 * 2 * math.pi
#表达式 math.pi 从 math 模块中获取变量 pi。
# 该变量的值是 π 的近似值，精确到约 15 位数字。
print(math.sin(radians))






