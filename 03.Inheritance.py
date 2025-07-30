'''
3. Inheritance
#Inheritance lets one class reuse the code of another.
#It’s like a child copying useful features from a parent and adding its own.
 
=> Example: User and Admin
(An Admin is also a User, but with extra powers like deleting accounts.
Instead of writing the same login system again, we reuse the User class inside Admin.)

Example Code:
-------------
# Define parent class
class User:
    def __init__(self, username):
        self.username = username

    def login(self):
        print(self.username, "logged in.")

# Define child class
class Admin(User):
    def delete_user(self):
        print(self.username, "deleted a user.")

# Create object of child class
admin1 = Admin("superadmin")  # Object created with inherited properties
admin1.login()
admin1.delete_user()

Output:
        superadmin logged in.
        superadmin deleted a user.
'''
