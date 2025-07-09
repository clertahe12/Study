# 列表的定义                    
mylist = ['asdf',123,True]

# 查找元素的位置
print(mylist.index('asdf'))

# 修改特定下标索引的值
mylist[0] = 45
print(mylist)

# 在最后添加元素
mylist.append(123)
print(mylist)

# 在固定位置添加元素
mylist.insert(1,'sadf')
print(mylist)

# 在列表尾部添加一批元素
mylist2 = [35,77]
mylist.extend(mylist2)
print(mylist)

# 删除指定下表索引
mylist.pop(0)
print(mylist)

# 删除某个元素在列表的第一项
mylist.remove(123)
print(mylist)

# 清空列表
mylist.clear()
print(mylist)

# 统计某元素出现的次数
mylist3 = [1,1,1,1,32,4,5,5,2,12,1,4,23]
print(mylist3.count(1))

mylist  = [1,2,3,4,5,2,1,2,3,4,21,1,1,1,1,1]
count = 0
for i in mylist:
    if i == 1:
        count += 1
print(count)

# 所有元素数量
print(len(mylist3))

# 练习
test = [21,25,21,23,22,20]
test.append(31)
test1 = [29,33,30]
test.extend(test1)
test.remove(21)
test.pop
test.index(31)

list5 = [1,2,3,4,5]
def list_for_function(list):
    for i in list:
        print(i)
list_for_function(list5)

def list_while_function(list):
    index = 0
    while index < len(list):
        print(list[index])
        index += 1
list_while_function(list5)

