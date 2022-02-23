import diagram

# print('\n\n------------------- Gaze Information Plot Setting -------------------')

# print("\nWhose gaze information do you want 'BEREAVED FAMILY' or 'NURSE' or ALL ?")
# user = input("Please enter b/n/a : ")

# print("\nWhich plot time span do you want 'SHORT' or 'LONG' ?")
# span = input("Please enter s/l : ")

# if span == 'l':
#     print("\nWhich plot mode do you want 'LINE' or 'POINT' ?")
#     mode = input("Please enter l/p : ")
# else :
#     mode = 'p'

# diagram = diagram.Diagram(user, span, mode)

# if user == 'a':
#     diagram.display_scatter_diagrams()
# else :
#     diagram.display_scatter_diagram()


####### FOR TEST #######
diagram = diagram.Diagram('b', 's', 'l')
diagram.display_scatter_diagram()
# diagram.display_scatter_diagrams()
