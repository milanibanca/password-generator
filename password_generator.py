import random
import string
import re
x = "abcdefghijklmnopqrstuvwxyzABCDEFGHIKLMONPQRTUVWXYZ"
special_characters = "!@#$%&*?"
password =""
print(password)
"""Loop that creats 12 random characters"""
for i in range(4):
    password+= random.choice(x)
    password += random.choice(special_characters)
    password += str(random.randint(0,9))
print(password,"The password length:",len(password))

"""Using the string module"""
all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
x =''.join(random.choices(all_chars,k=12))
print(x,"The password length: ",len(x))
