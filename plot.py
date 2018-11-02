import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime

csv = pd.read_csv("Data/log.csv", index_col = 0)

fig, ax = plt.subplots(1,1)

timestamps = []
for timestamp in csv.index:
    timestamps.append(datetime.datetime.fromtimestamp(timestamp))


ln1 = ax.plot(timestamps,csv.iloc[:,0], label = 'Temperature')
ax2 = ax.twinx()
ln2 = ax2.plot(timestamps,csv.iloc[:,1], label = 'Relative Humidity', color = 'r')

lns = ln1 + ln2
labs = [l.get_label() for l in lns]
ax.legend(lns,labs)

ax.set_xlabel('Time')
ax.set_ylabel('Temperature (C)')
ax2.set_ylabel('Relative Humidity (%)')

fig.autofmt_xdate()
plt.show()

