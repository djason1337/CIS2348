# 2203959 Dominic Jason

import csv
import datetime


# AI USED
# Prompt: How can I sort dictionary items in python without the use of databases, lambda, itemgetter, or databases?
# Yes, the original output was modified to suit the needs of the project.
# No follow up questions were asked.
# I learned that it was possible to create a key to sort certain items,
# and that you do not always have to use lambda to accomplish that.


# create keys for sorting
def last_name(student):
    return student['last_name']


def id(student):
    return student['id']


def gpa(student):
    return float(student['gpa'])


def graduation_date(student):
    return datetime.datetime.strptime(student['graduation_date'], "%m/%d/%Y").date()


# Read inputs from majors file
majors = []
with open('StudentsMajorsList-3.csv', 'r') as file:
    for line in file:
        majors.append(line.strip().split(','))

# read inputs from gpas file
gpas = []
with open('GPAList-1.csv', 'r') as file:
    for line in file:
        gpas.append(line.strip().split(','))

# read inputs from graduation dates file
grad_dates = []
with open('GraduationDatesList-1.csv', 'r') as file:
    for line in file:
        grad_dates.append(line.strip().split(','))

# sort each list
majors.sort()
gpas.sort()
grad_dates.sort()


# Initialize students list, create list of entire student data with corresponding dict key and values
students = []
for data in zip(majors, gpas, grad_dates):
    student = {
        'id': data[0][0], 'major': data[0][3], 'first_name': data[0][2], 'last_name': data[0][1], 'gpa': data[1][1], 'graduation_date': data[2][1], 'disciplined': data[0][4]}
    students.append(student)


# sort student list by last name
students = sorted(students, key=last_name)


# Function for creating full roster file
def full_roster():
    with open('FullRoster.csv', 'w', newline='') as file:
        for student in students:
            csv.writer(file).writerow([student['id'], student['major'], student['first_name'], student['last_name'], student['gpa'], student['graduation_date'], student['disciplined']])


# function to sort students by major and create csv files for each
def list_majors(students):
    majors = {}
    for student in students:
        major = student['major'].replace(' ', '')
        if major not in majors:
            majors[major] = []
        majors[major].append(student)

    for major, students in majors.items():
        students.sort(key=id)
        with open(f'{major}Students.csv', 'w', newline='') as file:
            for student in students:
                csv.writer(file).writerow([student['id'], student['last_name'], student['first_name'], student['graduation_date'], student['disciplined']])


# check if a student has graduated
def graduated(student):
    graduation_date = datetime.datetime.strptime(student['graduation_date'], "%m/%d/%Y").date()
    return graduation_date < datetime.date.today()


# create scholarship candidates file
def scholarship_candidates():
    # create list of eligible students
    scholarship_students = [student for student in students if float(student['gpa']) > 3.8 and not graduated(student) and student['disciplined'] != 'Y']

    # sort students by GPA from highest to lowest
    scholarship_students.sort(key=gpa, reverse=True)

    with open('ScholarshipCandidates.csv', 'w', newline='') as file:

        for student in scholarship_students:

            csv.writer(file).writerow([student['id'], student['last_name'], student['first_name'], student['major'], student['gpa']])


# create list of disciplined students, print them to output csv
def disciplined_students():
    disciplined = [student for student in students if student['disciplined'] == 'Y']
    disciplined.sort(key=graduation_date)

    with open('DisciplinedStudents.csv', 'w', newline='') as file:
        for student in disciplined:
            csv.writer(file).writerow([student['id'], student['last_name'], student['first_name'], student['graduation_date']])


# interactive functionality
def query_student(major_query, gpa_query):
    queried_students = [student for student in students if student['major'].lower() == major_query.lower() and float(student['gpa']) - gpa_query <= 0.1 and not graduated(student) and student['disciplined'] != 'Y']
    if not queried_students:
        print("No such student")
    else:
        print("Your student(s):")
        for student in queried_students:
            print(f"ID: {student['id']}, First Name: {student['first_name']}, Last Name: {student['last_name']}, GPA: {student['gpa']}")

    # query for students within 0.25 of the requested GPA
    similar_students = [student for student in students if gpa_query - 0.25 <= float(student['gpa']) <= gpa_query + 0.25 and not graduated(student) and student['disciplined'] != 'Y']
    if similar_students:
        print("You may, also, consider:")
        for student in similar_students:
            print(f"ID: {student['id']}, First Name: {student['first_name']}, Last Name: {student['last_name']}, GPA: {student['gpa']}")

# if no students satisfied the above conditions, find the student with the closest GPA
    if not queried_students and not similar_students:
        closest_gpa_diff = float('inf')
        closest_student = None
        for student in students:
            if student['major'].lower() == major_query.lower() and not graduated(student) and student['disciplined'] != 'Y':
                gpa_diff = abs(float(student['gpa']) - gpa_query)
                if gpa_diff < closest_gpa_diff:
                    closest_gpa_diff = gpa_diff
                    closest_student = student
        if closest_student is not None:
            print("The student with the closest GPA is:")
            print(f"ID: {closest_student['id']}, First Name: {closest_student['first_name']}, Last Name: {closest_student['last_name']}, GPA: {closest_student['gpa']}")


# run until user inputs q
while True:
    user_input = input("Please enter the major and GPA separated by a space (or 'q' to quit): ")

    if user_input.lower() == 'q':
        break

    user_input = user_input.split()

    if len(user_input) < 2:
        print("Invalid input. Please enter the major and GPA separated by a space.")
        continue

    major_query = " ".join(user_input[:-1])
    gpa_query = float(user_input[-1])

    query_student(major_query, gpa_query)


# execute functions and create csv files

try:

    list_majors(students)

    full_roster()

    scholarship_candidates()

    disciplined_students()

    print('Yay! All files were created successfully!')

except:
    print('Oh no! An error has occurred')
