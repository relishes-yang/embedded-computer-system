# 2. 查找包含目标字符串的元素（返回字符串本身）

def find_strings(str_list, target):
    """返回列表中包含目标字符串的所有字符串"""
    return [s for s in str_list if target in s]

# 测试示例
print(find_strings(["apple", "banana", "pineapple"], "apple"))  # 输出 ['apple', 'pineapple']