import string
import random
def password_generator(length=15):
    char=string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(char)for i in range(length))
    return password

if __name__ =="__main__":
    length=int(input("enter the length of password:"))

    if length > 0:
        password = password_generator(length)
        print(f"Generated password:{password}")

    else:
        print("Invalid input.Please give a valid input.")
