from models import user
from models import task

# data handling

def load_data():
    pass
 

def save_data():
    pass

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
                print("3. Edit User")
                print("4. Edit Project")
                print("5. Delete User")
                print("6. Delete Project")
                print("7. Exit")
                print("8. Save Data")
                print()
                print()

                choice = input("Enter a number----").strip()
                if choice == "1":
                    title = input("Enter title/name of project----").strip()
                    description = input("Enter the description of the project----").strip()
                    due_date = input("Enter the due date of the project(DD-MM-YYYY)----").strip()
                    new_project = add_project(title, description, due_date)
                elif choice == "2":
                    name = input("Enter name----").strip()
                    email = input("Enter email----").strip()
                    new_user = user(name, email)

                elif choice == "3":
                    pass
                elif choice == "4":
                    pass
                elif choice == "5":
                    pass
                elif choice == "6":
                    pass
                elif choice == "7":
                    break
                elif choice == "8":
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
                    pass
                elif choice == "2":
                    pass
                elif choice == "3":
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
                    pass
                elif choice == "2":
                    project_name = input("Enter name of project task to be in----")
                    title = input("Enter title of task----")
                    status = input("Enter status of task----")
                    assigned_to = input("Enter name of person assigned to----")
                    new_task = task(project_name, title, status, assigned_to)
                elif choice == "3":
                    pass
                elif choice == "4":
                    break
                elif choice == "5":
                    save_data()
                else:
                    print("Try again, invalid input")
            elif choice == "4":
                break
            elif choice == "5":
                save_data()
            elif choice == "6":
                load_data()
            else:
                print("Try again, invalid input")
    finally:
        save_data()