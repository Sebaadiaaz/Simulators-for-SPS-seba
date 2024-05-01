import multiprocessing
import json
import SPS_test
import numpy as np
import tqdm

def wrapper(args):
    # Función auxiliar para llamar a SPS_test.main con los argumentos
    # self.resultados.append(list(tqdm.tqdm(pool.imap_unordered(wrapper,param_list[:8]), total=len(param_list[:8])))
    return SPS_test.main(*args)

if __name__ == "__main__":

    time_period = 50000 #10201    
    start_sampling_time = 201
    interval = 50
    RC_low = 5
    RC_high = 15
    RSRP_ratio_beacon = 0.2      
    ds_list = [6, 5, 4, 3, 2, 1, 0]
    sd = 1
    td = 200 #np.arange(25, 525, 25)
    obs_list = [False, True]
    aw_list = 200 #[10, 50, 100, 200, 500]
    nr_list = True #[False, True]  
    mu_list = 0 #[0,1,2]

    param_list = []
    

    #for target_distance in td:
    for obs in obs_list:
            #for aw in aw_list:
                #for nr in nr_list:
                    #if nr:
                        #for mu in mu_list:
        for ds in ds_list:
            param = [time_period,td,start_sampling_time,interval,RC_low,RC_high,RSRP_ratio_beacon,mu_list,obs,ds,nr_list,aw_list,sd]
            param_list.append(param)
                    #else:
                    #    param = [time_period,target_distance,start_sampling_time,interval,RC_low,RC_high,RSRP_ratio_beacon,mu_list[0],obs,ds,nr,aw,sd]
                    #    param_list.append(param)

    #for conf in param:
    
    # Número máximo de procesos (8 para usar 8 CPU)
    num_procesos = 14
    resultados=[]
    # Crear un grupo de procesos
    with multiprocessing.Pool(processes=num_procesos) as pool:
        #resultados = pool.map(wrapper,param_list)
        resultados.extend(list(tqdm.tqdm(pool.imap_unordered(wrapper,param_list), total=len(param_list))))

    diccionario_final = {}
    for idx, resultado in enumerate(resultados):
        resultado_dic = json.loads(resultado)
        diccionario_final[idx] = resultado_dic

    with open("Final_results_group8_Fitting_20Hz.json", "w") as archivo:
        json.dump(diccionario_final, archivo, indent=4)

    print("Archivo 'Final_results_group8_Fitting_20Hz.json' creado exitosamente.")

#    print("Archivo 'Final_results_group1.json' creado exitosamente.")

    # Ahora 'resultados' contiene los 90 resultados generados en paralelo
    # Puedes procesarlos o combinarlos según lo que necesites

    # Por ejemplo, imprimir los primeros 10 resultados
    #print(resultados[:10])

    # Combinar los resultados en un solo diccionario
    #diccionario_final = {}
    #for resultado in resultados:
    #    resultado_dic = json.loads(resultado)
    #    diccionario_final.update(resultado_dic)

    # Exportar como archivo JSON
    #with open("Final_results_group1.json", "w") as archivo:
    #    json.dump(resultados, archivo, indent=4)

    #print("Archivo 'Final_results_group1.json' creado exitosamente.")
