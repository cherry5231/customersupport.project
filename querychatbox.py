def user():
    print("Welcome to Demo,type Create if you want to create an account or if an existing user type login")
    account_type = input("")
    if account_type == "create" or account_type == "Create" or account_type == "CREATE":
        while True:  
            regions = ["Asia", "Europe", "Russia", "Australia", "Africa", "America"]
            for region in regions:
                print(region)
            
            account_location = input("Please choose the region from above: ")

            if account_location in regions:
                print(account_location)
                break

            else:
                    print("Invalid region")
        while True:  
            phn_no = input("Enter your phone number: ")
            if len(phn_no) == 10 and phn_no.isdigit():
                print(phn_no,"we will send an otp to this phone number , please enter the otp below\n")
                break
            else:
                print("Please enter correct phone number\n")
        while True:    
            otp = (input(""))
            
            if len(otp) == 4 and otp.isdigit():
                print("Thankyou for registration,Your account has been registered successfully\n")
                break
                
            else:
                print("Invalid otp\n")
    else:
            print("Welcome Back, its good to have you, please enter your username to login")
        
     

    email = input("Enter your email: ")
    print(email)
    while True: 
        Password = input("Create a password: ")
        has_upper= False
        has_digit = False
        has_specialchar = False
        spclchar = "@$#!%^&*_"

        for password in Password:
                    
                                
                    if password.isupper():
                        has_upper = True
                    
                    
                    if password.isdigit():
                        has_digit = True
                    if password in spclchar:
                        has_specialchar = True
        if has_upper and has_digit and has_specialchar:
                    print("Accepted")
                    break
        else:
                    print("password should have atleast one upper case letter,a digit,a symbol: ")
    while True:
        
        
       username = input("Enter username:  ")
       has_upper= False
       has_digit = False
       has_specialchar = False
       spclchar = "@$#!%^&*_"            
       for name in username:
                
                if name.isupper():
                    has_upper = True
                
                
                if name.isdigit():
                    has_digit = True
                if name in spclchar:
                    has_specialchar = True
       if len(username) <= 10 and has_upper and has_digit and has_specialchar:
                print("Welcome to query assistance",username,"Thankyou for signing up,How may i help you?")
                break
       else:
            print("username should have atleast one upper case letter,a digit,a symbol and allowed up to 10 charecters: ")
    return username

          
              
    
         
        

def chatbox(username):
    query = input("Please state your queries: ")
    
    print("Am sorry to hear that,on our behalf we would like to kindly apologise for the inconveince we have caused,our team would review your request and contact you soon")
    response1 = input("")
    
    print("For your queries do you want to contact our manager yourself? if not just type no ")
    response2 = input("")
    if response2 == "no" or response2== "No" or response2== "NO" or response2 == "Nope" or response2== "NOPE" or response2== "nope":
        print("Good to hear that,if you want anything else let me know")
    else:
     print("Our manager mail is kattacharan10flasmvp@gmail.com , please makes sure to be respectful and detailed about your problems for a faster solution")
    response3 = input("")
    
    print("Thankyou for contacting",username,"We will be glad to always support you")
userr = user()
    
chatbox(userr)