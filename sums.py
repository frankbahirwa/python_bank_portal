def frank():
    num1 = int(input('enter num 1:_ '))
    num2 = int(input('enter num 2:_ '))
    results  = num1+num2
    print (f'then sum is {results}')


def check_odd():

    num = int(input('enter a number:_ '))
    if num % 2!= 0:
        print(f'{num} is odd')
    else:
        print(f'{num} is even')    

def menu():
    print("\n menu")
    print("1. Addition")
    print("2. chacking odd")

    choice  = input('enter your choice:_ ')

    if choice == '1':
        frank()
    elif choice == '2':
        check_odd()
menu()              