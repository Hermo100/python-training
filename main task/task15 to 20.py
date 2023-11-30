basic_salary=int(input("enter basic salary: "))
benefits=int(input("enter benefits: "))
gross_salary=basic_salary+benefits
print(f"gross salary is {gross_salary}")

# nhif
if gross_salary <= 5999:nhifContribution = 150
elif (gross_salary >=6000 and gross_salary <= 7999):nhifContribution = 300 
elif (gross_salary>=8000 and gross_salary <= 11999):nhifContribution = 400
elif (gross_salary>=12000 and gross_salary <= 14999):nhifContribution = 500
elif (gross_salary>=15000 and gross_salary <= 19999):nhifContribution = 600
elif (gross_salary>=20000 and gross_salary <= 24999):nhifContribution = 750
elif (gross_salary>=25000 and gross_salary <= 29999):nhifContribution = 850
elif (gross_salary>=30000 and gross_salary <= 34999):nhifContribution = 900
elif (gross_salary>=35000 and gross_salary <= 39999):nhifContribution = 950
elif (gross_salary>=40000 and gross_salary <= 44999):nhifContribution = 1000
elif (gross_salary>=45000 and gross_salary <= 49999):nhifContribution = 1100
elif (gross_salary>=50000 and gross_salary <= 59999):nhifContribution = 1200
elif (gross_salary>=60000 and gross_salary <= 69999):nhifContribution = 1300
elif (gross_salary>=70000 and gross_salary <= 79999):nhifContribution = 1400
elif (gross_salary>=80000 and gross_salary <= 89999):nhifContribution = 1500
elif (gross_salary>=90000 and gross_salary <= 99999):nhifContribution = 1600
else:nhifContribution = 1700
print(f"nhif is {nhifContribution}")

# nssf
nssf_rate=0.06
max=18000
nssf_contribution=gross_salary*nssf_rate
if gross_salary>18000:nssf_contribution=max*nssf_rate
else:nssf_contribution=gross_salary*nssf_rate
print(f"nssf is {nssf_contribution}")   

#nhdf
nhdf_rate=0.015
nhdf_contribution=gross_salary*nhdf_rate
print(f"nhdf is {nhdf_contribution}")

# taxable income
taxable_income=gross_salary-(nssf_contribution+nhdf_contribution)
print(f" taxable income is {taxable_income}")

# payee
relief=2400
if (taxable_income <= 24000):payee = relief-relief
elif (taxable_income>24000 and taxable_income <= 32333):payee = ((24000*0.1)+((taxable_income - 24000) * 0.25))-relief
else:payee =((24000*0.1)+(8333*0.25)+((taxable_income - 32333) * 0.3))-relief
print(f" payee is {round(payee)}")

# net salary
net_salary=gross_salary-(nhifContribution+nhdf_contribution+nssf_contribution+payee)
print(f"net salary is {net_salary}")





