def calc_gross(benefits,basic_salary):
    gross_salary=basic_salary+benefits
    return gross_salary
basic_salary = int(input("enter basic salary: "))
benefits = int(input("enter benefits: "))

gross=calc_gross(basic_salary,benefits)
print(gross)