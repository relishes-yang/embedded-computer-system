class Singleton:
    # 类属性，存储全局唯一实例
    _instance = None

    # 重写实例创建的核心方法__new__，控制实例生成逻辑
    def __new__(cls, *args, **kwargs):
        # 若实例不存在，创建唯一实例
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        # 实例已存在，直接返回已有实例
        return cls._instance


# 测试验证
if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    # 两个实例内存地址完全一致，证明是同一个对象
    print(f"s1内存地址：{id(s1)}")
    print(f"s2内存地址：{id(s2)}")
    print(f"是否为同一个实例：{s1 is s2}")  # 输出 True