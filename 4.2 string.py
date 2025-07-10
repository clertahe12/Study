mystr = "abcdefghijklmnopqrstuvwxyz"

# 通过下标获取值
print(mystr[0])

# index方法
print(mystr.index("i"))

# replace方法
new_mystr = mystr.replace("a","0")
print(new_mystr)

# split方法
mystr1 = "hello welcome to my place"
mystr1_list = mystr1.split(' ')
print(mystr1_list)

# strip()去除首尾括号中的内容
mystr2 = "123woshichaoren321"
new_mystr2 = mystr2.strip("123")
print(new_mystr2)

# 统计字符串中某字符出现的次数
print(len(mystr))

# 统计某字符串出现的次数
count = mystr2.count('o')
print(count)

'''练习分割字符串
1. 统计有多少个it
2. 空格替换为1
3. 按照1分割获得list
'''
mylist = "itheima itcast boxuegu"
count = mylist.count('it')
print(count)
new_mylist = mylist.replace(' ','1')
print(new_mylist)
print(new_mylist.split('1'))