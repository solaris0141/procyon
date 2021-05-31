#Encryption software v1.0
import time
import random
import tkinter
def loadBar(dot):
    for i in range(dot):
        print(".",end = "")
        time.sleep(2)
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
    print("#                                Procyon v1.0                                       #")
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
setup()
menu()
