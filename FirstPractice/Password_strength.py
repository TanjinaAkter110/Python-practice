def password_strength(user_input):
    
    

  
        if not user_input.isdigit() and not user_input.isalnum() and not user_input.isalpha ():
            return ('Strong!')
            
        elif len (user_input)<8 :
            return ('Weak: The password is too short!')
    
        else :
           return ('Moderate')
user_input= input('Please enter your password')
password= password_strength(user_input)

print (password)
