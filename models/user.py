class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.role = None
    
    def add_user(self):
        self.role = "developer"
        if "@" and "." in self.email and self.name and self.email != "":
            print("add user is working")

    def view_user(self):
        pass

    def list_users(self):
        pass

    def edit_user(self):
        pass

    def delete_user(self):
        pass