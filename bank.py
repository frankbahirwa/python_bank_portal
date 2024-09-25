# python bank portal

main_balance = 0

def deposit():
  global main_balance
  money = int(input('Enter money to deposit:_ '))
  if money >0:
    main_balance += money
    print(f'Successfully deposited {money}. Your new balance is {main_balance}')

def withdraw():
      global main_balance

      money = int(input('Enter money to withdraw:_ '))
      if money <= main_balance:
        main_balance -= money
        print(f'Successfully withdrawn {money}. Your new balance is {main_balance}')
      else:
        print('Insufficient balance to withdraw')

def check_balance():
  global main_balance
  print(f'the main balance now is {main_balance}')

def backing():
   print('Backing')
      

def menu():  
  while True:
    print('\n menu')
    print('1. check balance')
    print('2. withdraw money')
    print('3. deposit money')
    print('4. exit')

    choice = input('enter your choice:_ ')
    
    if choice == '1':
      check_balance()
    elif choice == '2':
      withdraw()
    elif choice == '3':
      deposit()
    elif choice == 'exit':
      print('Exiting...')
      main()
    
    else:
      print('Invalid input...')


def main():
   global main_balance

   initial = 100000
   ussd ='*123#'
   main_balance = initial
   pin  = 12345
   
   inussd = input('Enter the ussd code:_ ')
   if ussd == inussd:
      inpin = int(input('Enter the pin code:_ '))
      if inpin == pin:
         menu()
      else:
         print('Invalid pin code...')
main()