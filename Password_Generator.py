# importing important modules
import random 
import string

# procedure to generate the password
def generate_password(length = 8):
    character = string.ascii_letters + string.digits + string.punctuation
    password = " ".join(random.choice(character) for _ in range(length))
    return password

# printing the password generated
print(generate_password())