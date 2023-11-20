my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76,"John")]
print(my_ds[3][2]["currency"])
# quetsion 2
print(my_ds[2])
# questuion 3
print(my_ds[3][1])
# question4

my_ds[3][2]["amount"]=90
print(my_ds)

# question5
my_ds[4]=str(my_ds[4])
print(my_ds[4][-1::-1])
# question 6
list(my_ds[5][1])
my_ds[5]="jane"
print(my_ds)