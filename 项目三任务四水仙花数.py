print("水仙花数：")
ws = int(input("请输入水仙花数的位数："))
sxh = []
for n in range(3, ws + 1):
    start = 10**(n-1)
    end = 10**n
        
    for num in range(start, end):
        # 计算各位数字的n次幂之和
        digits = [int(d) for d in str(num)]
        power_sum = sum(d**n for d in digits)
            
        if power_sum == num:
            sxh.append(num)
            # 显示计算过程
            expression = " + ".join([f"{d}^{n}" for d in digits])
            print(f"{num} = {expression}")
    
print(f"\n总共找到 {len(sxh)} 个水仙花数：")
print(sxh)