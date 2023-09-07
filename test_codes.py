# open_menu = open("menu.txt", "r")
# # opens the menu.txt file for reading and all the text file contents
# # a list of strings
# lines = open_menu.readlines()

# # makes each line a list with the name of the pizza and all the ingredients as 2 total
# # list elements for each list
# for eachLine in lines:
#     stripped_line = eachLine.strip()
#     split_lines = eachLine.split("$")
#     print(split_lines)
#     for eachItem in split_lines:
#         index = 0
#         for eachElement in eachItem:
#             if eachElement[index].isdigit() == True:
#                 eachElement.split([index])
#             index += 1
#             print(eachElement)
           
input_line = "Margarita Pizza $12 tomato sauce, mozzarella cheese, cheddar cheese"
pizza_info = input_line.split(' $')
print(pizza_info)
name = pizza_info[0]
string_price = pizza_info[1][:2]
index = 0
#print(name)
price = float(string_price)
#print(string_price)
toppings = pizza_info[1][3:]
print(toppings)

# myList = []
# myList.append(name)
# print(myList)
# myList.append(price)
# myList.append(toppings)
# print(myList)
# print(myList[0], myList[1], myList[2][0])



