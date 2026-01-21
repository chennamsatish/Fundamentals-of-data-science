import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
weather_data = pd.read_csv('temperature2.csv')

# Line plot for monthly temperature
plt.figure()
plt.plot(weather_data['date'], weather_data['meantemp'])
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.title("Monthly Temperature Line Plot")
plt.show()
