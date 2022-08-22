import random
import string
s = string.ascii_letters + string.digits + string.punctuation
paswrd = random.choice(string.ascii_lowercase)
paswrd += random.choice(string.ascii_uppercase)
paswrd += random.choice(string.digits)
paswrd += random.choice(string.punctuation)
for i in range(6):
        paswrd += random.choice(s)
print("Your Password is  ", paswrd)