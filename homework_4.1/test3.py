# 编写一个程序，按升序对（名称，年龄，高度）元组进行排序，
# 其中 name 是字符串，age 和 height 是数字。

# # 读取控制台输入
# data = []
# while True:
#     line = input().strip()
#     if not line:
#         break
#     name, age, h = line.split(',')
#     data.append( (name.strip(), int(age), int(h)) )
#
# # 按name>age>height升序排序
# data = sorted(data, key=lambda x: (x[0], x[1], x[2]))
#
# # 输出结果
# for item in data:
#     print(f"{item[0]}, {item[1]}, {item[2]}")

data = []
while True:
    line = input().strip()
    if not line:
        break
    name, age, h = line.split(',')
    data.append((name.strip(), int(age), int(h)))

data.sort()  # 默认按元组顺序排序

for name, age, h in data:
    print(f"{name}, {age}, {h}")