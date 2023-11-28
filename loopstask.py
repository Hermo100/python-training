# question 1
num=[]
for i in range(1,51):
 num.append(i)
print(num)

# question 2
digits=[]
for i in range(1,51):
   if (i%7==0) or (i%5==0):
    digits.append(i)
print(digits)

# question 3

sum_values=0
count=0
for num in range(10,41):
    sum_values+=num
    count+=1
average=sum_values/count
print(sum_values)
print(average)



#  question 4
main=[]
for i in range(10,51):
  main.append(i)
  if i%2!=0:
   if len(main)==10:
    break
print(main)
  
  