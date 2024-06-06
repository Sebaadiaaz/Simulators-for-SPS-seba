# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 14:48:14 2021

@author: xin
"""

import pandas as pd
import csv


for j in range(0,5):
    print("Progress: "+str(100*j/5))
    set_of_staying_nodes=[]
    vehicle_data=[] 
    for s in range(1+10000*j,10001+10000*j): #range(1+200*j,201+200*j): # range(1,6001):
         
        step_number= 220000+s #160000+s #305000+s #315000+s #360000+s #330000+s #5000+s
        #print(str(step_number))
        location_step=pd.read_csv("Data_ped/v18location_for_timestep%s.csv"%str(step_number),header=None)
        vehicle_data.append(location_step)
        if s==(1+10000*j):    # 200*j):  # list all vehicle IDs at first time-step
            set_of_staying_nodes=list(vehicle_data[0][0])
            #print(set_of_staying_nodes)
        else:  # check those non-repeated ones and delete them
            for g in set_of_staying_nodes:
                #print(g)
                if g not in list(vehicle_data[s-(1+10000*j)][0]): # 200*j)][0]):
                    set_of_staying_nodes.remove(g)      
        
    vehicle_num = len(set_of_staying_nodes)   
    print(str(vehicle_num))


# =============================================================================
# using observe_vehicles as a list to record all locations          
# =============================================================================
    observe_vehicles=[]
    for s in range(0,10000):#200): #0+j*200,200+j*200):
        for i in range(0,len(vehicle_data[s][0])):
            if vehicle_data[s][0][i] in set_of_staying_nodes:
                observe_vehicles.append([s,vehicle_data[s][1][i],vehicle_data[s][2][i],vehicle_data[s][3][i]]) # save locations of all vehicles and type -j*200
            

# =============================================================================
# save the locations of all vehicles during a given time period
# =============================================================================
    filename = '/home/ayanez/Simulators-for-SPS/sumo_simulation/Ped_simu_SUMO/Data_ped/v18sumo_ped_vehicle_location_sec_'+str(j)
    #filename = 'C:\\Users\\adani\\OneDrive\\Documentos\\GitHub\\SimulatorSPS\\OOP_for_SPS\\traffic_data_ped_v2\\v2sumo_ped_vehicle_location_sec_' + str(j)
    n=0

    f=open('%s.csv'%filename,'w',newline='')
    writer=csv.writer(f)
    for i in observe_vehicles:
        writer.writerow(i)
    f.close()

