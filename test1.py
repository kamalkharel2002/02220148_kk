import xml.etree.ElementTree as ET

tree = ET.parse('lab1.xml') 
root = tree.getroot()

# Iterate through all students
for student in root.findall('student'):
    student_id = student.get('id')
    name = student.find('name').text
    department = student.find('department').text
    email = student.find('email').text
    year = student.find('year').text

    print(f"""
{{
  "id": "{student_id}",
  "name": "{name}",
  "department": "{department}",
  "email": "{email}",
  "year": "{year}"
}}
""")