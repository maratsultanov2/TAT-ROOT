import numpy as np
from scipy.signal import argrelextrema
def adaptive_anchors(series, window=5, tol=0.1):
    n=len(series)
    if n<window: return np.array([np.argmin(series)])
    smooth=np.convolve(series,np.ones(window)/window,mode='valid')
    raw=argrelextrema(smooth,np.less,order=min(window,len(smooth)//2))[0]
    if len(raw)<2: return np.array([np.argmin(series)])
    if len(raw)>2:
        vals=series[raw]; thr=np.mean(vals)+tol*np.std(vals)
        filtered=raw[vals<thr]
        return filtered if len(filtered)>0 else np.array([np.argmin(series)])
    return raw
