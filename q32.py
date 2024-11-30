'''A group of people from different parts of Ranchi visited ‘Universal Studio’, Singapore and they enjoyed various fun events.
The first event was ‘Roller Coaster’ for which the ticket price was 44 dollars for male, 38 dollars for females and 21 dollars for kids. They spent a total of 1412 dollars for this event. Second event was ‘4D Max Cinema’ for which ticket prices were 32 dollars, 28 dollars and 15 dollars respectively. They spent 1024 dollars for this event.
Finally they had a ‘cable car’ trip for which the ticket prices were 24 dollars, 20 dollars and 10 dollars respectively. They spent 728 dollars for the cable car trip.
Determine the number of males, females and kids in the group. (Use numpy)'''
import numpy as np

A = np.array([[44, 38, 21],
              [32, 28, 15],
              [24, 20, 10]])

b = np.array([1412, 1024, 728])

x = np.linalg.solve(A, b)

m, f, k = x

print(f"Number of males: {int(m)}")
print(f"Number of females: {int(f)}")
print(f"Number of kids: {int(k)}")
