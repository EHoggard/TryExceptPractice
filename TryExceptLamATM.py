x = lambda a, b : a*b
print(x(2, 6))

import random
import Validation

database = {}
userdatabase = {}
user = {}

def init():


    isValidOptionSelected = False
    print("Welcome to Bank of Hoggard")

    while isValidOptionSelected == False:

        haveAccount = int(input("Do you have an account with us?: 1 (yes) 2 (no) \n"))
        
        if(haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected = True
            register()
        else:
            print("You have selected an invalid option")
            init()

def login():

    print("Login to your account")

    accountNumberfromuser = int(input("What is your account number? \n" ))

    is_valid_account_number = Validation.account_number_validation(accountNumberfromuser)

    if is_valid_account_number:

        password = input("What is your password? \n")

        for accountnumber, userDetails in database.items():
                if(accountnumber == accountNumberfromuser):
                    if(userDetails[3] == password):
                        bankOperation(user)

    print('Invalid account or Password')
    login()


def register():
    print("Register for new account")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create password \n")

    accountNumber = generateAccountNumber()
    print(accountNumber)
    #database[accountNumber] = [ first_name, last_name, email, password, 0 ]
    is_userid_created = database.Create(accountNumber, first_name, last_name, email, password, 0 )
    if is_userid_created:
        print("Your account has been created")
        print("Your account number is: %d" % accountNumber)
    else:
        print("Something went wrong, please try again")
        register()

    login()

def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user[1] ) )
    
    
    selectedOption = int(input("What would you like to do? (1) Deposit (2) Withdrawl (3) Complaint (4) Exit \n"))

    if (selectedOption == 1):
            
        depositOperation()
    elif (selectedOption == 2):
            
        withdrawlOperation()
    elif (selectedOption == 3):
            
        Complaint()
    elif (selectedOption == 4):
            
        exit()
    else:
        print("Invalid Option Selected")
        bankOperation(user)

Balance = 6000

def withdrawlOperation():
    input("How much would you like to withdrawl? \n")
    print("Please take your cash")

def depositOperation():
    Deposit = input("How much would you like to deposit? \n")
    sum = float(Balance) + float(Deposit)
    print('Your current Balance is', sum)

def Complaint():
    input("What issue would you like to report? \n")
    print("Thank you for contacting us")

def generateAccountNumber():

    return random.randrange(1111111111,9999999999)

def logout():
    login()

init()