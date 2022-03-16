def calculate_coordinate_information(x,y):
    if (1500 <= x and x < 2500) and (0 <= y and y < 1500):
        return 'Face'
    # elif (0 <= x and x < 0) and (0 <= y and y < 2160):
    #     return 'Eye'
    # elif (0 <= x and x < 0) and (0 <= y and y < 2160):
    #     return 'Mouth'
    elif (0 <= x and x < 500) and (0 <= y and y < 1000):
        return 'Desk'
    elif (0 <= x and x < 200) and (1000 <= y and y < 2160):
        return 'Vase'
    elif (300 <= x and x < 500) and (1000 <= y and y < 2160):
        return 'Portrait'
    else :
        return 'Background'

