numbers = [1, 2, 3]
new_list = []

new_list = [ n + 1 for n in numbers]

print(numbers, new_list)


#new_list = [expression for item in iterable]
# 
# Strings list comphrension
name = "Brent"
letters_in_name = [letter for letter in name]
name2 = ""
print(letters_in_name)

for letter in letters_in_name:
    name2 += letter
    
print(f"name = {name2}")

#3Challenge
doubled_number = [n*2 for n in range(1,5)]

print(doubled_number)

#conditional list comphersion

#new_list = [ n for n in list
# 
shortnames = [item for item in list if len(item) <=4]
