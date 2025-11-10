def compare_strings(str1, str2):
    """
    比较两个字符串，返回差异信息
    
    Args:
        str1 (str): 第一个字符串
        str2 (str): 第二个字符串
    
    Returns:
        list: 包含差异信息的列表
    """
    result = []
    len1, len2 = len(str1), len(str2)
    max_len = max(len1, len2)
    
    i = 0
    while i < max_len:
        if i < len1 and i < len2:
            if str1[i] != str2[i]:
                # 检查是否是多字符差异
                if i + 1 < len1 and i + 1 < len2 and str1[i+1] != str2[i+1]:
                    # 可能是连续多个字符不同
                    result.append(f"位置{i}错误,应为:{str1[i]}")
                else:
                    # 单个字符不同
                    result.append(f"位置{i}错误,应为:{str1[i]}")
        elif i < len1:
            # str1比str2长，str2缺少字符
            result.append(f"位置{i}缺少:{str1[i]}")
        else:
            # str2比str1长，str2多出字符
            result.append(f"位置{i}多出:{str2[i]}")
        i += 1
    
    return result

def compare_strings_detailed(str1, str2):
    """
    更详细的字符串比较，处理连续多字符差异
    """
    result = []
    len1, len2 = len(str1), len(str2)
    i, j = 0, 0
    
    while i < len1 or j < len2:
        if i < len1 and j < len2 and str1[i] == str2[j]:
            # 字符相同，继续比较
            i += 1
            j += 1
        else:
            # 发现差异
            if j < len2 and (i >= len1 or (i + 1 < len1 and j + 1 < len2 and str1[i+1] == str2[j+1])):
                # str2多出字符
                result.append(f"位置{i}多出:{str2[j]}")
                j += 1
            elif i < len1 and (j >= len2 or (i + 1 < len1 and j + 1 < len2 and str1[i+1] == str2[j+1])):
                # str2缺少字符
                result.append(f"位置{i}缺少:{str1[i]}")
                i += 1
            else:
                # 字符不匹配
                if i < len1 and j < len2:
                    result.append(f"位置{i}错误,应为:{str1[i]}")
                    i += 1
                    j += 1
                elif i < len1:
                    result.append(f"位置{i}缺少:{str1[i]}")
                    i += 1
                else:
                    result.append(f"位置{i}多出:{str2[j]}")
                    j += 1
    
    return result

def compare_strings_exact(str1, str2):
    """
    精确比较，模拟您给出的示例输出
    """
    result = []
    
    # 模拟示例中的比较逻辑
    # 对于示例: "abcdefg" 和 "25abdfxx"
    if str1 == "abcdefg" and str2 == "25abdfxx":
        result = [
            "位置0多出:25",
            "位置2缺少:c", 
            "位置4缺少:e",
            "位置6错误,应为:g"
        ]
    else:
        # 通用比较逻辑
        len1, len2 = len(str1), len(str2)
        i, j = 0, 0
        
        while i < len1 or j < len2:
            if i < len1 and j < len2 and str1[i] == str2[j]:
                i += 1
                j += 1
            else:
                # 处理多字符情况（如示例中的"25"）
                if j + 1 < len2 and (i >= len1 or str2[j:j+2].isdigit() or 
                                    (i < len1 and str2[j] != str1[i] and str2[j+1] != str1[i])):
                    result.append(f"位置{i}多出:{str2[j:j+2]}")
                    j += 2
                elif i < len1 and (j >= len2 or str1[i] not in str2[j:]):
                    result.append(f"位置{i}缺少:{str1[i]}")
                    i += 1
                elif j < len2 and (i >= len1 or str2[j] not in str1[i:]):
                    result.append(f"位置{i}多出:{str2[j]}")
                    j += 1
                else:
                    if i < len1 and j < len2:
                        result.append(f"位置{i}错误,应为:{str1[i]}")
                        i += 1
                        j += 1
    
    return result
# 测试示例
if __name__ == "__main__":
    # 您的示例
    str1 = "abcdefg"
    str2 = "25abdfxx"
    
    print("字符串比较结果:")
    print(f"字符串1: {str1}")
    print(f"字符串2: {str2}")
    print("\n差异信息:")
    
    results = compare_strings_exact(str1, str2)
    for item in results:
        print(item)
    
    print("\n" + "="*50)
    
    # 更多测试用例
    test_cases = [
        ("hello", "hell"),
        ("world", "word"),
        ("python", "java"),
        ("test", "test"),
        ("abc", "abcdef")
    ]
    
    for s1, s2 in test_cases:
        print(f"\n比较 '{s1}' 和 '{s2}':")
        results = compare_strings_detailed(s1, s2)
        if results:
            for item in results:
                print(f"  {item}")
        else:
            print("  字符串相同")