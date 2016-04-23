from numpy import *
import matplotlib.pyplot as plt
import os
import os.path


def show_in_matplot(chip_trend,name):
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
    plt.xlabel('Time')
    plt.ylabel('Chips')
    plt.savefig(name)
    plt.gcf().clear()
    
def get_file_list(rootdir):
    file_route_list = []
    for parent,dirnames,filenames in os.walk(rootdir):
        for filename in filenames:
            if filename[-4:]=='.txt':
                file_route_list.append(filename)
    return file_route_list
    
