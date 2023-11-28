# n="10"
# for i in n:
#     print(i)
y=range(0,10)
for i in y:
    print(i)
nov_intake=["antony","tosh","ramadhan","cornelius","lilian","herman","bilal","iano","abigail"]
for i in nov_intake:
    if i=="herman":
        break
    print(i)

    person = {
    "name" : "John Doe", 
    "age":30, 
    "location": "Nairobi",
    "email" :"johndoe@mail.com"
    }
    for key,value in person.items():
        print(key,value)