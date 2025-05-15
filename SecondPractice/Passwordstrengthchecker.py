def password_strength(password):


    if len(password)<8:
        
        print ('Weak!')

    if len(password)>=8 and password.isal and password.isalnum:
        print ('Strong!')
 
    else:
        print ('Moderate')
password = input("Please enter your password")
    
password_strength(password)