def monkey_peach():
    """
    简单暴力破解法解决猴子分桃问题
    """
    # 从一个较大的数开始尝试
    peaches = 1

    while True:
        original = peaches  # 保存原始桃子数

        # 模拟五只猴子的操作
        success = True
        for i in range(5):
            # 检查当前桃子数是否能分5份余1
            if peaches % 5 != 1:
                success = False
                break

            # 分成5份，扔掉1个，拿走1份（即剩下4份）
            peaches = (peaches - 1) // 5 * 4

        # 如果五只猴子都成功操作，找到了答案
        if success:
            return original

        peaches = original + 1  # 尝试下一个桃子数


# 计算并输出结果
result = monkey_peach()
print(f"海滩上原来最少有 {result} 个桃子")

# 验证结果
print("\n验证过程:")
temp = result
for i in range(1, 6):
    print(f"第{i}只猴子：{temp}个桃子 -> 分5份余1 -> 拿走1份 -> 剩余{(temp - 1) // 5 * 4}个")
    temp = (temp - 1) // 5 * 4