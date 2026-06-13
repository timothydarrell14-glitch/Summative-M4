class Project:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date
        }

    @classmethod
    def add_project(cls, title, description, due_date, projects):
        from datetime import datetime

        if title == "" or description == "" or due_date == "":
            print("**Please make sure all input fields are not empty**")
            return None

        try:
            datetime.strptime(due_date, "%d-%m-%Y")
        except ValueError:
            print("Write the date in this format(DD-MM-YYYY)")
            return None

        project = {
            'title': title,
            'description': description,
            'due_date': due_date
        }
        projects.append(project)
        print("Project successfully added")
        return project