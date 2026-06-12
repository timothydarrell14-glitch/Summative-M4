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
    def add_task(cls, project_name, title, status, assigned_to):
        pass

    def view_tasks_for_project(self):
        pass

    def view_task(self):
        pass

    def edit_task(self):
        pass

    def delete_task(self):
        pass

# change status of task