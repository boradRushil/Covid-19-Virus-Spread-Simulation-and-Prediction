import pandas as pd
import matplotlib.pyplot as plt
url = 'F:/Drive D Lenovo_S540/ECE210 Signal and Sustem/Project/COVID_19_Cases.csv'
data = pd.read_csv(url)

plt.figure(figsize=(20,5))
plt.plot(data['Months'],data['Covid Deaths in India'])

print(data)
plt.show()
