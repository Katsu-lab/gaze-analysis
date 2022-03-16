def calculate_coordinate_information(x,y):
    if (0 <= x and x <= 300) and (0 <= y and y <= 300):
        return 'Face'
    elif (0 <= x and x <= 0) and (0 <= y and y <= 0):
        return 'Eye'
    elif (0 <= x and x <= 0) and (0 <= y and y <= 0):
        return 'Mouth'
    elif (0 <= x and x <= 0) and (0 <= y and y <= 0):
        return 'Desk'
    elif (0 <= x and x <= 0) and (0 <= y and y <= 0):
        return 'Vase'
    elif (0 <= x and x <= 0) and (0 <= y and y <= 0):
        return 'Portrait of deceased person'
    elif (0 <= x and x <= 0) and (0 <= y and y <= 0):
        return 'Background'

