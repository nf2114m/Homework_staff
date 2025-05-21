class Task:
    def __init__(self, task_id, title, description, due_date="", status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_record(self):
        return f"{self.task_id}|{self.title}|{self.description}|{self.due_date}|{self.status}"

    @classmethod
    def from_record(cls, line):
        parts = line.strip().split("|")
        if len(parts) == 5:
            return cls(*parts)
        return None

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"


class TxtStorage:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename

    def load(self):
        tasks = []
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    task = Task.from_record(line)
                    if task:
                        tasks.append(task)
        except FileNotFoundError:
            pass
        return tasks

    def save(self, tasks):
        with open(self.filename, "w") as f:
            for task in tasks:
                f.write(task.to_record() + "\n")


class ToDoManager:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load()

    def find_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def add_task(self):
        task_id = input("Enter Task ID: ")
        if self.find_task(task_id):
            print("Task ID already exists.")
            return
        title = input("Enter Title: ")
        desc = input("Enter Description: ")
        due = input("Enter Due Date (YYYY-MM-DD, optional): ")
        status = input("Enter Status (Pending/In Progress/Completed): ")
        self.tasks.append(Task(task_id, title, desc, due, status))
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        for task in self.tasks:
            print(task)

    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        task = self.find_task(task_id)
        if not task:
            print("Task not found.")
            return
        title = input(f"Title [{task.title}]: ") or task.title
        desc = input(f"Description [{task.description}]: ") or task.description
        due = input(f"Due Date [{task.due_date}]: ") or task.due_date
        status = input(f"Status [{task.status}]: ") or task.status
        task.title = title
        task.description = desc
        task.due_date = due
        task.status = status
        print("Task updated successfully!")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        before_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        if len(self.tasks) < before_count:
            print("Task deleted.")
        else:
            print("Task not found.")

    def filter_tasks(self):
        status = input("Enter status to filter (Pending/In Progress/Completed): ")
        filtered = [task for task in self.tasks if task.status.lower() == status.lower()]
        if not filtered:
            print("No tasks with this status.")
        else:
            for task in filtered:
                print(task)

    def save_tasks(self):
        self.storage.save(self.tasks)
        print("Tasks saved to file.")

    def load_tasks(self):
        self.tasks = self.storage.load()
        print("Tasks loaded from file.")


def main():
    manager = ToDoManager(TxtStorage())

    while True:
        print("\nWelcome to the To-Do Application!")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Exit")

        choice = input("Enter your choice: ")
        match choice:
            case "1": manager.add_task()
            case "2": manager.view_tasks()
            case "3": manager.update_task()
            case "4": manager.delete_task()
            case "5": manager.filter_tasks()
            case "6": manager.save_tasks()
            case "7": manager.load_tasks()
            case "8":
                print("Goodbye!")
                break
            case _: print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
