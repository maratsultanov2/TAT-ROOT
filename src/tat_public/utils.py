import numpy as np
def normalize(x):
    x_min,x_max=x.min(),x.max()
    return (x-x_min)/(x_max-x_min+1e-12) if x_max-x_min>1e-12 else np.zeros_like(x)
def estimate_drift(series):
    t=np.arange(len(series)); slope,_=np.polyfit(t,series,1); return slope
def block_shuffle(series, block_size=3):
    n=len(series); n_blocks=n//block_size
    blocks=[series[i*block_size:(i+1)*block_size] for i in range(n_blocks)]
    rem=series[n_blocks*block_size:]
    np.random.shuffle(blocks)
    if len(rem)>0: blocks.append(rem)
    return np.concatenate(blocks)
