from numpy import *
import matplotlib.pyplot as plt

def show_in_matplot(chip_trend):
    chip_ndarray = array(chip_trend)
    time_list = []
    for i in range(0,len(chip_trend)):
        time_list.append(i)
    time_ndarray = array(time_list)
    print(ndarray)
    y = chip_ndarray
    x = time_ndarray
    max = 0
    for i in chip_trend:
        if i>max:
            max = i
    plt.plot(x,y)
    plt.xlim(0,len(chip_trend))
    plt.ylim(0,max+5)
    plt.show()
    
show_in_matplot(chip_trend)
    
