password =  (input('Enter your password: '))


if len(password) < 8:
    print ('very weak')
                
if len(password) == 8:
    print ('weak')
        
if len(password) > 8 and len(password) <= 16:
    print ('strong')
        
if len(password) > 16:
    print ('very strong')
         
                
