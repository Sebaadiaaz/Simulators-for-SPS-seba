<<<<<<< HEAD
import shapely
=======
#import shapely
>>>>>>> f96bd5f16050c5c36add83514447fe7e6800d28d
#from shapely import LineString, Point, Polygon
from Obstacles import Obstacles
import numpy as np
#point = Point(0, 0)
#print(shapely.distance(Point(10, 0), point))
#print(shapely.distance(LineString([(1, 1), (1, -1)]), point))
#print(shapely.distance(Polygon([(3, 0), (5, 0), (5, 5), (3, 5), (3, 0)]), point))
#print(shapely.distance(Point(), point))
#print(shapely.distance(None, point))


locationTx=[276,432]
locationRx=[276,800]
obstacles = Obstacles()
print(obstacles.getObsaclesLossess(locationTx,locationRx))

list=[0, 1, 2, 3,5,6,7,8,9, 4]

list2 = [list,[0]*len(list)]

list2[1][list2[0].index(4)]=1



print(list2)
print(sum(list2[1]))
Disntances = np.arange(25, 525, 25)

print(Disntances)

a = False
b = True

if a and b: print("Hola printie un bool")
