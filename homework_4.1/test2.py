# 2. 查找包含目标字符串的元素索引

def find_index(str_list, target):
    return [i for i, s in enumerate(str_list) if target in s]

# 测试示例
print(find_index(["apple", "banana", "pineapple"], "apple"))  # 输出 [0, 2]