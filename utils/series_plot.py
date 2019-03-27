import matplotlib.pyplot as plt


def plot_multi_series(series_list,index_list = [], title_names = []):
    if not len(index_list):
        num_display = len(series_list)
    else: num_display = len(index_list)
    if num_display > 9:
        num_display=9
    plot_index = num_display*100+10
    # plotting properties 
    len_x = 12
    len_y = 2*num_display
    fig = plt.figure(figsize=(12,len_y))
    for i in range(num_display):
        plot_index+=1
        ax = fig.add_subplot(plot_index)
        idx = i
        if index_list:
            idx = index_list[i]
        
        label = "series %d"%(idx)
        if len(title_names):
            label = title_names[idx]
        ax.plot(series_list[idx],label=label)
        ax.legend(loc=0)
    plt.show()
    return 1
    