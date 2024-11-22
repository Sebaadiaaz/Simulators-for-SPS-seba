import random

class cluster():
    
    def __init__(self):
        self.cluster_IDs =[[],[],[]]    
       
    def getClusterID(self,time):
        while True:
            C_ID = random.randint(1000,9999)  # Genera un valor aleatorio entre 1 y 100
            if C_ID not in self.cluster_IDs[0]:
                self.cluster_IDs[0].append(C_ID)
                self.cluster_IDs[1].append(time)
                return C_ID

    def deleteCluster(self,ID,time):
        ind=self.cluster_IDs[0].index(ID)
        self.cluster_IDs[2][ind]=time


