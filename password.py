import random
import string

charvalues= string.ascii_letters + string.digits 
password_len= random.randint(8,12)
password= "".join([random.choice(charvalues) for i in range(password_len)])
print(password)