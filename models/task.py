from models import project

class Task:
    def __init__(self, title, status, assigned_to):
        self.title = title
        self.status = status
        self.assigned_to = assigned_to
    
    def to_dict(self):
        print(f'Title: self.title')
        print(f'Status: self.status')
        print(f'Assigned to: self.assigned_to')

        return {
            'title': self.title,
            'status': self.status,
            'assigned_to': self.assigned_to
        }