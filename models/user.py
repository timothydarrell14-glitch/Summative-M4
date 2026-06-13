class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.role = None
    
    @classmethod
    def add_user(cls, name, email, users):
        if name == "" or email == "":
            print("**Ensure input fields are all filled**")
            return None

        if "@" in email and "." in email:
            user = {
                'name': name,
                'email': email
            }
            users.append(user)
            print("**User successfully added**")
            return user

        print("**Ensure input fields are all filled**")
        return None

    def view_user(self, name, users):
        for user in users:
            if user['name'] == name:
                print(user)

    def list_users(self, users):
        for user in users:
            print(user)