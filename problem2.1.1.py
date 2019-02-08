from itertools import chain
import itertools
import numpy as np
import random
import multiprocessing as mp


def unique(x):
    unique_list=[]
    for i in x:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

def enumerate_list(L,n):
    h=enumerate(range(0, L), 1)
    t=enumerate(range(0, n-1), 1)
    numlist=[]
    [numlist.append(x[1]) for x in h]
    [numlist.append(x[1]) for x in t]
    return numlist

def possible_options(L,n,numlist):
    possible=[]
    for i in range(0,L):
        tmp=[]
        [tmp.append(numlist[x]) for x in range(i,i+n)]
        possible.append(tmp)
    return possible 

def sample(k,possible):
    com=[possible[random.randint(0,len(possible)-1)] for i in range(0, k)]
    joined_list=[]
    for x in com:
        for i in x:
            joined_list.append(i)
    com=joined_list
    com=unique(x=com)
    return com

L = 31
n = 5
k = 43
numlist = enumerate_list(L=L,n=n)
possible = possible_options(L=L,n=n,numlist=numlist)


pool = mp.Pool(mp.cpu_count())
print(mp.cpu_count())

#com_list=[]
#counter=0

com_list = [pool.apply(sample, args=(k,possible)) for x in range(0,10000)]

#while counter <= 100:
#    com = sampling(k=k,possible=possible)
#    com_list.append(com)
#    counter = counter + 1

lengths=[len(x) for x in com_list]
tmp=[lengths.count(x) for x in range(n,L+1)]
print(tmp)