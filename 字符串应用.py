#字符串查找
str1 = 'aabbccddaaabbbcccddd'
print(str1.find("ddd"))
print(str1.count("a"))

#字符串替换 replace
print(str1.replace("a", "A"))
print(str1.replace("b", "B",3))

#正则表达式
import re
result = re.match("aa", str1)
print(result)

#捕获字符串
text = "johnsonfs0@outlook.com"    #匹配字母开头
pattern = r"(\w+)@(\w+)\.(\w+)"
match = re.match(pattern, text)
username = match.group(1)
domain = match.group(2)
print("Username:", username)
print("Domain:", domain)

text2 = "123abc def456"     #匹配数字开头
pattern2 = r'\d+'
match2 = re.match(pattern2, text2)
print(match2)

abc = "kelvin.cloud:114514"
cf = r"(\w+)\.(\w+)\:(\w+)"  #(\w+)表示字母，数字，符号等元素。
match3 = re.match(cf, abc)
print(match3.group(1))
print(match3.group(2))
print(match3.group(3))