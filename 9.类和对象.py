# 设计一个闹钟
class Clock:
    id = None
    price = None
    
    def ring(self):
        print('ring for 2000s')

# 创造两个对象让他们工作
clock1 = Clock()
clock1.id = 1
clock1.price = 19

clock2 = Clock()
clock2.id = 2
clock2.price = 29

clock1.ring()
clock2.ring()