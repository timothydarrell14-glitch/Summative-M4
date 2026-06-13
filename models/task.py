from models import project

class Task:
    def __init__(self, project, title, status, assigned_to):
        self.project = project
        self.title = title
        self.status = status
        self.assigned_to = assigned_to
    
    def to_dict(self):
        print(f'Title: {self.title}')
        print(f'Status: {self.status}')
        print(f'Assigned to: {self.assigned_to}')

        return {
            'project': self.project,
            'title': self.title,
            'status': self.status,
            'assigned_to': self.assigned_to
        }

    @classmethod
    def add_task(cls, project_name, title, status, assigned_to, tasks):
        if project_name == "" or title == "" or status == "" or assigned_to == "":
            print("**Please ensure all input fields are filled**")
            return None
        task = {
            'project': project_name,
            'title': title,
            'status': status,
            'assigned_to': assigned_to
        }
        tasks.append(task)
        print("**Task added successfully**")
        return task

    @classmethod
    def view_tasks_for_project(cls, project_name, tasks):
        for task in tasks:
            if task['project'] == project_name:
                print(task)

    def view_task(self, name, tasks):
        for task in tasks:
            if task['title'] == name:
                print(task)