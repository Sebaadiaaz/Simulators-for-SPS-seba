# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 11:11:38 2021
@author: XIN
"""
#import random
import numpy as np
def GenerateVehicleLocation(NumVehicle,FirstVehicleLocation,VehicleLength,IntraDistance,lane):  
    VehicleLocation=[[]]*NumVehicle
    #dis=int(4000/NumVehicle)
    for i in range(0,NumVehicle):
        if i < lane:
            VehicleLocation[i]=[FirstVehicleLocation[0],FirstVehicleLocation[0]+3.75*(i%lane)]
        else:
#            VehicleLocation[i] = [VehicleLocation[i-lane][0] + VehicleLength + IntraDistance+random.randint(0,int(dis/2*100))*0.01-dis/4,
#             VehicleLocation[i-lane][1]]
            #VehicleLocation[i] = [VehicleLocation[i-lane][0] + VehicleLength + IntraDistance+random.randint(0-int(dis/2*50),int(dis/2*50))*0.01,
            # VehicleLocation[i-lane][1]]

            VehicleLocation[i] = [VehicleLocation[i-lane][0] + VehicleLength + np.random.exponential(scale=IntraDistance),
             VehicleLocation[i-lane][1]]
            
            #VehicleLocation[i] = [VehicleLocation[i-1][0] + VehicleLength + IntraDistance,VehicleLocation[0][1]]
    return VehicleLocation