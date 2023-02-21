import matplotlib.pyplot as plt
import pandas as pd

url_ebola_inf = 'F:/Drive D Lenovo_S540/ECE210 Signal and Sustem/Project/EBOLACases.csv'
url_ebola_died = 'F:/Drive D Lenovo_S540/ECE210 Signal and Sustem/Project/EbolaDied.csv'
url_swinflu_died = 'F:/Drive D Lenovo_S540/ECE210 Signal and Sustem/Project/NoOfDeathRateSwinFlu.csv'
url_swinflu_inf = 'F:/Drive D Lenovo_S540/ECE210 Signal and Sustem/Project/No_of_Swin_Flu_Cases.csv'
url_corona_inf = 'F:/Drive D Lenovo_S540/ECE210 Signal and Sustem/Project/CovidWorldInfec.csv'
url_corona_died = 'F:/Drive D Lenovo_S540/ECE210 Signal and Sustem/Project/CovidDeath.csv'

data_ebola_inf = pd.read_csv(url_ebola_inf)
data_ebola_die  = pd.read_csv(url_ebola_died)
data_swinflu_inf = pd.read_csv(url_swinflu_inf)
data_swinflu_die = pd.read_csv(url_swinflu_died)
data_covid_inf = pd.read_csv(url_corona_inf)
data_covid_die = pd.read_csv(url_corona_died)
# Corona infected vs Ebola infected
print("       You have multiple ways to comapre 2 virus  ")
print("1----- Corona infected vs Ebola infected          ")
print("2----- Corona infected vs Swin FLu infected       ")
print("3----- Swin FLu vs Ebola infected                 ")
print("4----- Corona vs Ebola death count                ")
print("5----- Corona vs Swin FLu count                   ")
print("6----- Swin FLu vs Ebola death count              ")
choice = int(input("Choose the comparison you want"))
if(choice==1):
    ax = data_covid_inf.plot()
    data_ebola_inf.plot(ax=ax)
    plt.show()
#data_swinflu_inf.plot()
'''ax1 =str( data_covid_inf['Date'])
ax1 = float(ax1)
print(ax1)
ay1 = data_covid_inf['Covid Infected']
print(ay1)
plt.plot(ax1,ay1)
'''
    
if(choice==2):

# Corona infected vs SwinFlu infected
    ax = data_covid_inf.plot()
#data_ebola_inf.plot(ax=ax)
    data_swinflu_inf.plot(ax=ax)
    plt.show()
'''ax1 =str( data_covid_inf['Date'])
ax1 = float(ax1)
print(ax1)
ay1 = data_covid_inf['Covid Infected']
print(ay1)
plt.plot(ax1,ay1)
'''
    

if(choice==3):
# SwinFlu vs Ebola infected
#data_covid_inf.plot()
    ax= data_ebola_inf.plot()
    data_swinflu_inf.plot(ax=ax)
    plt.show()
'''ax1 =str( data_covid_inf['Date'])
ax1 = float(ax1)
print(ax1)
ay1 = data_covid_inf['Covid Infected']
print(ay1)
plt.plot(ax1,ay1)
'''


#------------------------------
if(choice==4):
# Corona died vs Ebola died
    ax= data_covid_die.plot()
    data_ebola_die.plot(ax=ax)
#data_swinflu_inf.plot()
    plt.show()

if(choice==5):

# Corona died vs SwinFlu died
    ax = data_covid_die.plot()
#data_ebola_inf.plot(ax=ax)
    data_swinflu_die.plot(ax=ax)
    plt.show()

if(choice==6):

# SwinFlu vs Ebola die
#data_covid_inf.plot()
    ax= data_ebola_die.plot()
    data_swinflu_die.plot(ax=ax)
    plt.show()
