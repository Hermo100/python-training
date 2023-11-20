person = {
    "name" : "John Doe", 
    "age":30, 
    "location": "Nairobi",
    "email" :"johndoe@mail.com"
    }
print(person["email"])
# # adding values to dictionaries
person["age"]=57
person["email"]="djdj@gmail.com"
person["location"]="mombasa"
person["name"]="jane doe"
print(person)
# # adding a new key value pair
print(person)
# methods
print(person.get("name"))
print(person.copy())
person.pop("age")
print(person)
person.values()
print(person.values())
new_data={"course":"education","campus":"nairobi"}
person.update(new_data)
print(person)
print(person.popitem())
print(person.keys())