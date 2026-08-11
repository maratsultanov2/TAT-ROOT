import numpy as np, matplotlib.pyplot as plt
from tat_public import adaptive_anchors, coherence, tat_monitor
np.random.seed(42)
x=np.linspace(0,3,150); fine=0.2*(x-1.5)**2+0.05*np.random.randn(150)
anchors=adaptive_anchors(fine,5,0.1)
peaks,signal,thr=tat_monitor(fine,3,2.0)
fig,axes=plt.subplots(1,3,figsize=(15,4))
axes[0].plot(x,fine,'b-'); axes[0].scatter(x[anchors],fine[anchors],c='red',s=80)
axes[0].set_title('Anchors'); axes[0].grid(alpha=0.3)
axes[1].plot(x,signal,'k-'); axes[1].axhline(thr,color='red',linestyle='--')
axes[1].set_title('Monitor'); axes[1].grid(alpha=0.3)
c=coherence(fine[10:30],fine[80:100])
axes[2].text(0.5,0.5,f'Coherence = {c:.4f}',ha='center',va='center',fontsize=14,transform=axes[2].transAxes)
plt.tight_layout(); plt.savefig('tat_basic_example.png',dpi=150); plt.show()
