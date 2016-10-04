
def remove_non_letters(s):
    '''
    Input: en string
    Return: en string

    Beskriving:
        Tar en sträng och tar bort alla icke bokstäver.
        Tagen från lärar-Karl.
    '''
    return "".join([c for c in s if c.isalpha()])

def checkAvailablility(s):
    '''
    Input: en string
    Return: integer

    Beskriving:
        Öppnar en kanal till username.txt och
        kollar om s finns bland anvandarnamnen.
    '''
    f = open('username.txt','r')
    for line in f:
        if remove_non_letters(line[0:15]) == s:
            return 1
    f.close()
    return 0

def uLogIn((username,password)):
    '''
    Input: Tuple med två strängar.
    Return: en integer

    Beskriving:
        oppnar en kanal med username.txt,
        ser om username/password stammer overens
    '''
    f = open('username.txt','r')
    found = 0
    for line in f:
        if remove_non_letters(line[0:15]) == username:
            if remove_non_letters(line[16:31]) == password:
                found = 1
            else:
                found = 2

    f.close()
    return found

def uRegister((username,password)):
    f = open('username.txt','r+')
    temp = "                "
    f.seek(0,2)
    f.write(("\n" + username + temp[0:(16-length(username))] + password + temp[0:(16-length(username))]))
    f.close()
    print "User successfully created"
    return

def length(xs):
    n = 0
    for val in xs:
        n = n+1
    return n

def changeCheck(choosenStr):
    temp = remove_non_letters(choosenStr)
    if temp == choosenStr:
        return 1
    else:
        return 0

def stringFix(choosenStr):
    temp = "                "
    return choosenStr + temp[0:(16-length(uname))]
