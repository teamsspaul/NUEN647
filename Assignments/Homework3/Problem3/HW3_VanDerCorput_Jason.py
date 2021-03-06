import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import random


N=50
Nbins=10
RandomNumbers=np.random.uniform(low=0,high=1,size=500000)
Samples=norm.ppf(RandomNumbers)
a=[]
b=[]
c=[]
d=[]
e=[Samples]
def vdc(n, base=2):
    vdc, denom = 0,1
    while n:
        denom *= base
        n, remainder = divmod(n, base)
        vdc += remainder / denom
    return vdc
for i in range(1,N+1):
    a.append (norm.ppf(random.random()))
    b.append (norm.ppf(1.0*(i-1)/N + random.random()/N))
    c.append (norm.ppf((vdc(i, base=2))))
    d.append (norm.ppf((vdc(i, base=3))))
    
    


plt.hist(a, bins=np.arange(16)/2.5-3) 
plt.title("Histogram of random data")
plt.savefig('C:\\PythonScripts\\UQhomework\\HW3P3Random')
plt.clf()

plt.hist(b, bins=np.arange(16)/2.5-3)  
plt.title("Histogram of stratified (50 bins) data")
plt.savefig('C:\\PythonScripts\\UQhomework\\HW3P3Stratified')
plt.clf()

plt.hist(c, bins=np.arange(16)/2.5-3) 
plt.title("Histogram of VDC 2 data")
plt.savefig('C:\\PythonScripts\\UQhomework\\HW3P3VDC2')
plt.clf()

plt.hist(d, bins=np.arange(16)/2.5-3) 
plt.title("Histogram of VDC 3 data")
plt.savefig('C:\\PythonScripts\\UQhomework\\HW3P3VDC3')
plt.clf()

plt.hist(e, bins=np.arange(31)/5.0-3) 
plt.title("Histogram with many points")
plt.savefig('C:\\PythonScripts\\UQhomework\\HW3P3ManyPoints')
plt.clf()
