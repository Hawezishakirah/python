#lists are mutable, it works with index
#item stored should be the same
student_names = ['Sandra','Patricia','Phionah','Anitah']#strings
student_marks = [80,56,78,90]#integers
data = ['Sandra',90, 'Kamwokya'] #mixed types

#access the whole list
print(student_names, type(student_names))

#accessing list items
#indexes (positive indexing)
#these are arrays and we use indexes
print(student_names[0]) #first item
print(student_names[1]) #second item
print(student_names[2]) #third item
print(student_names[3]) #last item

#indexes(negative indexing)
print(student_names[-4]) #first item
print(student_names[-3]) #second item
print(student_names[-2]) #third item
print(student_names[-1]) #last item

#adding new items to the list
#at the end
student_names.append('bright')
print(student_names)

#at a particular position
student_names.insert(2,'queen')
print(student_names)

# assignment
# print Patricia,Faith and Anitah
# add masha at the fourth position
# update the name Phionah to Phionah Aladina
# display the length of the student list
# print all the students names using a 'for' loop
# calculate the total marks for the student marks variable

#answers
#(a)
student_names = ['Patricia','Faith','Anitah']
#Get the first two names
slice1 = student_names[0:2]#['Patricia','Faith']
#Get the last name
slice2 = student_names[2:]#['Anitah']
#Get all names with a step of 1(same as the original list)
slice3 = student_names[:]#['Patricia','Faith','Anitah']
#Get every second name
slice4 = student_names[::2]#['Patricia','Anitah']

#or
names = ["Patricia","Faith","Anitah"]
for name in names:
    print(name)

#(b)
student_names.insert(4,'Masha')
print(student_names)

#(c)
updated_name = name.replace("Phionah","Phionah Aladina")
print(updated_name)
#or
names = ["Patricia","Faith","Anitah","Phionah"]
index = names.index('Phionah')
names[index] = "Phionah Aladina"
print(names)

#(d)
student_names =["Patricia","Faith","Anitah","Phionah Aladina"]

for student in student_names:
    print(f"The length of {student} is {len(student_names)}")
    #or
    students = ["Patricia","Faith","Anitah","Phionah Aladina"]
    lengths = [len(student) for student in student]
    print(lengths)

    #(e)
student_names = ["Patricia","Faith","Anitah","Phionah Aladina"]
for student in student_names:
    print(student_names)

#(f)
student_marks = [80,56,78,90]
total_marks = sum(student_marks)
print(f"The total marks for the students is:{total_marks}")