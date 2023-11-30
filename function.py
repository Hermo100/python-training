# def calc_gross(benefits,basic_salary):
#     gross_salary=basic_salary+benefits
#     return gross_salary
# basic_salary = int(input("enter basic salary: "))
# benefits = int(input("enter benefits: "))

# gross=calc_gross(basic_salary,benefits)

# def area(a,b):
#     area=(a*b)/2
#     return area

# triangle1=area(20,10)
# print(triangle1)

# def check_number(maths):
#     if maths%2==0:
#       maths="even"
#     else:
#         maths="odd"
#     return maths
    
# number=int(input("enter a number"))
# num=check_number(number)
# print(num)

def subjects(math,eng,swa,sci,sos):
    total_marks=math+eng+swa+sci+sos
    return total_marks

math=int(input("enter math marks: "))
eng=int(input("enter eng marks :"))
swa=int(input("enter swa marks :"))
sci=int(input("enter sci marks :"))
sos=int(input("enter sos marks :"))

marks=subjects(math,eng,swa,sci,sos)
print(marks)

def average(marks):
    average_marks=marks/5
    return average_marks

avg=average(marks)
print(avg)

def grading(avg):
    if avg>=79:
        grade="A"
    elif avg>=60 and avg<79:
        grade="B"
    elif avg>=49 and avg <=59:
        grade="C"
    elif avg>=40 and avg<=49:
        grade="D"
    else:
        grade="E"
    return grade
    
grades=grading(avg)
print(grades)