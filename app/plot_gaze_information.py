import configparser
import display_diagram as display

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

# print("Whose gaze information do you want 'BEREAVED FAMILY' or 'NURSE' or ALL ?")
# user = input("Please enter b/n/a : ")
# print("Which gaze plot mode do you want 'SHORT' or 'LONG' ?")
# mode = input("Please enter s/l : ")

# if user == 'a':
#     display.scatter_diagrams()
# else :
#     display.scatter_diagram(user)

display.scatter_diagram('BEREAVED FAMILY')
