#Arran C
#5/3/20
#imports the module we need to automate the swiping.
import pyautogui

counter = 0
userQuit = 'no'

#To discover what is the position of the screen, uncomment the code below and edit the values in the if statments
#xyz = pyautogui.position()
#print(xyz)

amountOfSwipes = int(input('Enter the amount of times would you like to swipe: '))
if amountOfSwipes > 100:
    print('Please re-enter')

#Allows the user to quit at any time
userAsk = input('Would you like to start? (Make sure the screen is clear and there\'s nothing in they way of it): ')

while userQuit == 'no':
    
    while counter != amountOfSwipes:

        counter = counter + 1
        
        if userAsk == 'yes':
            pyautogui.moveTo(720, 491)
            pyautogui.drag(200, 0, 0.5, button='left')
            pyautogui.moveTo(1165, 542)
            break
        elif userAsk == 'no':
            print('Okay, goodbye!')
            quit

        userQuit = input(('Would you like to try again?: '))
        if userQuit == 'no':
            print('Okay, goodbye.')
        else:
            break



