'''
1. 切片
2. 列表推倒式
3. 生成器表达式
4. 解包
5. with 自动资源管理
6. 装饰器
7. 海象运算符
8. 模式匹配--超级switch
'''

# lambda arguments: expression
square = lambda x: x * x

# 列表推导式

# 生成器表达式

words = ["apple", "be", "cat", "dog", "elephant"]
# 将以下列表中的所有字符串转换为大写，并过滤掉长度小于3的字符串
print([word.upper() for word in words if len(word) >= 3])
# 生成1-10的数字的平方，但只保留偶数的平方
print([i ** 2 for i in range(1,11) if i % 2 == 0])
# 将二维矩阵展平为一维列表
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([nums for rows in matrix for nums in rows])
# 获取从一个嵌套字典结构中提取所有学生的数学成绩，并计算平均分
classes = {
    "ClassA": [
        {"name": "Alice", "scores": {"math": 85, "english": 92}},
        {"name": "Bob", "scores": {"math": 78, "english": 88}}
    ],
    "ClassB": [
        {"name": "Charlie", "scores": {"math": 92, "english": 85}},
        {"name": "Diana", "scores": {"math": 88, "english": 90}}
    ]
}
import statistics
avg = statistics.mean([s['scores']['math'] for class_group in classes.values() for s in class_group ])
print(avg)

# 创建一个生成器函数 fibonacci_gen()，无限生成斐波那契数列（从0开始）
def fibonacci_gen():
    a,b = 0,1 
    while True:
        yield a
        a, b = b, a + b


