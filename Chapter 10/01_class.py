class Employee: 
    language = "Py" # This is a class attribute
    salary = 1200000


jude = Employee()
jude.name = "Jude" # This is an instance attribute
print(jude.name, jude.language, jude.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.salary, rohan.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class