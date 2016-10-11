from utils import register


exit = False
while exit == False:
    print('1. Register')
    print('2. Login')
    print('3. Exit')



    choice = input('What would you like to do?')


    if choice == 1:
        register()
