from models.user import User
from models.task import Task
from models.project import Project
import os
import json
from importlib import resources

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
task_data = os.path.join(BASE_DIR, 'data', 'tasks.json')
user_data = os.path.join(BASE_DIR, 'data', 'users.json')
project_data = os.path.join(BASE_DIR, 'data', 'projects.json')

tasks = []
users = []
projects = []


def load_data():
    global tasks, users, projects

    with resources.open_text("data", "tasks.json") as f:
        tasks = json.load(f)
    
    with resources.open_text("data", "users.json") as f:
        users = json.load(f)

    with resources.open_text("data", "projects.json") as f:
        projects = json.load(f)

    # print(tasks)
    # print(users)
    # print(projects)

def save_data():
    os.makedirs(os.path.dirname(task_data), exist_ok=True)

    with open(task_data, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2)

    with open(user_data, 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=2)

    with open(project_data, 'w', encoding='utf-8') as f:
        json.dump(projects, f, indent=2)

# display menu

# -------> Admin/Employee
# -------> Admin-> Edit - Add - Delete User/Project
# -------> Employee-> View projects, view tasks
# -------> Project -> List of projects, add task, list of tasks in project
# ****include tasks in project object ****
def run():
    """Run the admin CLI loop."""
    load_data()
    try:
        while True:
            print("======CLI======")
            print()
            print()
            print("1. Admin")
            print("2. User")
            print("3. Project")
            print("4. Exit")
            print("5. Save data")
            print("6. Load Data")
            print()
            print()

            choice = input("Enter a number----").strip()

            if choice == "1":
                print("=====ADMIN=====")
                print()
                print()
                print("1. Add Project")
                print("2. Add User")
                # print("3. Edit User")
                # print("4. Edit Project")
                # print("5. Delete User")
                # print("6. Delete Project")
                print("3. Exit")
                print("4. Save Data")
                print()
                print()

                choice = input("Enter a number----").strip()
                if choice == "1":
                    title = input("Enter title/name of project----").strip()
                    description = input("Enter the description of the project----").strip()
                    due_date = input("Enter the due date of the project(DD-MM-YYYY)----").strip()
                    new_project = Project.add_project(title, description, due_date, projects)
                    print(new_project)

                elif choice == "2":
                    name = input("Enter name----").strip()
                    email = input("Enter email----").strip()
                    new_user = User.add_user(name, email, users)
                    print(new_user)

                # elif choice == "3":
                #     pass
                # elif choice == "4":
                #     pass
                # elif choice == "5":
                #     pass
                # elif choice == "6":
                #     pass
                elif choice == "3":
                    save_data()
                    break
                elif choice == "4":
                    save_data()
                else:
                    print("Try again, invalid input")

            elif choice == "2":
                print("====USER====")
                print()
                print()
                print("1. View Projects")
                print("2. View Tasks assigned")
                print("3. Exit")
                print("4. Save data")
                print()
                print()

                choice = input("Enter a choice----").strip()
                if choice == "1":
                    for project in projects:
                        print(project)
                elif choice == "2":
                    name = input("Enter name")
                    for task in tasks:
                        if name in task['assigned_to']:
                            print(task)
                elif choice == "3":
                    save_data()
                    break
                elif choice == "4":
                    save_data()
                else:
                    print("Try again, invalid input")
            elif choice == "3":
                print("====PROJECTS====")
                print()
                print()
                print("1. List projects")
                print("2. Add Task")
                print("3. List of tasks in project")
                print("4. Exit")
                print("5. Save Data")
                print()
                print()

                choice = input("Enter a number----").strip()

                if choice == "1":
                    for project in projects:
                        print(project)
                elif choice == "2":
                    project_name = input("Enter name of project task to be in----")
                    if project_name in [project['title'] for project in projects]:
                        title = input("Enter title of task----")
                        status = input("Enter status of task----")
                        assigned_to = input("Enter name of person assigned to----")
                        new_task = Task.add_task(project_name, title, status, assigned_to, projects)
                        print(new_task)
                    else:
                        print("Please enter a valid project")
                elif choice == "3":
                    name = input("Enter project name")
                    Task.view_tasks_for_project(name, tasks)
                elif choice == "4":
                    break
                elif choice == "5":
                    save_data()
                else:
                    print("Try again, invalid input")
            elif choice == "4":
                save_data()
                break
            elif choice == "5":
                save_data()
            elif choice == "6":
                load_data()
            else:
                print("Try again, invalid input")
    finally:
        save_data()