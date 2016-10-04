def logInScreen():
    print "Welcome back."
    n = 1
    while n == 1:
        userChoice = logInActions()
        print userChoice
        if userChoice == 1:
            libActions()
        elif userChoice == 2:
            lendStatus()
        elif userChoice == 3:
            userInfo()
        elif userChoice == 4:
            n = 0
        else:
            print "Login Screen switch defaulted."
    return

def logInActions():
    printScreen(1)
    n = int(raw_input())
    return n

def libActions():
    printScreen(2)
    n = int(raw_input())
    if n == 1:
        print "To be implemented!"
    elif n == 2:
        print "To be implemented!"
    elif n == 3:
        return
    else:
        print "libAction switch defaulted."
    return

def lendStatus():
    printScreen(3)
    n = int(raw_input())
    if n == 1:
        print "To be implemented!"
    elif n == 2:
        return
    else:
        print "lendStatus switch defaulted."
    return


def userInfo():
    printScreen(4)
    n = int(raw_input())
    if n == 1:
        print "To be implemented!"
    elif n == 2:
        return
    else:
        print "userInfo switch defaulted."
    return


def printScreen(n):
    if n == 1:
        print "1. Library actions."
        print "2. Lend status."
        print "3. User information."
        print "4. Log out."
    elif n == 2:
        print "1. Search by title."
        print "2. Search by author."
        print "3. Return to previous menu."
    elif n == 3:
        print "1. List lent books."
        print "2. Return to previous menu."
    elif n == 4:
        print "1. Show user statistics."
        print "2. Return to previous menu."
    else:
        print "printScreen switch defaulted."
    return
