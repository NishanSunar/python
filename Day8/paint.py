import math
def paint_calc(height, width, cover):
    no_of_cans = math.ceil((height * width)/cover)
    print(f"You'll need {no_of_cans} numbers of cans.")
test_h = int(input("Height of wall:"))
test_width = int(input("width of wall:"))
coverage = 5
paint_calc(height=test_h, width = test_width, cover = coverage)