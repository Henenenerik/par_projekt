
from userfunctions import *
from util_func import *




def mainMenu():
    '''
    Input:
    Return: integer

    Beskriving:
        Skriver ut huvudmenyn.

    '''
    print "Options:"
    print "1. Log in"
    print "2. Register"
    print "3. Quit"

    return int(raw_input())

def logIn():
    '''
    Input:
    Return: integer

    Beskriving:
        Laser in anvandarnamn och losenord,
        kallar uLogIn() for att se om det stammer.

    '''
    uname = raw_input("Username: ")
    upass = raw_input("Password: ")

    #uLogIn finns i userfunctions.py
    return uLogIn((uname,upass))

def regUser():
    '''
    Input:
    Return: integer

    Beskriving:
        Laser in anvandarnamn och losenord,
        kallar checkAvailablility() for att se att det inte redan finns,
        om allt ar bra, kallar uRegister() for att skriva in det i databasen.
    '''
    uname = raw_input("Desired username(letters;Max16chars): ")

    #Kollar att anvandarnamnet uppfyller kraven och ar nytt.
    #changeCheck() och checkAvailablility() finns i userfunctions.py
    if length(uname)>16 or changeCheck(uname) == 0:
        return 2
    elif checkAvailablility(uname) == 1:
        return 3
    upass = raw_input("Desired password(letters;Max16chars): ")

    #Kollar att losenordet uppfyller kraven.
    if length(upass)>16 or changeCheck(upass) == 0:
        return 2

    #skriver in anvandaren i databasen.
    #uRegister() finns i userfunctions.py
    uRegister((uname,upass))
    return 0

def main():
    '''
    Input:
    Return:

    Beskriving:
        Huvudfunktionen for programmet.
        Tar input fran anvandaren och kallar motsvarande funktioner.
        Avbryts nar anvandaren vill avsluta programmet.
    '''
    quit = 1
    currentUser = ('none','none')

    while quit == 1:
        userChoice = mainMenu()
        # Om anvandaren vill logga in.
        if userChoice == 1:
            n = logIn()
            # Om inloggningen lyckas.
            if n == 1:
                logInScreen()
            # Om inloggningen misslyckas.
            elif n == 2:
                print "Wrong password"
            elif n == 0:
                print "No user by that name"
            else:
                print "user login switch defaulted"
        # Om anvandaren vill registera sig.
        elif userChoice == 2:
            n = regUser()
            # Om registreringen lyckas.
            if n == 0:
                print "User registered."
            # Om registreringen misslyckas.
            elif n == 1:
                print "Invalid username."
            elif n == 2:
                print "Invalid password."
            elif n == 3:
                print "Username already used."
            else:
                print "User register switch defaulted."
        # Om anvandaren vill avsluta programmet.
        elif userChoice == 3:
            quit = 0
        else:
            print "userChoice switch defaulted"
main()
