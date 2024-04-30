import multiprocessing
import two_way_traci


if __name__ == "__main__":

    num_procesos = 16

    # Crear un grupo de procesos
    with multiprocessing.Pool(processes=num_procesos) as pool:
        pool.map(two_way_traci.main(), range(num_procesos))





