# 从1开始,4结束,步长1
mylist = [0,1,2,3,4,5,6,]
mylist[1:4]

# 从头开始,最后结束,步长1
mytuple = (0,1,2,3,4,5,6)
mytuple[:]

# 从头开始.最后结束,步长为2
mystr = '0123456'
mystr[::2]

# 步长-1
mystr[::-1]

# 3开始,1结束,步长-1
print(mystr[3:1:-1])

'''大练习
'''
str = '九八七,六五四,三二一'
new_str = str[::-1]
mylist = new_str.split(',')
print(mylist[1])
