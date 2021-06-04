#Encryption software v1.2
import time
import random
import string

def loadBar(dot):
    for i in range(dot):
        print(".",end = "")
        time.sleep(1)
def setup():
    print("Starting up procyon", end="")
    loadBar(5)
    print("\n\n\n\n\n\n\n")
    print("    ====    ====     ===     ===== =    =     ===    ==     =                        ") 
    print("   =    =  =    =  =     =  =       =  =    =     =  = =    =    =        =   =    = ")
    print("   =    =  =    =  =     =  =         =     =     =  =  =   =     =      =   =    =  ")
    print("   =====   = ==    =     =  =         =     =     =  =   =  =      =    =   =    =   ")
    print("   =       =  =    =     =  =         =     =     =  =    = =     =    =   =      =  ")
    print("   =       =    =    ===     =====    =       ===    =     ==    =    =   =        = ")
    print("\n\n\n")
    print("#####################################################################################")
    print("#                                Procyon v1.2                                       #")
    print("#  ~ Use numbers to locate around the menu                                          #")
    print("#  ~ Have a great day :)                                                            #")
    print("#                                                                                   #")
    print("#                                                                                   #")
    print("#####################################################################################")
    print("\n\n\n\n")

def menu():
    print("\nFunctions List")
    print("(1) Caesar Cipher ")
    print("(2) Vigenere Cipher")
    print("(0) Quit ")
    while True:
        SELECT_MAIN = input("\nSelect: ")
        if checkInt(SELECT_MAIN) == True:
            if int(SELECT_MAIN) == 1:
                cae()
            elif int(SELECT_MAIN) == 2:
                vig()
            elif int(SELECT_MAIN) == 0:
                quit()
        else:
            print("Invalid input")
        
def checkInt(x):
    try:
        int(x)
        return True
    except:
        return False
def cae():
    print("\nCaesar Cipher")
    print("(1) Encode")
    print("(2) Decode")
    print("(0) Back to main menu")
    while True:
        SELECT_CAE = input("\nSelect: ")
        if checkInt(SELECT_CAE) == True:
            if int(SELECT_CAE) == 1:
                cae_en()
            elif int(SELECT_CAE) == 2:
                cae_de()
            elif int(SELECT_CAE) == 0:
                menu()
        else:
            print("Invalid input")
def vig():
    print("\nVigenere Cipher")
    print("(1) Encode")
    print("(2) Decode")
    print("(0) Back to main menu")
    while True:
        SELECT_VIG = input("\nSelect: ")
        if checkInt(SELECT_VIG) == True:
            if int(SELECT_VIG) == 1:
                vig_en()
            elif int(SELECT_VIG) == 2:
                vig_de()
            elif int(SELECT_VIG) == 0:
                menu()
        else:
            print("Invalid input")
#Caesar Cipher
def cae_en():
    print("\nMessage to be encrypted (no numbers or symbols)")
    while True:
        cae_en_in = input("===> ")
        if cae_valid(cae_en_in) == True:
            break
    print("\nShift the message by how much \n(Message can be shifted by 1 to 25, type 0 for random shift)")
    while True:
        SHIFT = input("===> ")
        if checkInt(SHIFT) == False:
            print("Not a valid number please re-enter")
        else:
            if int(SHIFT) > 25 or int(SHIFT) < 0:
                print("Not a valid number please re-enter")
            else:
                break
    a,b = cae_en_logic(SHIFT,cae_en_in)
    print("Your encrypted message:\n" + a)
    print("\nKeys shifted: " + str(b))
    time.sleep(2)
    menu()
def cae_valid(words):
    error = 0
    for letter in words:
        for x in range(10):
            if letter == str(x):
                error += 1
    if error == 0:
        return True
    else:
        print("Error: Numbers or symbols are present in the message please re-enter")
        return False
def cae_en_logic(key,msg):         #This part... lol so inefficient
    if int(key) == 0:
        key_shift = random.randint(1,26)
    else:
        key_shift = int(key)
    x,y = string.ascii_lowercase,string.ascii_uppercase
    lower = list(x)   
    upper = list(y)
    newMsg = ""
    for i in msg:
        if i.isupper() == True:
            index = upper.index(i)      
            newIndex = index + key_shift
            newIndex = cae_adj(newIndex)
            newMsg += upper[newIndex]
        elif i.islower() == True:
            index = lower.index(i)
            newIndex = index + key_shift
            newIndex = cae_adj(newIndex)
            newMsg += lower[newIndex]
        elif i == " ":
            newMsg += " "
    return newMsg,key_shift
def cae_adj(num):
    if num > 25:
        num = num - 26
    return num



def cae_de():
    print("Message to be decrypted (no numbers or symbols) ")
    while True:
        cae_de_in = input("===> ")
        if cae_valid(cae_de_in) == True:
            break
    print("Key (From 1 to 25, Enter 0 if unknown)")
    while True:
        SHIFT = input("===> ")
        if checkInt(SHIFT) == False:
            print("Not a valid number please re-enter")
        else:
            if int(SHIFT) > 25 or int(SHIFT) < 0:
                print("Not a valid number please re-enter")
            else:
                break
    cae_de_logic(SHIFT,cae_de_in)
    time.sleep(2)
    menu()
def cae_de_logic(key,msg):
    x,y = string.ascii_lowercase,string.ascii_uppercase
    lower = list(x)   
    upper = list(y)
    if int(key) > 0:
        start = int(key)
        end = int(key) + 1
    else:
        start = 1
        end = 26
    print("\t  Key","\t\t  Message")
    print("\tdefault\t\t",msg)     
    for key_shift in range(start,end):
        newMsg = ""
        print("\t ",key_shift,end ="")
        for i in msg:
            if i.isupper() == True:
                index = upper.index(i)      
                newIndex = index + key_shift
                newIndex = cae_adj(newIndex)
                newMsg += upper[newIndex]
            elif i.islower() == True:
                index = lower.index(i)
                newIndex = index + key_shift
                newIndex = cae_adj(newIndex)
                newMsg += lower[newIndex]
            elif i == " ":
                newMsg += " "
        print("\t\t",newMsg)
        
        

#Caesar Cipher
setup()
menu()



