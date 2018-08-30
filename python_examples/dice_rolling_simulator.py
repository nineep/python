import random

global user_exit_checker
user_exit_checker="exit"

# Our start function (what the user will first see when starting the program_

def start():
    print "Welcome to dice rolling simulator: \nPress Enter to proceed"
    raw_input(">")

    #Starting our result function (The dice picker function)
    result()

#Our exit function (what the user will see when choosing to exit the program)
def bye():
    print "Thanks for using the diceing rolling simulator! Have to great day! =)"

# Result function which is our dice chooser function
def result():
    #user dice chooser No idea how this got in here, thanks EroMonsterSanji.

    print "\r\nGreat! Begin by choosing a die! [6] [8] [12]?\r\n"
    user_dice_chooser = raw_input(">")
    user_dice_chooser = int(user_dice_chooser)

    #Below is the references to our dice functions (Below), when the user choose a dice
    if user_dice_chooser == 6:
        dice6()

    elif user_dice_chooser == 8:
        dice8()

    elif user_dice_chooser == 12:
        dice12()

    #If the user doesn't choose an applicable option
    else:
        print "\r\nPlease choose one of the applicable options!\r\n"
        result()

#Below are our dice functions
def dice6():
    dice_6 = random.randint(1,6)
    print "\r\nYou rolled a " + str(dice_6) + "!\r\n"

    #cheking if the user would like to roll another die, or to exit the program
    user_exit_checker_raw = raw_input("\r\nIf you want to roll another die, type [roll]. To exit, type [exit].\r\n?>")
    user_exit_checker = (user_exit_checker_raw.lower())
    if user_exit_checker == "rool":
        start()
    else:
        bye()

def dice8():
    dice_8 = random.randint(1,8)
    print "\r\nYou rolled a " + str(dice_8) + "!"

    user_exit_checker_raw = raw_input("\r\nIf you want to roll another die, type [roll]. To exit, type [exit].\r\n?>")
    user_exit_checker = (user_exit_checker_raw.lower())
    if user_exit_checker=="roll":
        start()
    else:
        bye()

def dice_12():
    dice_12 = random.randint(1,12)
    print "\r\nYou rolled a " + str(dice_12) + "!"

    user_exit_checker_raw = raw_input("\r\nIf you want to roll another die, type [roll]. To exit, type [exit].\r\n?>")
    user_exit_checker = (user_exit_checker_raw.lower())
    if user_exit_checker=="roll":
        start()
    else:
        bye()
        
# Actually starting the program now.
start()
