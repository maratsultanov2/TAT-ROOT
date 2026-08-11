import numpy as np
def tat_monitor(series, window=3, sigma=2.0):
    n=len(series); signal=np.zeros(n)
    for i in range(window,n-window):
        l=series[i-window:i]; r=series[i+1:i+window+1]
        div=np.std(l)+np.std(r)
        harm=np.corrcoef(l,r)[0,1] if np.std(l)>0 and np.std(r)>0 else 0
        signal[i]=div-harm
    thr=np.nanmean(signal)+sigma*np.nanstd(signal)
    return np.where(signal>thr)[0], signal, thr
def permutation_test(series, n_perm=1000, window=3, sigma=2.0):
    obs,_,_ = tat_monitor(series,window,sigma); observed=len(obs)
    null=[]
    for _ in range(n_perm):
        s=np.random.permutation(series)
        p,_,_=tat_monitor(s,window,sigma); null.append(len(p))
    null=np.array(null); return observed, null, np.mean(null>=observed)
