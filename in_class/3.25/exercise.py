# #!/usr/bin/python3
#
# nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(nums[0:4])
#
# queue = []
#
# # 添加元素到队列的末尾
# queue.append('A')
# queue.append('B')
# queue.append('C')
#
# # 从队列的开头删除元素并返回
# print(queue.pop(0))  # A
# print(queue.pop(0))  # B
# print(queue.pop(0))  # C
#
# # !/usr/bin/python3
#
# list = ['Google', 'Runoob', 1997, 2000]
#
# print("原始列表 : ", list)
# del list[2]
# print("删除第三个元素 : ", list)
#


# !/usr/bin/python3

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)

tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
type(tinydict)

