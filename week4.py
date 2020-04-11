grade_one= {'Sami': [19, 18, 19.5, 30, 10],
 'Ahmad': [15, 14, 16, 21, 7],
  'Faris': [18, 19, 17, 26, 9],
  'Salem': [20, 20, 19, 30, 10],
   'Mahmoud': [12, 13, 11, 18, 7]}
grade_two= {'Lana': [17, 19, 20, 28, 9],
 'Dina': [18.5, 19.5, 20, 29, 10],
  'Maha': [20, 20, 18, 26, 9],
   'Abeer': [16, 18, 19.5, 25, 8]}
grade_three= {'Rima': [18, 19, 18, 26, 9],
              'Tala': [20, 20, 19, 29, 10],
              'Lamar': [19, 20, 18, 26, 9],
              'Rola': [15, 14, 16, 19, 7],
              'Naya': [9, 6, 11, 14, 7],
              'Dalal': [1, 5, 2, 6, 7],
              'Ola': [19.5, 20, 20, 29.5, 10]}


def students_names():
    print('Enter the class name')
    a=str(input())
    if a=='grade_one':
        b=str(list(grade_one.keys()))
    elif a =='grade_two':
        b=str(list(grade_two.keys()))
    elif a == 'grade_three':
        b=str(list(grade_three.keys()))
    else :
        b="Not defined"
    print("Students names",a,b)

def student_score():
    print('Enter the class name, and the student name')
    grade=str(input())
    if grade=='grade_one':
        name=str(input())
        sum1=sum(grade_one[name])
    elif grade=='grade_two':
        name=str(input())
        sum1=sum(grade_two[name])
    elif grade=='grade_three':
        name=str(input())
        sum1=sum(grade_three[name])
    else :
        name='Not defined'
    print('Student degree',name,sum1)

def students_count():
    print('Enter the class name')
    a=str(input())
    if a=='grade_one':
        c=str(len(grade_one.keys()))
    elif a =='grade_two':
        c=str(len(grade_two.keys()))
    elif a == 'grade_three':
        c=str(len(grade_three.keys()))
    else :
        c="Not defined"
    print("Number of students:",c)

def menu():
    print("Choose one: students_names, student_score, students_count ")
    Enter=str(input())
    if Enter == 'students_names':
        students_names()
    elif Enter =='student_score':
        student_score()
    elif Enter =='students_count':
        students_count()
def ret():
    while True:
        print("If you finish write done or more To complete")
        answer=str(input())
        if answer=='more':
            menu()
            continue

        else:
            print("Good bye")
            break

menu()
ret()
