"""
5.字典编程。编写一个有5个中英文单词的字典，可以添加、删除、遍历单词；
然后，单词数量达到10个，最终，可以中英文单词可以相互翻译。
"""

# 初始化包含5个中英文单词的字典
word_dict = {
    "苹果": "apple",
    "香蕉": "banana",
    "橙子": "orange",
    "葡萄": "grape",
    "草莓": "strawberry"
}

def add_word():
    """添加新单词到字典"""
    chinese = input("输入中文单词: ")
    english = input("输入英文单词: ")
    word_dict[chinese] = english
    print(f"已添加: {chinese} -> {english}")


def delete_word():
    """删除字典中的单词"""
    word = input("输入要删除的中文单词: ")
    if word in word_dict:
        del word_dict[word]
        print(f"已删除: {word}")
    else:
        print("单词不存在")


def show_words():
    """遍历并显示所有单词"""
    print("\n当前字典内容:")
    for chinese, english in word_dict.items():
        print(f"{chinese} -> {english}")
    print(f"总单词数: {len(word_dict)}\n")


def translate():
    """中英文相互翻译"""
    if len(word_dict) < 10:
        print("错误: 需要10个单词才能进行翻译")
        return

    query = input("输入中文或英文单词: ")

    # 尝试查找中文
    if query in word_dict:
        print(f"中文: {query} -> 英文: {word_dict[query]}")
    # 尝试查找英文
    elif query in word_dict.values():
        # 找到对应的中文
        chinese = next(key for key, value in word_dict.items() if value == query)
        print(f"英文: {query} -> 中文: {chinese}")
    else:
        print("单词未找到")


# 主程序
print("欢迎使用中英文单词翻译工具！")
print("初始有5个单词，添加5个达到10个后即可进行翻译")

while True:
    print("\n菜单:")
    print("1. 添加单词")
    print("2. 删除单词")
    print("3. 遍历单词")
    print("4. 翻译")
    print("5. 退出")

    choice = input("请选择操作: ")

    if choice == "1":
        add_word()
    elif choice == "2":
        delete_word()
    elif choice == "3":
        show_words()
    elif choice == "4" and len(word_dict) >= 10:
        translate()
    elif choice == "5":
        print("感谢使用，再见！")
        break
    else:
        print("无效选择，请重试")