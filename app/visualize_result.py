import diagram

# print('\n\n------------------- Gaze Information Plot Setting -------------------')

# print("\nWhose gaze information do you want 'BEREAVED FAMILY' or 'NURSE' or 'ALL' ?")
# user = input("Please enter b/n/a : ")

# print("\nWhich plot time span do you want 'SHORT' or 'LONG' ?")
# span = input("Please enter s/l : ")

# if span == 'l':
#     print("\nWhich plot mode do you want 'LINE' or 'POINT' ?")
#     mode = input("Please enter l/p : ")
# else :
#     mode = 'p'

# if user == 'a':
#     print("\nWhose gaze information do you want 'SEPALATE' or 'OVERLAP' ?")
#     graph = input("Please enter s/o : ")
# else :
#     graph = 's'

# diagram = diagram.Diagram(user, span, mode, graph)
# print('User: ' + diagram.user)
# print('Span: ' + diagram.span)
# print('Mode: ' + diagram.mode)
# print('Graph: ' + diagram.graph)

# if user == 'a':
#     diagram.display_scatter_diagrams()
# else :
#     diagram.display_scatter_diagram()

# Let's refactor and add Function annotation

####### FOR TEST #######

diagram = diagram.Diagram('a', 's', 'p', 'o')

print('User: ' + diagram.user)
print('Span: ' + diagram.span)
print('Mode: ' + diagram.mode)
print('Graph: ' + diagram.graph)

# diagram.display_scatter_diagram()
diagram.display_scatter_diagrams()
