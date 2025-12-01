import os
import numpy as np
import multiprocessing, pathos.multiprocessing
from tqdm import tqdm


def MC_sim_batch(batch_size):
    import numpy as np
    W = 10e-6
    L = 180e-9
    Vg = 0.7
    Vd = 1

    Cox = np.random.normal(8.7e-15, 2e-15, batch_size)
    uox = np.random.normal(1.7e-15, 0.3e-15, batch_size)
    Vth = np.random.normal(-0.8, 0.2, batch_size)
    lam = np.random.normal(1/20, 1/50, batch_size)

    Ids = 0.5 * (W/L) * Cox * uox * (Vg - Vth)**2 * (1 + lam * Vd)
    return Ids


   
def run_MC_sim(N_MC, batch, N_core):
    
    os.environ['OPENBLAS_NUM_THREADS'] = '1'
    os.environ['MKL_NUM_THREADS'] = '1'

    batch_list = [batch] * (N_MC // batch)

    code_time = np.zeros(N_core)

    multiprocessing.freeze_support()
    pool = pathos.multiprocessing.ProcessingPool(N_core)

    results = list(tqdm(pool.imap(MC_sim_batch, batch_list), total=len(batch_list)))

    pool.close()     
    pool.join()      
    pool.terminate() # kills zombie 
    pool.restart()   
    del pool        

    Ids = np.concatenate(results)
    
    return Ids
