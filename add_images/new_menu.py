"""
Provides a basic frontend
"""
import sys
import main
import shutil
from pathlib import Path

def load_users():
    """
    Loads user accounts from a file
    """
    filename = input('Enter filename of user file: ')
    main.load_users(filename)


def load_status_updates():
    """
    Loads status updates from a file
    """
    filename = input('Enter filename for status file: ')
    main.load_status_updates(filename)


def add_user():
    """
    Adds a new user into the database
    """
    user_id = input('User ID: ')
    email = input('User email: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')

    if not main.add_user(user_id,
                         email,
                         user_name,
                         user_last_name):
        print("An error occurred while trying to add new user")
    else:
        print("User was successfully added")


def update_user():
    """
    Updates information for an existing user
    """
    user_id = input('User ID: ')
    email = input('User email: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')
    if not main.update_user(user_id, email, user_name, user_last_name):
        print("An error occurred while trying to update user")
    else:
        print("User was successfully updated")


def search_user():
    """
    Searches a user in the database
    """

    user_id = input('Enter user ID to search: ')
    result = main.search_user(user_id)
    if not result:
        print("ERROR: User does not exist")
    else:
        print(f"User ID: {result['user_id']}")
        print(f"Email: {result['email']}")
        print(f"Name: {result['user_name']}")
        print(f"Last name: {result['user_last_name']}")


def delete_user():
    """
    Deletes user from the database
    """
    user_id = input('User ID: ')
    if not main.delete_user(user_id):
        print("An error occurred while trying to delete user")
    else:
        print("User was successfully deleted")


def add_status():
    """
    Adds a new status into the database
    """
    user_id = input('User ID: ')
    status_id = input('Status ID: ')
    status_text = input('Status text: ')
    if not main.add_status(status_id, user_id, status_text):
        print("An error occurred while trying to add new status")
    else:
        print("New status was successfully added")


def update_status():
    """
    Updates information for an existing status
    """
    user_id = input('User ID: ')
    status_id = input('Status ID: ')
    status_text = input('Status text: ')
    if not main.update_status(status_id, user_id, status_text):
        print("An error occurred while trying to update status")
    else:
        print("Status was successfully updated")


def search_status():
    """
    Searches a status in the database
    """
    status_id = input('Enter status ID to search: ')
    result = main.search_status(status_id)
    if not result:
        print("ERROR: Status does not exist")
    else:
        print(f"User ID: {result['user_id']}")
        print(f"Status ID: {result['status_id']}")
        print(f"Status text: {result['status_text']}")


def delete_status():
    """
    Deletes status from the database
    """
    status_id = input('Status ID: ')
    if not main.delete_status(status_id):
        print("An error occurred while trying to delete status")
    else:
        print("Status was successfully deleted")

def add_picture():
    user_id = input('Enter user id: ')
    tags = input('Enter picture tags: ')
    main.add_picture(user_id, tags)

def list_images():
    user_id = input('Enter user id: ')
    main.list_images(user_id)

def reconcile_images():
    main.reconcile_images()

def quit_program():
    """
    Quits program
    """
    path = Path.cwd() / 'images'
    if path.exists():
        shutil.rmtree(path)
    sys.exit()

if __name__ == '__main__':
    # clear old images
    # path = Path.cwd() / 'images'
    # if path.exists():
    #     shutil.rmtree(path)
    # path.mkdir(exist_ok=False)

    menu_options = {
        'A': load_users,
        'B': load_status_updates,
        'C': add_user,
        'D': update_user,
        'E': search_user,
        'F': delete_user,
        'H': add_status,
        'I': update_status,
        'J': search_status,
        'K': delete_status,
        'L': add_picture,
        'P': list_images,
        'O': reconcile_images,
        'Q': quit_program
    }

    while True:
        user_selection = input("""
                                    A: Load user database
                                    B: Load status database
                                    C: Add user
                                    D: Update user
                                    E: Search user
                                    F: Delete user
                                    H: Add status
                                    I: Update status
                                    J: Search status
                                    K: Delete status
                                    L: Add picture
                                    P: List images
                                    O: List picture discrepancies
                                    Q: Quit

                                    Please enter your choice: """)

        if user_selection.upper() in menu_options:
            menu_options[user_selection.upper()]()
        else:
            print("Invalid option")
