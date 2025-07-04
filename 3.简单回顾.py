money = 50000  # 初始化账户余额

def check_balance():
    """查看余额"""
    print(f'Your balance is ${money}')
    input('Press any key to return to the main menu...')

def add_money():
    """存款操作"""
    global money  # 使用 global 来修改全局变量
    number = int(input('Please enter the amount that you want to add: '))
    money += number
    print(f'You have added ${number}. Your new balance is ${money}')
    input('Press any key to return to the main menu...')

def withdraw_money():
    """取款操作"""
    global money  # 使用 global 来修改全局变量
    number = int(input('Please enter the amount that you want to withdraw: '))
    if number <= money:
        money -= number
        print(f'You have withdrawn ${number}. Your new balance is ${money}')
    else:
        print('Insufficient funds!')
    input('Press any key to return to the main menu...')

def main_menu():
    """主菜单，用户交互"""
    name = input('Welcome to the ATM, Enter your name: ')
    print(f'Hello, {name}, welcome to the ATM!')
    
    while True:
        # 显示菜单选项
        print('\nMain Menu:')
        print('1. Check balance')
        print('2. Add money')
        print('3. Withdraw money')
        print('4. Exit')
        
        option = input("Please enter your choice (1-4): ")

        if option == '1':
            check_balance()
        elif option == '2':
            add_money()
        elif option == '3':
            withdraw_money()
        elif option == '4':
            print('Thank you for using the ATM. Goodbye!')
            break  # 退出循环，结束程序
        else:
            print('Invalid choice, please try again.')

# 启动程序
main_menu()
