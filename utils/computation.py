import numpy as np

def compute_corr(x,y):
    if len(x)!=len(y):
        raise RuntimeError("length of the input series should be same")
    x0 = x-np.mean(x)
    y0 = y-np.mean(y)
    l = len(x)
    return (np.dot(x0,y0)/l)/(np.std(x)*np.std(y))
    
def compute_corr_matrix(series_list):
    dim = len(series_list)
    mat = np.zeros([dim,dim])
    for i in range(dim):
        for j in range(dim):
            x = series_list[i]
            y = series_list[j]
            corr = compute_corr(x,y)
            mat[i,j] = corr
    return mat

def corr_dist_lag0(x,y):
    return 1-abs(compute_corr(x,y))