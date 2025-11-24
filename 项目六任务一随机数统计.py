import random

# 生成1000个随机整数
random_numbers = [random.randint(1, 100) for _ in range(1000)]
print("1000个随机数已生成")
chose = input("是否打印生成的随机数列表？(y/n): ")
if chose.lower() == 'y':
    print("生成的随机数列表:", random_numbers)

# 统计出现频率
frequency = {}
for num in random_numbers:
    frequency[num] = frequency.get(num, 0) + 1
print("随机数出现的频率:")
for num, freq in frequency.items():
    print(f"数字 {num} 出现了 {freq} 次")