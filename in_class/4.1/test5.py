# 编写一个程序，按升序对（名称，年龄，高度）元组进行排序，
# 其中 name 是字符串，age 和 height 是数字。

# 读取控制台输入
data = []  # 创建一个空列表，用于存储输入的元组

while True:  # 无限循环，直到遇到空行才退出
    line = input().strip()  # 读取一行输入，并去除首尾的空白字符（如换行符、空格）
    if not line:            # 如果读取到空行（用户直接按回车），则结束输入
        break

    # 按逗号分割字符串，得到三个部分：名称、年龄、高度
    # 注意：用户可能输入带空格的字段，例如 "Json ,21,85"
    name, age, h = line.split(',')

    # 去除名称两端可能存在的空格，年龄和高度转换为整数
    # 然后将 (名称, 年龄, 高度) 作为一个元组添加到 data 列表中
    data.append((name.strip(), int(age), int(h)))

# 按 name > age > height 升序排序
# key=lambda x: (x[0], x[1], x[2]) 表示先按元组的第一个元素（名称）排序，
# 如果名称相同，则按第二个元素（年龄）排序，如果年龄也相同，则按第三个元素（高度）排序
# 默认排序方式为升序
data = sorted(data, key=lambda x: (x[0], x[1], x[2]))

# 输出结果
for item in data:  # 遍历排序后的每个元组
    # 使用 f-string 格式化输出，字段之间用逗号和空格分隔，保持与输入格式一致
    print(f"{item[0]}, {item[1]}, {item[2]}")