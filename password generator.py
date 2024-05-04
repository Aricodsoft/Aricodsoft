import random
import string

def generate_password(length):
    if length < 1:
        raise ValueError("Password length must be at least 1")

    char_list = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + string.digits
        + string.punctuation
    )

    password = []
    for _ in range(length):
        password.append(random.choice(char_list))

    return ''.join(password)

password_length = int(input("Please enter the desired password length (minimum 12 for a secure password): "))

if password_length < 12:
    print("For a more secure password, consider using a length of at least 12 characters.")

generated_password = generate_password(password_length)

print("The generated secure password is: {}".format(generated_password))