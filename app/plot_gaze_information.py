import configparser
import display_diagram as display

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

print('\n\n------------------- Gaze Information Plot Setting -------------------')

print("\nWhose gaze information do you want 'BEREAVED FAMILY' or 'NURSE' or ALL ?")
user = input("Please enter b/n/a : ")

print("\nWhich plot time span do you want 'SHORT' or 'LONG' ?")
span = input("Please enter s/l : ")

if span == 'l':
    print("\nWhich plot mode do you want 'LINE' or 'POINT' ?")
    mode = input("Please enter l/p : ")
else :
    mode = 'p'

# if user == 'a':
#     display.scatter_diagrams(span, mode)
# else :
#     display.scatter_diagram(user, span, mode)

display.scatter_diagram('BEREAVED FAMILY', span, mode)
# display.scatter_diagrams()
