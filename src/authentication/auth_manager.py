# auth_manager.py

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def authenticate(username, password, users):
    """
    Authenticate the user based on the provided username and password.
    :param username: The username to authenticate.
    :param password: The password to authenticate.
    :param users: List of User objects representing registered users.
    :return: True if authentication is successful, False otherwise.
    """
    for user in users:
        if user.username == username and user.password == password:
            return True
    return False

# Example usage:
if __name__ == "__main__":
    # Assume we have a list of registered users
    registered_users = [
        User(username="admin", password="admin123"),
        User(username="user1", password="pass123"),
        User(username="user2", password="securepwd"),
    ]

    # Prompt for user input
    input_username = input("Enter your username: ")
    input_password = input("Enter your password: ")

    # Authenticate the user
    if authenticate(input_username, input_password, registered_users):
        print("Authentication successful. Welcome, {}!".format(input_username))
    else:
        print("Authentication failed. Invalid username or password.")
