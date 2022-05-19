def calculate_bereavement_coordinate_information(x,y,resize):
    if ((1250 / resize) <= x and x < (2600 / resize)) and (0 <= y and y <( 600 / resize)):
        return 'Body'
    elif ((1400 / resize) <= x and x < (2300 / resize)) and ((600 / resize) <= y and y < (1500 / resize)):
        return 'Face'
    elif ((2000 / resize) <= x and x < (2270 / resize)) and ((800 / resize) <= y and y < (1600 / resize)):
        return 'Poster'
    elif ((2900 / resize) <= x and x < (3840 / resize)) and (0 <= y and y < (2000 / resize)):
        return 'Closet'
    else :
        return 'Background'

def calculate_nurse_coordinate_information(x,y,resize):
    if (0 <= x and x < (600 / resize)) and (0 <= y and y < (900 / resize)):
        return 'Desk'
    elif ((100 / resize) <= x and x < (300 / resize)) and ((1000 / resize) <= y and y < (1500 / resize)):
        return 'Flower'
    elif ((340 / resize) <= x and x < (640 / resize)) and ((1000 / resize) <= y and y < (1470 / resize)):
        return 'Portrait'
    elif ((1500 / resize) <= x and x < (2700 / resize)) and (0 <= y and y < (420 / resize)):
        return 'Body'
    elif ((1700 / resize) <= x and x < (2350 / resize)) and ((400 / resize) <= y and y < (1300 / resize)):
        return 'Face'
    else :
        return 'Background'
