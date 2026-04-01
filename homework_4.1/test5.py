# 一词多义字典：key为单词，value为释义列表
word_dict = {
    "bus": ["公共汽车", "总线"],
    "bank": ["银行", "河岸"],
    "key": ["钥匙", "按键"]
}

# 极简查询功能
word = input("请输入单词: ").lower()
print(word_dict.get(word, []))