# 定义tuple
t1 = (123,"hello",True)

# 定义单个元素
t2 = ("hello",)

# tuple 的嵌套
t3 = ((1,2,3),(4,5,6),(7,8,9),(0,1,2))

# 下表索引获得值
num = t3[1][2]
print(num)
 
# tuple的相关操作 嵌套的只找一层,否则需要循环
# index() 找到对应元素的下表值,否则报错
# count() 统计某元素在tuple中出现的次数
# len() 统计长度

# while遍历
def tuple_while_function(tuple):
    index = 0
    while index < len(tuple):
        print(tuple[index])
        index += 1
tuple_while_function(t3)

# for便利
def tuple_for_function(tuple):
    for element in tuple:
        print(element)
tuple_for_function(t3)