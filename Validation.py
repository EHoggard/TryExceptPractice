def account_number_validation(accountNumber):
    if accountNumber:

        if len(str(accountNumber)) == 10:

            try:
                int(accountNumber)
                return True
            except ValueError:
                print("Invalid Account Number, Account Number should be an integer")
            except TypeError:
                print("Invalid Account Type")
                return False
        else:
            print("Invalid Account Type")
            return False
    else:
        print("Account number is a required field")
        return False

def valid_registration_input(input):