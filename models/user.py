class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_dict(self, name, email):
        print(f'Name: self.name')
        print(f'Email: self.email')
        return {
            'name': self.name,
            'email': self.email
        }
    
    def add_user(self, name, email):
        self.role = "developer"
        if "@" and "." in self.email and self.name and self.email != "":
            print("User is working")

    def view_user(self):
        pass

    def list_users(self):
        pass

    def edit_user(self):
        pass

    def delete_user(self):
        pass