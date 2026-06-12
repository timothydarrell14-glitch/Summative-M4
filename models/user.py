class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_dict(self):
        print(f'Name: self.name')
        print(f'Email: self.email')
        return {
            'name': self.name,
            'email': self.email
        }