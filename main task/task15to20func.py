# gross salary
def gross(basic,benefits):
    final_salary=basic+benefits
    return final_salary
basic=int(input("enter basic salary: "))
benefits=int(input("enter benefits: "))

gross_salary=gross(basic,benefits)
print(f" gross salary is {round(gross_salary,2)}")

# nhif
def nhif(gross_salary):
 if gross_salary <= 5999:nhifContribution = 150
 elif (gross_salary >=6000 and gross_salary <= 7999):
    nhifContribution = 300 
 elif (gross_salary>=8000 and gross_salary <= 11999):
    nhifContribution = 400
 elif (gross_salary>=12000 and gross_salary <= 14999):
    nhifContribution = 500
 elif (gross_salary>=15000 and gross_salary <= 19999):
    nhifContribution = 600
 elif (gross_salary>=20000 and gross_salary <= 24999):
    nhifContribution = 750
 elif (gross_salary>=25000 and gross_salary <= 29999):
    nhifContribution = 850
 elif (gross_salary>=30000 and gross_salary <= 34999):
    nhifContribution = 900
 elif (gross_salary>=35000 and gross_salary <= 39999):
    nhifContribution = 950
 elif (gross_salary>=40000 and gross_salary <= 44999):
    nhifContribution = 1000
 elif (gross_salary>=45000 and gross_salary <= 49999):
    nhifContribution = 1100
 elif (gross_salary>=50000 and gross_salary <= 59999):
    nhifContribution = 1200
 elif (gross_salary>=60000 and gross_salary <= 69999):
    nhifContribution = 1300
 elif (gross_salary>=70000 and gross_salary <= 79999):
    nhifContribution = 1400
 elif (gross_salary>=80000 and gross_salary <= 89999):
    nhifContribution = 1500
 elif (gross_salary>=90000 and gross_salary <= 99999):
    nhifContribution = 1600
 else:
    nhifContribution = 1700
 return nhifContribution

final_nhif=nhif(gross_salary)
print(f" nhif contribution is {round(final_nhif,2)}")

# nssf
def nssf(gross_salary):
   initial_nssf=gross_salary*0.06
   if gross_salary>18000:initial_nssf=18000*0.06
   else:initial_nssf=gross_salary*0.06
   return initial_nssf
final_nssf=nssf(gross_salary)
print(f" nssf contribution is {round(final_nssf,2)}")

# nhdf
def nhdf(gross_salary):
   initial_nhdf=gross_salary*0.015
   return initial_nhdf
final_nhdf=nhdf(gross_salary)
print(f" nhdf contribution is {round(final_nhdf,2)}")
   
# taxable income
def taxable(gross_salary,final_nssf,final_nhdf):
   final_income=gross_salary-(final_nssf+final_nhdf)
   return final_income
taxable_income=taxable(gross_salary,final_nssf,final_nhdf)
print(f" taxable income is {round(taxable_income,2)}")

# payee
def paye(taxable_income):
   relief=2400
   if (taxable_income <= 24000):payee = relief-relief
   elif (taxable_income>24000 and taxable_income <= 32333):payee = ((24000*0.1)+((taxable_income - 24000) * 0.25))-relief
   else:payee =((24000*0.1)+(8333*0.25)+((taxable_income - 32333) * 0.3))-relief
   return payee
final_payee=paye(taxable_income)
print(f" payee is {round(final_payee,2)}")

# net salary
def net(gross_salary,final_nssf,final_nhdf,final_nhif,final_payee):
   final_net=gross_salary-(final_nhif+final_nhdf+final_nssf+final_payee)
   return final_net
net_salary=net(gross_salary,final_nssf,final_nhdf,final_nhif,final_payee)
print(f" net salary is {round(net_salary,2)}")