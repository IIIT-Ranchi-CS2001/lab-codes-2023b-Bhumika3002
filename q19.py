#Generate two tuples to represent two distinct points in space. (Three dimensional geometry). Determine the Euclidian distance between the two.
import math
t1=(1,2,3)
t2=(4,5,6)
sum=(math.pow((t2[0]-t1[0]),2)+math.pow((t2[1]-t1[1]),2)+math.pow((t2[2]-t1[2]),2))
distance=math.sqrt(sum)
print(distance)