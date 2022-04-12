def calculate_bereavement_coordinate_information(x,y):
    if (1400 <= x and x < 2300) and (600 <= y and y < 1500):
        return 'Face'
    elif (1150 <= x and x < 2300) and (1500 <= y and y < 2000):
        return 'Body'
    elif (2500 <= x and x < 3350) and (300 <= y and y < 2000):
        return 'Closet'
    elif (2000 <= x and x < 2270) and (6000 <= y and y < 1250):
        return 'Poster'
    else :
        return 'Background'

def calculate_nurse_coordinate_information(x,y):
    if (1500 <= x and x < 2100) and (800 <= y and y < 1650):
        return 'Face'
    elif (1300 <= x and x < 2200) and (1650 <= y and y < 2000):
        return 'Body'
    elif (0 <= x and x < 500) and (0 <= y and y < 1000):
        return 'Desk'
    elif (0 <= x and x < 200) and (1000 <= y and y < 2160):
        return 'Vase'
    elif (300 <= x and x < 500) and (1000 <= y and y < 2160):
        return 'Portrait'
    else :
        return 'Background'
