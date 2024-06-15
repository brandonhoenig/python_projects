
import random
import string 

all_characters = string.ascii_letters + string.digits + string.punctuation

length = int(input("Enter the length of the password: "))

password = ''.join(random.choices(all_characters, k=length))

print("Your password is:", password)


def generate_password(length, count = 1):
    passwords = []
    for i in range(count):
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        passwords.append(password)
    return passwords

generate_password(55)

