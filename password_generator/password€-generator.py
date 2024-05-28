import random
import string

def generate_password(length):
    if length < 4:
        return "Error: Password length should be at least 4 to ensure complexity."

    all_characters = string.ascii_letters + string.digits + string.punctuation

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    password += random.choices(all_characters, k=length-4)

    random.shuffle(password)

    return ''.join(password)

def main():
    print("Password Generator")
    
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
            password = generate_password(length)
            print(f"Generated Password: {password}")
            
            another = input("Generate another password? (yes/no): ")
            if another.lower() != 'yes':
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
