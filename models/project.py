class Project:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date

    def to_dict(self):
        print(f'Title: self.title')
        print(f'Description: self.description')
        print(f'Due Date: self.due_date')
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date
        }
    
    def add_project(self, title, description, due_date):
    #check for date and empty strings
        pass 

    def view_project(self):
        pass

    def list_projects(self):
        pass

    def update_project(self):
        pass

    def delete_project(self):
        pass