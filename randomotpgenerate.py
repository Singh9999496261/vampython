# create first python project to generate 6 digit random otp

import random
otp=random.randrange(100000,1000000)
print(otp)
user = int(input("enter your otp :"))
if otp == user:
    print("access granted")
else :
    print("access denied")    