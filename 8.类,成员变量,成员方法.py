# 设计一个类
class Student:
    # 成员变量
    name = None
    age = None
    gender = None
    
    # 成员方法 (方法中必须有self才能访问成员变量)
    def say_hi(self):
        print(f'hi, my name is {self.name}')
        
    def say_hi2(self,message):
        print(f'hi, my name is {self.name}, {message}')

# 创建一个对象
stu1 = Student()

# 给他进行赋值
stu1.age = 18
stu1.gender = 'male'
stu1.name = 'Bryce'
stu1.say_hi()
stu1.say_hi2('holy shit')

