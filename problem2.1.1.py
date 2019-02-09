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

pool = mp.Pool(mp.cpu_count())

def base_function(L,n,p,k):
    numlist = enumerate_list(L=L,n=n)
    possible = possible_options(L=L,n=n,numlist=numlist)
    if k >= 200:
        iter=1000
    else:
        iter= 100000
    com_list = [pool.apply(sample, args=(k,possible)) for x in range(0,iter)]
    lengths=[len(x) for x in com_list]
    #total_list=[]
    #for x in range(n,L+1):
        #n_comb=lengths.count(x)
        #proportion=n_comb/len(lengths)
        #proportion=round(proportion,3)
        #sequenced_error=proportion*(x)*(p)
        #non_sequenced_error=proportion*(L-x)*(1-0.25)
        #summation=sequenced_error+non_sequenced_error
        #total_list.append(n_comb)
        #print(sequenced_error)
        #print(non_sequenced_error)
    #total_list=sum(total_list)
    total_list=sum(lengths)/len(lengths)
    return total_list
#8573 31 0.088 100
L=8573
n=31
p=0.088
k=100
n = base_function(L=L,n=n,p=p,k=k)
print(n)

#with open("test2.txt") as f:
#    for line in f:
#        line = line.split(" ")
#        n = base_function(L=int(line[0]),n=int(line[1]),p=float(line[2]),k=int(line[3]))
#        print(n)