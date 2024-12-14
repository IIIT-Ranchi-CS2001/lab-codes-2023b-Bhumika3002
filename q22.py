#Enter the coordinates of two points on the cartesian plane (take user input using comprehension). Find the equation of the straight line passing through these points.# Take user input for two points (x1, y1) and (x2, y2)
x1, y1 = [int(i) for i in input("Enter coordinates of first point (x1 y1): ").split()]
x2, y2 = [int(i) for i in input("Enter coordinates of second point (x2 y2): ").split()]


if y1 == y2:
    print(f"The line is vertical, equation is x = {x1}")
else:
   
    slope = (x1 - x2) / (y1 - y2)

   
    print(f"The equation of the line is: (x - {x1}) = {slope} * (y - {y1})")



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 