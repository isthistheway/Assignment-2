open_menu = open("menu.txt", "r")
# opens the menu.txt file for reading and all the text file contents
# a list of strings
lines = open_menu.readlines()

# makes each line a list with the name of the pizza and all the ingredients as 2 total
# list elements for each list
for eachLine in lines:
    stripped_line = eachLine.strip()
    split_lines = eachLine.split("$")
    for eachItem in split_lines[1]:
        print(eachItem)