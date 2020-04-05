import string
import random
def reg_user():
    users = []
    def create_account():
        def new_user():
            #Enter user data
            fname = input("First Name: ")
            lname = input("Last Name: ")
            email = input("Email: ")
            user_id = ''.join([random.choice(string.ascii_letters + string.digits) for x in range(4)])

            #password generation
            pword = ''.join([random.choice(string.ascii_letters + string.digits) for x in range(5)])
            password = fname[0:2] + lname[-2:] + pword
            print("Your password is " + password)

            #If user rejects generated password:
            new_pword = input("Are you satisfied with this password? yes/no?  ").lower()
            if new_pword == "no":
                new_password = input("Enter your password here. Password should be more than 7 characters: ")
                while len(new_password) < 7:
                    new_password = input("Your password should be more than seven characters. Enter your password again: ")
                else:
                    print("Password saved!")
            elif new_pword == "yes":
                print("Password saved!")
            else:
                print()

            #storing User details
            user_details = {"id": user_id, "First_Name": fname, "Last_Name": lname, "Email": email, "Password": password}
            if new_pword == "no":
                user_details["Password"] = new_password
            users.append(user_details)

        new_user()
        # add new user account
        new_account = input("Do you want to register a new user? yes/no? ").lower()
        if new_account == "yes":
            create_account()

        elif new_account == "no":
            print("Thanks for signing up!")
        else:
            print("")
        print()

    create_account()
    #print user list here
    print(users)


reg_user()



