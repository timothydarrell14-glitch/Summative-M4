class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.role = None
    
    def add_user(self, name, email, users):
        self.role = "developer"
        if "@" and "." in email and name != "" and email != "":
            users.append({
                'name': {name},
                'email': {email}
            })
            print("**User successfully added**")

        else:
            print("**Ensure input fields are all filled**")

    def view_user(self, name, users):
        for user in users:
            if user['name'] == name:
                print(user)

    def list_users(self, users):
        for user in users:
            print(user)

    # def edit_user(self):
    #     pass

    # def delete_user(self):
    #     pass