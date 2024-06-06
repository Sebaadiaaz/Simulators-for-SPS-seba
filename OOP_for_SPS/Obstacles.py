import shapely
#import shapely.distance
from shapely.geometry import Polygon, LineString, Point

class Obstacles():
    
    def __init__(self):
        self.buildings ={}
        self.beta =  9 #9.2 # in dB per wall values form Sommer's paper https://ieeexplore.ieee.org/document/5720204
        self.gamma = 0.4 #0.32 # in dB per meter values from Sommer's paper https://ieeexplore.ieee.org/document/5720204

        # Loading building from "ETSI_TR_138_913_V14_3_0_urban.poly.xml" file
        self.buildings[0] = Polygon([(262.490000,420.330000), (262.490000,12.330000), (487.490000,12.330000), (487.490000,420.330000), (326.350000,420.330000), (262.490000,420.330000)]) # Former corner: 262.490000,420.330000 South-Est Square
        self.buildings[1] = Polygon([(12.410000,853.580000), (12.410000,445.580000), (237.410000,445.580000), (237.410000,853.580000), (76.270000,853.580000), (12.410000,853.580000)]) # Former corner: 237.410000,445.580000 North-West Square
        # half building scenario self.buildings[2] = Polygon([(262.570000,853.420000), (262.570000,445.420000), (487.570000,445.420000), (487.570000,853.420000), (326.430000,853.420000), (262.570000,853.420000)]) # Former corner: 262.570000,445.420000 Nort-Est Square
        #self.buildings[3] = Polygon([(512.270000,420.480000), (512.270000,12.480000), (737.270000,12.480000), (737.270000,420.480000), (576.130000,420.480000), (512.270000,420.480000)])
        #self.buildings[4] = Polygon([(512.570000,853.080000), (512.570000,445.080000), (737.570000,445.080000), (737.570000,853.080000), (576.430000,853.080000), (512.570000,853.080000)])
        #self.buildings[5] = Polygon([(511.930000,1286.830000), (511.930000,878.830000), (736.930000,878.830000), (736.930000,1286.830000), (575.790000,1286.830000), (511.930000,1286.830000)])
        #self.buildings[6] = Polygon([(12.710000,1286.870000), (12.710000,878.870000), (237.710000,878.870000), (237.710000,1286.870000), (76.570000,1286.870000), (12.710000,1286.870000)])
        #self.buildings[7] = Polygon([(262.560000,1286.740000), (262.560000,878.740000), (487.560000,878.740000), (487.560000,1286.740000), (326.420000,1286.740000), (262.560000,1286.740000)])             
        # half building scenario self.buildings[3] = Polygon([(12.000000,420.000000), (12.000000,12.000000), (237.000000,12.000000), (237.000000,420.000000), (75.860000,420.000000), (12.000000,420.000000)]) # Former corner: 237.000000,420.000000 South-West Square


        
    def getObsaclesLossess(self,location1,location2):
        TotalLoss_dB = 0
        #TotalLoss_mW = 0
        #print(location1[0])
        #print(location2[0])
        # Drawing a line with the transmiter and receiver node
        TxRxLine = LineString( [(location1[0], location1[1]),(location2[0],location2[1]) ] ) 
        
        # Geting the intersection between the line and the buildings 
        for i in range (0,len(self.buildings)):
            polydiff = TxRxLine.intersection(self.buildings[i]) #
            xy = shapely.get_coordinates(polydiff) #polydiff.coords.xy
            #print(xy)
            #x=xy[0]
            #y=xy[1]
            #listx = list(x)
            #listy = list(y)
            #print(listx)
            #print(listy)
            if len(xy)>1: #len(listx) > 1 and len(listy) > 1 :
                pointA=Point(xy[0][0],xy[0][1]) #listx[0],listy[0])
                pointB=Point(xy[1][0],xy[1][1]) #listx[1],listy[1])
                TotalLoss_dB =  2*self.beta + pointA.distance(pointB)*self.gamma #TotalLoss_dB + 2*self.beta + shapely.distance(pointA,pointB)*self.gamma
                #TotalLoss_mW = TotalLoss_mW + 10**(TotalLoss_dB/10) #10**((2*self.beta)/10) + 10**((pointA.distance(pointB)*self.gamma)/10)
        #TotalLoss = 10**(TotalLoss_dB)+10**
        
        return TotalLoss_dB
     



