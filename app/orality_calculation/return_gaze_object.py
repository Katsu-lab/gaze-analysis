def calculate_bereavement_coordinate_information(x,y):
    if (1250 <= x and x < 2600) and (0 <= y and y < 600):
        return 'Body'
    elif (1400 <= x and x < 2300) and (600 <= y and y < 1500):
        return 'Face'
    elif (2000 <= x and x < 2270) and (800 <= y and y < 1600):
        return 'Poster'
    elif (2900 <= x and x < 3840) and (0 <= y and y < 2000):
        return 'Closet'
    else :
        return 'Background'

def calculate_nurse_coordinate_information(x,y):
    if (0 <= x and x < 600) and (0 <= y and y < 900):
        return 'Desk'
    elif (100 <= x and x < 300) and (1000 <= y and y < 1500):
        return 'Flower'
    elif (340 <= x and x < 640) and (1000 <= y and y < 1470):
        return 'Portrait'
    elif (1500 <= x and x < 2700) and (0 <= y and y < 420):
        return 'Body'
    elif (1700 <= x and x < 2350) and (400 <= y and y < 1300):
        return 'Face'
    else :
        return 'Background'
