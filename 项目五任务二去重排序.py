def fg(text):
    words = text.split()
    unique_words = []
    seen = set()    
    for word in words:
        if word not in seen:
            seen.add(word)
            unique_words.append(word)
    sorted_words = sorted(unique_words)    
    return sorted_words

input_string = "hello world and practice makes perfect and hello world again"
result = fg(input_string)

print("原始字符串:", input_string)
print("去重排序后的单词列表:", result)
print("去重排序后的字符串:", " ".join(result))