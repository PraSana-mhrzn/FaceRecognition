class Employee:
    def __init__(self, emp_id, name, department, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.base_salary = base_salary
        self.attendance = []

    def mark_attendance(self, date, present):
        self.attendance.append((date, present))

    def calculate_salary(self):
        total_days = len(self.attendance)
        if total_days == 0:
            return 0

        # Define attendance rules based on department (you can customize these rules)
        attendance_rules = {
            'HR': 0.9,  # HR department: 90% attendance required
            'IT': 0.85,  # IT department: 85% attendance required
            'Finance': 0.88  # Finance department: 88% attendance required
            # Add more department rules as needed
        }

        required_attendance = total_days * attendance_rules.get(self.department, 0.9)
        actual_attendance = sum(present for _, present in self.attendance)

        attendance_percentage = actual_attendance / required_attendance

        # Calculate salary based on attendance percentage
        salary = self.base_salary * attendance_percentage
        return salary


# Sample usage of the Employee class
if __name__ == "__main__":
    # Create employees
    employee1 = Employee(1, "John", "HR", 5000)
    employee2 = Employee(2, "Alice", "IT", 6000)
    employee3 = Employee(3, "Bob", "Finance", 5500)

    # Mark attendance for employees
    employee1.mark_attendance("2023-09-20", 1)  # Present
    employee1.mark_attendance("2023-09-21", 0)  # Absent
    employee2.mark_attendance("2023-09-20", 1)  # Present
    employee2.mark_attendance("2023-09-21", 1)  # Present
    employee3.mark_attendance("2023-09-20", 0)  # Absent
    employee3.mark_attendance("2023-09-21", 1)  # Present

    # Calculate salaries
    salaries = {
        employee1.name: employee1.calculate_salary(),
        employee2.name: employee2.calculate_salary(),
        employee3.name: employee3.calculate_salary(),
    }

    # Print calculated salaries
    for name, salary in salaries.items():
        print(f"{name}'s Salary: ${salary:.2f}")















"""import pymongo

# Step 1: Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI
db = client["company"]  # Replace "company" with your database name
attendance_collection = db["attendance"]  # Replace "attendance" with your collection name
employees_collection = db["employees"]  # Replace "employees" with your collection name

# Step 2: Retrieve attendance data for each employee
for employee in employees_collection.find():
    employee_id = employee["_id"]
    department = employee["department"]
    # Retrieve attendance records for the employee
    attendance_records = attendance_collection.find({"employee_id": employee_id})

    # Step 3: Calculate salary based on attendance records and department-specific rules
    total_attendance = attendance_records.count()  # Calculate total attendance
    department_rules = {
        "HR": {"base_salary": 5000, "bonus_per_attendance": 100},
        "IT": {"base_salary": 6000, "bonus_per_attendance": 150},
        "Sales": {"base_salary": 5500, "bonus_per_attendance": 120},
        # Add rules for other departments
    }

    if department in department_rules:
        department_rule = department_rules[department]
        base_salary = department_rule["base_salary"]
        bonus_per_attendance = department_rule["bonus_per_attendance"]
        salary = base_salary + (bonus_per_attendance * total_attendance)
    else:
        # Handle departments without rules
        salary = 0  # Set a default salary or handle as needed

    # Step 4: Update the employee's salary in the database
    employees_collection.update_one(
        {"_id": employee_id},
        {"$set": {"salary": salary}}
    )

# Close the database connection
client.close()"""
