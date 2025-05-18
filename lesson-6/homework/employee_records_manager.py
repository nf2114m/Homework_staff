def main(number):
    if number==1:
        employee_id=input("Employee ID: ")
        name=input("Name: ")
        position=input("Position: ")
        salary=input("Salary: ")
        with open("employees.txt","a") as file:
            file.write(f"{employee_id},{name},{position},{salary}\n")
        print("Done!")
    if number==2:
        with open("employees.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                a,b,c,d=line.split(",")
                print(f"{a} | {b} | {c} | {d}")
    if number==3:
        s=input("search: ")
        with open("employees.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                    a,b,c,d=line.split(",")
                    if a==s:
                        print(f"{a} | {b} | {c} | {d}")
                        break
    if number==4:
        i=0
        s=input("search: ")
        with open("employees.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                    a,b,c,d=line.split(",")
                    if a==s:
                        print("Update")
                        employee_id=input("Employee ID: ")
                        name=input("Name: ")
                        position=input("Position: ")
                        salary=input("Salary: ")
                        lines[i]=f"{employee_id},{name},{position},{salary}\n"
                        with open("employees.txt","w") as file:
                            file.writelines(lines)
                        print("Updated!")
                    i=i+1
    if number==5:
        i=0
        s=input("Input ID to delete: ")
        with open("employees.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                    a,b,c,d=line.split(",")
                    if a==s:
                        del lines[i]
                        with open("employees.txt","w") as file:
                            file.writelines(lines)
                        print("Deleted!")
                    i=i+1

        
                                
            
        



while True:
    print("""1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit""")
    number=int(input("Enter a number: "))
    if number==6:
        break
    else:
        main(number)
    
