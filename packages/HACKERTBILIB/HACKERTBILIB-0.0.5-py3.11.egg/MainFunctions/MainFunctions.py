#A FEW EXTENCTIONS
#
#Created by: Me
#Function and what they do is in 'FunctionsList.md'



def libcredits():
        print("Creator: Me")

def libhelp():
    print("Function avalible:\ndo(*function*)\n\nrun function by do(), and a lot more")


def nothing():
    pass


def invalid():
    print("Invali input")

def do(menu):
    try:
        func = globals()[menu]
    except KeyError:
        func = invalid
    func()
    
    
def dowe(menu):
    try:
        func = globals()[menu]
    except KeyError:
        if menu == "":
            nothing()
        else:
            print(KeyError)
    func()

def dowee(menu):
    try:
        func = globals()[menu]
    except KeyError:
        if menu == "":
            nothing()
        else:
            print("Something is wrong, ", menu, " was not found")
    func()



def inputprint(intname, text):
        intname = input(text)
        print(intname)