
import numpy as np
import scipy
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker
class MyClass:
    N=int(input("Enter Total Population"))
    I0 = int(input("Enter No of Infected people"))
    R0 = int(input("Enter No of recovered people"))
    time_of_recov = int(input("No of days of recover"))

    S0 = N-I0-R0 #15000000        
    a = float(input("Transmission Rate "))
    def sIR_Model( y,t,N,  a , b):
        S,I,R  = y
        dS_dt = -a*S*I/N
        dI_dt = a*S*I/N - b*I
        dR_dt = b*I
        return (dS_dt,dI_dt,dR_dt)

    b = 1./time_of_recov


# Time Vector
#here written 160 because its for 160 days we have calculated
    t = np.linspace(0,160 ,160)

#INItal condition vector
    y0 = S0,I0,R0




#SOLUTION OF THIS SIR MODEL
    solution =  scipy.integrate.odeint(sIR_Model,y0,t,args=(N,a,b))
    S,I,R = solution.T

    days = range(0,160)
    df = pd.DataFrame({
    'suseptible':S,
    'infected':I,
    'recovered':R,
        'day':days})

    df.plot(x='day',
        y=['infected','suseptible','recovered'],
        color=['#000','#aac6ca','#bb6424'],
        kind = 'area',
        stacked=False)
    plt.show()
x=MyClass()