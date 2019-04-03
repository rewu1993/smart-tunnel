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