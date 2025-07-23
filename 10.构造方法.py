# 设计一个类
class Student:
    
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender    
        
    # 成员方法 (方法中必须有self才能访问成员变量) 
    def say_hi(self):
        print(f'hi, my name is {self.name}')
        
    def say_hi2(self,message):
        print(f'hi, my name is {self.name}, {message}')

# 创建一个对象
stu1 = Student(19,'male','Bryce')

stu1.say_hi()
stu1.say_hi2('holy shit')

