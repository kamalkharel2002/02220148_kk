import json

# this one loads the json file with a read operations to perform
def load_file():
    with open('lab2.json', 'r') as file:
        data = json.load(file)
    return data
# this will display the loaded json data
def display_students(data):
    for student in data["Student Record"]["students"]:
        print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")
        
# this will help to add the records by using the dictionary and saves the changes
def add_students():
    data = load_file() 
    id = int(input("Enter student ID: "))
    name = input("Enter student Name: ")
    age = int(input("Enter student Age: "))
    major = input("Enter student Major: ")

    for check in data['Student Record']['students']:
        if check['id'] == id:
            print("Student Already Exists")
            return

    new_std = {
        "id": id,
        "name": name,
        "age": age,
        "major": major
    }
    data["Student Record"]["students"].append(new_std)
    
    with open('lab2.json', 'w') as file:
        json.dump(data, file, indent=4)
    print("Student Added Successfully")

# this will delete the record based on the input matching the student ID
def delete_record():
    data = load_file() 
    id = int(input("Enter student ID to delete: "))
    
    for s in list(data["Student Record"]["students"]):  
        if s["id"] == id:
            data["Student Record"]["students"].remove(s)
            with open('lab2.json', 'w') as file:
                json.dump(data, file, indent=4)
            print("Student Deleted Successfully")
            return
    
    print("Student Not Found")

# Main loop for user interaction
data = load_file()
while True:
    print("1.Add Student,  2.Display Students,  3.Delete Student,  4.Exit")
    choose = input("Choose one to perform: ")
    
    if choose == "1": add_students()
    elif choose == "2": display_students(data)
    elif choose == "3": delete_record()
    elif choose == "4": break