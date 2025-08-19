import random
import string

# Password Generator Program
print(" Welcome to the Password Generator!")
length = int(input("Enter the desired length of the password: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(length))
print("Your Generated Password is:", password)
