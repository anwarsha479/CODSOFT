import string
import random
def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    all_characters = lower + upper + digits + symbols
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password
def main():
    while True:
        try:
            length = int(input("Enter the desired length for your password: "))
            if length <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    password = generate_password(length)
    print(f"Generated Password: {password}")
if __name__ == "__main__":
    main()
