import matplotlib.pyplot as plt
import numpy as np


def compute_fig_info(num_display):
    #split into several figures if number of plots exceed 9
    if num_display > 9:
        num_fig = int(num_display/9)
        last_fig_num = num_display%9
        num_display = num_fig*[9]
        if last_fig_num:
            num_display = num_fig*[9]+[last_fig_num]
    else: num_display = [num_display]
    return num_display


def plot_multi_series(series_list,index_list = [], title_names = [], x_series = []):
    plt.rcParams.update({'font.size': 18})
    
    if not len(index_list):
        num_display = len(series_list)
    else: num_display = len(index_list)
    display_list = compute_fig_info(num_display)
    if not len(x_series):
        x_series = np.linspace(0,len(series_list[0])-1,len(series_list[0]))
            
    for base,num_display in enumerate(display_list):
        plot_index = num_display*100+10
        # plotting properties 
        len_x = 12
        len_y = 2*num_display
        fig = plt.figure(figsize=(12,len_y))
        for i in range(num_display):
            plot_index+=1
            ax = fig.add_subplot(plot_index)
            idx = 9*base+i
            
            if index_list:
                idx = index_list[i]
                
            label = "series %d"%(idx)
            if len(title_names):
                label = title_names[idx]
            ax.plot(x_series,series_list[idx],label=label)
            ax.legend(loc=0)
    plt.xlabel('Sample Points')
    plt.ylabel('Measuremnts')
    plt.show()
    return True
    