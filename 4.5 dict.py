# 字典的创建
stu = dict(name = 'bob', age = 25, course = ['english','math'])

# 访问字典元素
print(stu["name"])

# 添加删除修改字典元素的值
stu['gender'] = 'male'
stu['age'] = 26
del stu['name']
print(stu)

# 合并字典
extra_info = dict(job = 'student', hobby = 'reading')
stu.update(extra_info)
print(stu)

# 键值对
stu.keys()
stu.values()

# 遍历
for keys in stu :
    print(keys)

for values in stu.values():
    print(values)
    
for k,v in stu.items():
    print(k,v)
    