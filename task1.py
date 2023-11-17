#question 1
name="  JOHn  ."
name=name[0:6].lower().strip()
print(name)
#question 2
my = "The Dog Breed is German Shepherd"
my=my[8:23]
print(my)
#questtion 2b
word= 'Defeats for the Clinton forces, this was her moment of triumph'
word=word[16:30]
print(word)
#question 3
old="The lazy dog; ran so fast; it hit the wall."
old=old.split(";")
print(len(old))
#question 4
first_name="  Joh.n"  
first_name=first_name.replace(".","").strip()
last_name="   Do,e" 
last_name=last_name.replace(",","").strip()
print(first_name+" "+last_name)
#question 5
r = '["E","W","C"]'
#r=r.replace(r,"EWC")
r2=''.join(filter(str.isalpha,r))
print(r2)
