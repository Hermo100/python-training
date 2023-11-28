prods = [['omo', '30kshs', '300'], ['milk', '50kshs', '200'], ['bread', '45kshs', '359'], ['coffee', '5kshs', '79']]

total_stock = 0


for i in prods:
  
    stock = int(i[2])
    total_stock += stock


print(f"Total Stock: {i}")