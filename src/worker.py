import json
import redis
import matplotlib.pyplot as plt

def makeplot(data):
    

    x_vals = []
    y_vals = []
    total = 0
    for i in range(len(data)):
        if data[i]['koi_disposition'] == 'CONFIRMED':
            total +=1
        year = data[i]['koi_time0bk']
        y_vals.append(total)
        x_vals.append(year)

    plt.xlabel("Years")
    plt.title("Visualization of confirmed Exoplanets over the years")
    plt.ylabel("How Many Confirmed Exoplanets")
    plt.plot(x_vals, y_vals, 'b--')
    plt.savefig('/plot.png')
    

makeplot(data)
