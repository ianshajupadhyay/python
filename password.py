password = input ('type your password ....')

weak = 'weak'
med = 'medium'
strong = 'strong'

if len(password) >12:
 print ('password is too long It must be between 6 and 12 characters')

elif len(password) <6:
 print ('password is too short It must be between 6 and 12 characters')

elif len(password) >=6 and len(password) <= 12:
 print ('password ok')

if password.lower()== password or password.upper()==password or password.isalnum()==password:
 print ('password is', weak)

elif password.lower()== password and password.upper()==password or password.isalnum()==password:
 print ('password is', med)

else:
 password.lower()== password and password.upper()==password and password.isalnum()==password
 print ('password is', strong)


