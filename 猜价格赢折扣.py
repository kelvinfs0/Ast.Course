import random
def main():
	mb = random.randint(1, 100)
	cishu = 0
	print("=== 猜价格赢折扣 ===")
	print("系统已生成 1~100 之间的价格，猜中有奖。输入end可退出。")

	while True:
		sr_str = input("请输入你的猜测: ").strip()
		if sr_str.lower() == "end":
			print("已退出游戏。")
			return
		if not sr_str.isdigit():
			print("请输入 1~100 的整数，或 end 退出。")
			continue
		sr = int(sr_str)
		if not 1 <= sr <= 100:
			print("范围超出，请输入 1~100 的整数。")
			continue
		cishu += 1
		if sr == mb:
			print(f"猜对了！价格就是 {mb}。共猜了 {cishu} 次。")
			print(get_discount(cishu))
			break
		elif sr < mb:
			print("偏小了，再试试~")
		else:
			print("偏大了，再试试~")
def get_discount(attempts: int) -> str:
	if attempts <= 3:
		return "恭喜获得 5 折优惠券！"
	if attempts <= 6:
		return "恭喜获得 8 折优惠券！"
	return "获得 95 折优惠券，加油再接再厉！"


if __name__ == "__main__":
	main()
