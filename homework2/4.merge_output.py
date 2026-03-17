"""
4.（练习实例99）有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
"""

a = open('A.txt', 'r',encoding='utf-8').read().strip()
b = open('B.txt', 'r',encoding='utf-8').read()
print(f"文件A的内容是：{a}")
print(f"文件B的内容是：{b}")
with open('C.txt', 'w',encoding='utf-8') as f:
    f.write(a + b)
print("""——————————————————————————————————
已将文件A和文件B的内容合并并写入文件C""")
with open('C.txt', 'r',encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)