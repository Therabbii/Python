password =  (input('Enter your password: '))

#while len(password) < 8:

if len(password) < 8:
         print ('very weak')
                
if len(password) == 8:
        print ('weak')
                
if len(password) > 8:
        print ('strong')
                
if len(password) > 16:
        print ('very strong')
         
                
