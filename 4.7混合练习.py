numbers = [3, 1, 4, 1, 5, 9, 2, 6]
'''
在列表末尾添加数字 8

删除第一个出现的 1

对列表进行升序排序

打印修改后的列表
'''

numbers.append(8)
numbers.remove(1)
numbers.sort(reverse=False)
print(numbers)

s = "Hello, World!"
'''
将字符串转换为全大写

统计字符 'l' 出现的次数

用 "Python" 替换 "World"

打印最终字符串
'''

s.count('l')
new_s =s.upper()
new_s1 = new_s.replace('World','Python')
print(new_s1)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)
print(A - B)

t = (10, 20, 30, 40, 50)
'''
访问第3个元素 索引为2

计算元组长度

将元组转换为列表 并修改第2个元素为 25

打印修改后的列表
'''
print(t[2])
print(len(t))
t = list(t)
print(t)

person = {"name": "Alice", "age": 25, "city": "New York"}
'''
添加键值对 "gender": "Female"

删除键 "age"

获取所有键的列表

打印修改后的字典

'''
person["gender"] = "male"
del person['age']
for k in person:
    print(k)
    
words = ["apple", "banana", "apple", "orange", "banana", "grape"]
scores = (85, 90, 78, 92, 88)
student = {
    "name": "Bob",
    "courses": ["Math", "Physics"],
    "grades": {"Math": 90, "Physics": 85}
}
'''
列表操作：统计 words 中 "apple" 出现的次数。

字符串操作：将 student["name"] 的首字母大写，其余小写。

集合操作：从 words 中提取唯一的水果名（去重）。

元组操作：计算 scores 的平均分（保留2位小数）。

字典操作：在 student["grades"] 中添加新科目 "Chemistry"，成绩为 88。
'''
print(words.count('apple'))
student['name'] = student["name"].capitalize()
s = set(words)
print(student)
print(round(sum(scores)/len(scores),2))
student["grades"]["Chemistry"] = 88
print(student)
