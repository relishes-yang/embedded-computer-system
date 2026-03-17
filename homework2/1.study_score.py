"""1.（练习实例15）利用条件运算符的嵌套来完成此题：
学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
"""

score = int(input("请输入学生成绩："))

if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'
print("学生成绩等级为：", grade)

# 或者写成下面形式
"""
score = int(input("请输入学生成绩："))
grade = 'A' if score >= 90 else 'B' if score >= 60 else 'C'
print("学生成绩等级为：", grade)

"""
