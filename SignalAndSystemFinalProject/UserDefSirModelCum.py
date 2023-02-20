
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
    #TotDays = int(input("Enter Days Of Graph you want"))
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

    values_S_t = df['suseptible']
    series_S_t = pd.Series(values_S_t) 
    values_I_t = df['infected']
    series_I_t = pd.Series(values_I_t) 
    values_R_t = df['recovered']
    series_R_t = pd.Series(values_R_t) 
  
# calling method 
    cumsum_S_t = series_S_t.cumsum()
    cumsum_I_t = series_I_t.cumsum()
    cumsum_R_t = series_R_t.cumsum()
    plt.plot(t,cumsum_S_t/1000,label='S')
    plt.plot(t,cumsum_I_t/1000,label='I')
    plt.plot(t,cumsum_R_t/1000,label='R')
    df1 = pd.DataFrame({
    'suseptible':cumsum_S_t,
    'infected':cumsum_I_t,
    'recovered':cumsum_R_t,
    'day':days})
    df1.plot(x='day',
        y=['infected','suseptible','recovered'],
        color=['#000','#aac6ca','#bb6424'],
        kind = 'area',
        stacked=False)
  
    print("Cummilative",df1)
    plt.show()
x = MyClass()
