#function is always used in programming to perform a particular task
#incase there is no function name we pass
#create a function that returns the main components of functions, the output 
#should say main
def function_basics():
    print('main components of functins are parameters,function name,arguments,function calls')
function_basics()

#create a function that returns your student name, reg number and your student age
def student_details():
    student_name='hawezi shakirah'
    student_age=20
    reg_number='2024/dsc/0036/ss'
    print(f'student_details with  student_name {student_name} , student_age {student_age} , reg_number {reg_number}')
student_details()

#global variable
marks = 90
print(marks)

#parameters
#create a function that returns your student_name,student_age and reg_number as parameters
def student_details_parameters(student_name,student_age, reg_number):
    print(f'the student_data with student_name{ student_name},student_age{student_age} , reg_number{reg_number}')
student_details_parameters('shakirah',20,'2024/dsc/0036/ss')

#return values(instead of print we can use return)
def my_name():
    return "shakirah"
#approach_2
def my_name_twq():
    name = "shakirah"
    return name
def my_age():
    age = 20
    return age

print(f" i am {my_age()}years old")
#or 
def my_name_parameter(name):
    return name
my_name_parameter('shakirah')

#create a function that calculates the area of a triangle the base and height must be function parameters
def area_of_triangle(base,height):
    area = (1/2)*base*height
    print(f' The area of a triangle: base{base},height{height}')
area_of_triangle(2,4)

#apprach_two
def area_of_triangle(base,height):
    base = int(input("enter the base:"))
    height = int(input("enter the height:"))
    area = int((1/2)*base*height)
    print(f' The area of a triangle: base{base},height{height}')
area_of_triangle(2,4)