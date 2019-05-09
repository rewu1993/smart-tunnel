import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize 
import numpy as np

def scan_digit(word):
    for c in word:
        if c.isdigit():
            return True
    return False

def clean_key(k):
    clean_words = []
    for w in word_tokenize(k):
        if len(w)>1 and not w.isdigit():
            # remove numbers 
            if not scan_digit(w):
#             for w_s in w.split('-'):
#                 if not "." in w_s:
                clean_words.append(w.lower())
    return clean_words
           
#encoding using the words set
def sentence_encoding(s,words_dict):
    encoding = np.zeros(len(words_dict))
    for w in s:
        idx = words_dict.index(w)
        if encoding[idx]==1:
            print (w,"duplicate")
        encoding[idx] +=1 
    return encoding
             
    
def find_uncorr_pair(coor_mat,thre = 0.9):
    anomaly_idx_pair = np.where(coor_mat<thre)
    x_coord = anomaly_idx_pair[0]
    y_coord = anomaly_idx_pair[1]
    coord_list = []
    for i,j in zip(x_coord,y_coord):
         coord_list.append((i,j))
    coord_list = list(set(tuple(sorted(l)) for l in coord_list))
    return coord_list

def search_k(search_s,keys,not_s=[],thre=0.8):
    ret = []
    for k in keys:
        count = 0
        skip_flag = False
        k_w_list = clean_key(k)
        for n_w in not_s:
            if n_w.lower() in k_w_list:
                skip_flag = True
                continue
        if not skip_flag:
            for s_w in search_s:
                if s_w.lower() in k_w_list:
                    count+=1
            prec = count/len(search_s)
            if prec>thre:
                ret.append(k)
    return ret
            
            
def get_series_data(data,keys,unit=True):
    sample_keys = keys
    if unit:
        sample_data = data[sample_keys][1:].astype('float')
        units = data[sample_keys][:1].values[0]
    else:
        sample_data = data[sample_keys].astype('float')
        units = len(sample_keys)*[0]
    series_data = sample_data.values.transpose()
    keys_with_unit = []
    for i,k in enumerate(sample_keys):
        u = str(units[i])
        comp = k+" ; "
        if unit:
            comp += u
        keys_with_unit.append(comp)
    return (series_data,keys_with_unit)
def explore_uncor(uncor_pair,series_data,keys):
    idx_pool = []
    for pair in uncor_pair:
        idx_0,idx_1 = pair[0],pair[1]
        print ("uncorrelate parameters: "+keys[idx_0]+" "+ keys[idx_1])
        idx_pool.append(idx_0)
        idx_pool.append(idx_1)
    idx_pool = list(set(idx_pool))
    if len(idx_pool):
        plot_multi_series(series_data,index_list=idx_pool,title_names=sample_keys)
        