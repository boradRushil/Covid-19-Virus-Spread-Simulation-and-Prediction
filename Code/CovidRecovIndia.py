import pandas as pd
import matplotlib.pyplot as plt
url_recov = 'F:/Drive D Lenovo_S540/ECE210 Signal and Sustem/Project/COVID_19_Cases_revor.csv'
data_recov = pd.read_csv(url_recov)
plt.figure(figsize=(20,5))
plt.plot(data_recov['Month'],data_recov['Covid Cured in India'])
print(data_recov)
plt.show()
