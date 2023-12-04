import hashlib
import getpass

class PasswordManager:
    def __init__(self):
        self.user_credentials = {}
        self.program_passwords = {}

    def register_user(self, username, password):
        if username not in self.user_credentials:
            hashed_password = self._hash_password(password)
            self.user_credentials[username] = hashed_password
            self.program_passwords[username] = {}
            print(f"User {username} registered successfully.")
        else:
            print("Username already exists. Please choose a different one.")

    def login_user(self, username, password):
        if username in self.user_credentials:
            hashed_password = self.user_credentials[username]
            if self._hash_password(password) == hashed_password:
                print("Login successful.")
                return True
            else:
                print("Incorrect password. Please try again.")
        else:
            print("Username not found. Please register.")
        return False

    def store_password(self, username, program, password):
        if username in self.program_passwords:
            self.program_passwords[username][program] = password
            print(f"Password for {program} stored successfully.")
        else:
            print("User not found. Please login or register.")

    def view_passwords(self, username):
        if username in self.program_passwords:
            print("Stored Passwords:")
            for program, password in self.program_passwords[username].items():
                print(f"{program}: {password}")
        else:
            print("User not found. Please login or register.")

    def _hash_password(self, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

# Example Usage
password_manager = PasswordManager()

while True:
    print("\n1. Register\n2. Login\n3. Store Password\n4. View Passwords\n5. Exit")
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")
        password_manager.register_user(username, password)
    elif choice == "2":
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")
        if password_manager.login_user(username, password):
            while True:
                inner_choice = input("1. Store Password\n2. View Passwords\n3. Logout\nEnter your choice (1/2/3): ")
                if inner_choice == "1":
                    program = input("Enter the program name: ")
                    password = getpass.getpass(f"Enter the password for {program}: ")
                    password_manager.store_password(username, program, password)
                elif inner_choice == "2":
                    password_manager.view_passwords(username)
                elif inner_choice == "3":
                    print("Logging out.")
                    break
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")
    elif choice == "3":
        print("Please login to store passwords.")
    elif choice == "4":
        print("Please login to view passwords.")
    elif choice == "5":
        print("Logout Successful.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
