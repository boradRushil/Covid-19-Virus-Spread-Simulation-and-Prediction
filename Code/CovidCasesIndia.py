import pandas as pd
import matplotlib.pyplot as plt
url_conf = 'F:/Drive D Lenovo_S540/ECE210 Signal and Sustem/Project/COVID_19_Cases_Conf.csv'
data_conf = pd.read_csv(url_conf)

plt.figure(figsize=(20,5))
plt.plot(data_conf['Month'],data_conf['Covid Confirmed Cases in India'])
print(data_conf)
plt.show()
