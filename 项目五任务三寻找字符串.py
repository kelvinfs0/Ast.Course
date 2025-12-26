fruits = ("apple", "banana", "cherry", "blackberry","almond","blueberry","carambola","durian","grape","grapefruit","lichee")
dc = ""
cd = 0
cda = 0
for dc in fruits:
    cd = len(dc)
    if cd >= cda:
        cda = cd
        name = dc
print(f"名字最长的元素是：{name}")