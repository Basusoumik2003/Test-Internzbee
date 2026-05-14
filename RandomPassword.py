import random
import string

pass_len = 7
charValues = string.ascii_letters + string.digits + string.punctuation


# List comprehension [function i in range(n)]

res = "".join([random.choice(charValues) for i in range(pass_len)])
print(res)
# password = ""
# for i in range(pass_len):
#     password += random.choice(charValues) 

# print("Your random password is:", password)