# 定义集合
myset = {'0','1','2','3','4'}

# 添加新元素
myset.add('6')

# 删除元素
myset.remove('1') 

# 随机获取一个元素
myset.pop()

# 清空集合
myset.clear()

# 四种对比
myset = {'0','1','2','3'}
myset1 = {'3','4','5'}
all = myset | myset1 # 并集
common = myset & myset1 # 交集
difference = myset - myset1 # 差集

'''set 练习
1. 定义一个空集合
2. for循环遍历list
3. 将列表元素添加到set
4. 打印set
'''
mylist = [1,2,3,4,1,2,3,4,5,6,3,2,3,4,6,7,8,9,7,6,5,3,4,6,8]

myset = set()
for element in mylist:
    myset.add(element)
print(myset)
