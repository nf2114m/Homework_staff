class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename

    def add_employee(self):
        employee_id = input("Employee ID: ")
        name = input("Name: ")
        position = input("Position: ")
        salary = input("Salary: ")
        with open(self.filename, "a") as file:
            file.write(f"{employee_id},{name},{position},{salary}\n")
        print("Done!")

    def view_all_employees(self):
        with open(self.filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                a, b, c, d = line.strip().split(",")
                print(f"{a} | {b} | {c} | {d}")

    def search_employee(self):
        s = input("Search by Employee ID: ")
        with open(self.filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                a, b, c, d = line.strip().split(",")
                if a == s:
                    print(f"{a} | {b} | {c} | {d}")
                    break
            else:
                print("Employee not found.")

    def update_employee(self):
        s = input("Search by Employee ID to update: ")
        with open(self.filename, "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            a, b, c, d = line.strip().split(",")
            if a == s:
                print("Update employee information.")
                employee_id = input("Employee ID: ")
                name = input("Name: ")
                position = input("Position: ")
                salary = input("Salary: ")
                lines[i] = f"{employee_id},{name},{position},{salary}\n"
                with open(self.filename, "w") as file:
                    file.writelines(lines)
                print("Updated!")
                return
        print("Employee not found.")

    def delete_employee(self):
        s = input("Input Employee ID to delete: ")
        with open(self.filename, "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            a, b, c, d = line.strip().split(",")
            if a == s:
                del lines[i]
                with open(self.filename, "w") as file:
                    file.writelines(lines)
                print("Deleted!")
                return
        print("Employee not found.")

def main():
    manager = EmployeeManager()

    while True:
        print("""1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit""")
        number = int(input("Enter a number: "))
        if number == 6:
            break
        elif number == 1:
            manager.add_employee()
        elif number == 2:
            manager.view_all_employees()
        elif number == 3:
            manager.search_employee()
        elif number == 4:
            manager.update_employee()
        elif number == 5:
            manager.delete_employee()
        else:
            print("Invalid input. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
