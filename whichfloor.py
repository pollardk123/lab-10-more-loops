maximum_stories = 20
while True :
    floor = int(input("On what floor of the building is your office?"))
    if floor > maximum_stories:
        print("you entered", "floor", "which is greater than the max floor" , "maximum_stories" , "please enter a valid number")
    elif maximum_stories>=floor:
        print("Congradulations! you entered the floor",floor)
        break
