import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        
        password = generate_password(length)
        print(f"Generated Password: {password}")
        
    except ValueError as e:
        print(f"Error: {e}")
        print("Please enter a valid positive integer as the length.")

if __name__ == "__main__":
    main()
