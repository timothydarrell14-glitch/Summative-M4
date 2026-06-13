class Project:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date

    @classmethod
    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date
        }

    def add_project(self, title, description, due_date, projects):
        from datetime import datetime

        if title == "" or description == "" or due_date == "":
            print("**Please make sure all input fields are not empty**")
        
        else:
            date = datetime.strptime(due_date, "%d-%m-%Y")
            
            if due_date == date:
                projects.append({
                    'title': title,
                    'description': description,
                    'due_date': due_date
                    })
                print("Project successfully added")

            else:
                print("Write the date in this format(DD-MM-YYYY)")
            

    def view_project(self, title):
        pass

    def update_project(self):
        pass

    def delete_project(self):
        pass