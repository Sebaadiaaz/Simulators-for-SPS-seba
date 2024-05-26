import numpy as np
import pandas as pd
from RBG import RBG
import time
from random import randrange
import csv

#print(randrange(10))
#sumo_ped_vehicle_location_sec_
#/home/simu5g/Simulators-for-SPS/OOP_for_SPS/traffic_data_ped/
time_period_all=50000

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

for section_index in range(0,int(time_period_all/10000)):
    #location_file_name = 'sumo_vehicle_location_'+ str(section_index)
    #location_file_name = 'manhattan_location_s20_'+ str(section_index)
    #location_file_name = 'sumo_vehicle_location' # + str(section_index)
    location_file_name = 'v19sumo_ped_vehicle_location_sec_' + str(section_index) 
    print('section_index',section_index)
    #Data=np.array(pd.read_csv("C:/Users/adani/OneDrive/Documentos/GitHub/SimulatorSPS/OOP_for_SPS/traffic_data_ped_v2/%s.csv"%(location_file_name),header=None)).tolist()
    Data=np.array(pd.read_csv("/home/ayanez/Simulators-for-SPS/sumo_simulation/Ped_simu_SUMO/Data_ped/%s.csv"%(location_file_name),header=None)).tolist()
    NewData=[]
    for i in range(0,len(Data)):
        p=randrange(10)
        type=[]
        #print(p) 
        #if p>=0 and p<2:   
        #    type=1
        #elif p>=2 and p<6:   
        #    type=2
        #else:   
        #    type=3
        if Data[i][3] == "DEFAULT_PEDTYPE" or Data[i][3] == "motorcycle" or Data[i][3] == "moped" or Data[i][3] == "slowbicycle" or Data[i][3] == "fastbicycle" or Data[i][3] == "avgbicycle":  
            type=1 #Type 1 corresponds to VRU
        else:
            type=2 #Type 2 corresponds to car
        NewData.append([Data[i][0],Data[i][1],Data[i][2],type])
    
    #filename='v2manhattan_location_s20_'+str(section_index)
    filename='type_v19sumo_ped_vehicle_location_sec_'+str(section_index)
    n=0
    #f=open("C:/Users/adani/OneDrive/Documentos/GitHub/SimulatorSPS/OOP_for_SPS/traffic_data_ped_v2/%s.csv"%filename,'w',newline='')
    f=open("/home/ayanez/Simulators-for-SPS/OOP_for_SPS/traffic_data_ped_v19/%s.csv"%filename,'w',newline='')
    
    writer=csv.writer(f)
    
    for j in NewData:
        writer.writerow(j)
    f.close()
  
